from django import forms

from main.models import Image


class ImageWidgetForm(forms.ModelForm):
    width = forms.IntegerField(max_value=500, min_value=75, initial=200, help_text='Width of the widget in pixels')
    color = forms.RegexField('^[A-Fa-f0-9]{6}$', initial='543674', help_text='Background color for the widget in HEX (without the "#")')

    class Meta:
        model = Image
        fields = ['awesome']
