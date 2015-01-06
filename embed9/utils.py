from django.http import Http404
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_app, get_models

from importlib import import_module

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
    except Exception:
        raise Http404
    return embed
    