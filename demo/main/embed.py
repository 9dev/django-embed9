from embed9.main import Embeddable

from main.forms import ImageWidgetForm


class ImageEmbed(Embeddable):
    widget_template = 'main/image_widget.html'
    form_class = ImageWidgetForm


class TextEmbed(Embeddable):
    pass
