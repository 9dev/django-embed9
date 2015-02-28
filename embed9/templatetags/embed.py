from django.template import Library, loader, Context
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

from embed9.utils import get_embeddable, get_encoded_params, get_form_initial

register = Library()


def widget(obj, *args, **kwargs):
    """ Render embed code template """
    model_name = obj.__class__.__name__
    model_name_lower = model_name.lower()
    app_name = obj._meta.app_label
    
    embed = get_embeddable(app_name, model_name)
    template_name = embed.get_code_template()
    t = loader.get_template(template_name)
    form_class = embed.get_form_class()
    params = get_form_initial(form_class)
    kwparams = kwargs.pop('params', {})
    
    for n, v in kwargs.items():
        params[n] = v
        
    for n, v in kwparams.items():
        params[n] = v
    encoded_params = get_encoded_params(params)
    url_kwargs = {'app': app_name, 'model': model_name_lower, 'pk': obj.pk}
    
    return t.render(Context({
        model_name_lower: obj,
        'widget_name': 'widget_' + model_name_lower + str(obj.pk),
        'domain': Site.objects.get_current().domain,
        'iframe_url': mark_safe(reverse('embed9:widget', kwargs=url_kwargs) + encoded_params),
        'loader_url': mark_safe(reverse('embed9:loader', kwargs=url_kwargs) + encoded_params),
        'params': params,
    }))


@register.simple_tag
def widget_preview(obj, *args, **kwargs):
    """ Render and return widget preview """  
    return widget(obj, *args, **kwargs)


@register.simple_tag
def widget_code(obj, *args, **kwargs):
    """ Render and return widget embed code """  
    return escape(widget(obj, *args, **kwargs))


@register.simple_tag
def widget_preview_url(obj):
    """ Render and return widget preview (and adjustment) url """  
    return reverse('embed9:preview', kwargs={'app': obj._meta.app_label, 'model': obj.__class__.__name__.lower(), 'pk': obj.pk})
