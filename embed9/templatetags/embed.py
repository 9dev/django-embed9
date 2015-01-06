from django.template import Library, loader, Context
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.html import escape

from random import randrange

from embed9.utils import get_embeddable

register = Library()

def widget(obj):
    """ Render embed code template """
    model_name = obj.__class__.__name__
    model_name_lower = model_name.lower()
    app_name = obj._meta.app_label
    widget_id = randrange(10,99999)
    
    embed = get_embeddable(app_name, model_name)
    template_name = embed.get_code_template()
    t = loader.get_template(template_name)
    
    return t.render(Context({
        model_name_lower : obj,
        'widget_id' : widget_id,
        'domain' : Site.objects.get_current().domain,
        'loader_url' : reverse('embed9:loader', kwargs={'app': app_name, 'model': model_name_lower, 'pk': obj.pk, 'widget_id': widget_id}),
    }))

@register.simple_tag
def widget_preview(obj):
    return widget(obj)

@register.simple_tag
def widget_code(obj):
    return escape(widget(obj))
