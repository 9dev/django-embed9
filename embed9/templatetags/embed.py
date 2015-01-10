from django.template import Library, loader, Context
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

from random import randrange

from embed9.utils import get_embeddable, get_encoded_params, get_form_initial

register = Library()

def widget(obj, *args, **kwargs):
    """ Render embed code template """
    model_name = obj.__class__.__name__
    model_name_lower = model_name.lower()
    app_name = obj._meta.app_label
    widget_id = randrange(10,99999)
    
    embed = get_embeddable(app_name, model_name)
    template_name = embed.get_code_template()
    t = loader.get_template(template_name)
    form_class = embed.get_form_class()
    params = get_form_initial(form_class)
    kwparams = kwargs.pop('params', {})
    
    for n,v in kwargs.items():
        params[n] = v
        
    for n,v in kwparams.items():
        params[n] = v
    
    return t.render(Context({
        model_name_lower : obj,
        'widget_id' : widget_id,
        'domain' : Site.objects.get_current().domain,
        'loader_url' : mark_safe(reverse('embed9:loader', kwargs={'app': app_name, 'model': model_name_lower, 'pk': obj.pk, 'widget_id': widget_id}) + get_encoded_params(params)),
        'params' : params,
    }))

@register.simple_tag
def widget_preview(obj, *args, **kwargs):    
    return widget(obj, *args, **kwargs)

@register.simple_tag
def widget_code(obj, *args, **kwargs):
    return escape(widget(obj, *args, **kwargs))
