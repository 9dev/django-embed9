from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.clickjacking import xframe_options_exempt

from embed9.utils import get_appmodel, get_embeddable

@xframe_options_exempt
def widget(request, app, model, pk):
    model_ = get_appmodel(app, model)
    embed = get_embeddable(app, model_.__name__)
    obj = get_object_or_404(model_, pk=pk)    
    template = embed.get_widget_template()
    
    return render_to_response(template, {
        model : obj,
    }, RequestContext(request))
