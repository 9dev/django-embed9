from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import cache_page
from django.utils.safestring import mark_safe
from django.conf import settings

from embed9.utils import get_params, common_view, get_encoded_params

WIDGET_CACHE_TIME = getattr(settings, 'WIDGET_CACHE_TIME', 60*60)


@cache_page(WIDGET_CACHE_TIME)
@xframe_options_exempt
def widget(request, app, model, pk):
    """ Renders an iframe with the widget. """
    embed, obj = common_view(app, model, pk)
    params = get_params(embed.get_form_class(), request.GET)
    template = embed.get_widget_template()
    
    return render_to_response(template, {
        model: obj,
        'params': params,
    }, RequestContext(request))


@cache_page(WIDGET_CACHE_TIME)
@xframe_options_exempt
def loader(request, app, model, pk):
    """ Renders JavaScript loader of the widget. """
    embed, obj = common_view(app, model, pk)
    params = get_params(embed.get_form_class(), request.GET)
    template = embed.get_loader_template()

    return render_to_response(template, {
        model: obj,
        'widget_name': 'widget_' + model + str(pk),
        'domain': Site.objects.get_current().domain,
        'iframe_url': mark_safe(reverse('embed9:widget', kwargs={'app': app, 'model': model, 'pk': pk}) + get_encoded_params(params)),
        'params': params,
    }, RequestContext(request))


def preview(request, app, model, pk):
    """ Handles previewing and adjusting the widget. """
    embed, obj = common_view(app, model, pk)
    template = embed.get_form_template()
    show_preview = True
    params = {}
    
    if request.method == 'POST':
        form = embed.get_form_class()(request.POST)
        if form.is_valid():
            for n, v in form.cleaned_data.items():
                params[n] = v
        else:
            show_preview = False
    else:
        form = embed.get_form_class()()
    
    return render_to_response(template, {
        'obj': obj,
        'form': form,
        'params': params,
        'show_preview': show_preview,
    }, RequestContext(request))
