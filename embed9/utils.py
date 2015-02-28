from django.http import Http404
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_app, get_models
from django.conf import settings
from django.shortcuts import get_object_or_404

from importlib import import_module
from urllib.parse import urlencode

APPS_MODELS = {}


def get_appmodel(app_name, model_name):
    """ Return a model class identified by given app and model names """
    app_models = APPS_MODELS.get(app_name)
    if not app_models:
        try:
            app = get_app(app_name)
        except ImproperlyConfigured:
            raise Http404
        app_models = APPS_MODELS[app_name] = dict((model._meta.model_name, model) for model in get_models(app))
        
    model = app_models.get(model_name)
    if not model:
        raise Http404
    return model


def get_embeddable(app_name, model_name):
    """ Return an embeddable class identified by given app and model names """
    try:
        module = import_module(app_name + '.embed')
        embed = getattr(module, model_name + 'Embed')()
    except Exception as e:
        if settings.DEBUG:
            raise e
        raise Http404
    return embed


def get_form_initial(form_class):
    """ Return initial dict for given form class """
    result = {}
    form = form_class()
    for field in form:
        result[field.name] = field.value()
    return result


def get_params(form_class, get_dict):
    """ Return valid form parameters or raise 404 """
    params = {}
    initial = get_form_initial(form_class)
    form = form_class(initial)
    
    for name, value in get_dict.items():
        field = form.fields.get(name)
        if field and value:
            form.data[name] = value

    if not form.is_valid():
        raise Http404
    
    for n, v in form.cleaned_data.items():
        params[n] = v
        
    return params


def common_view(app, model, pk):
    """ Validate passed arguments and get an embed instance and a model object """
    model_ = get_appmodel(app, model)
    embed = get_embeddable(app, model_.__name__)
    obj = get_object_or_404(model_, pk=pk)
    return embed, obj


def get_encoded_params(params):
    """ Generate the GET string for the URL """
    return '?' + urlencode(params) if params else ''
