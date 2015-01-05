from django.views.generic import DetailView, ListView

from main.models import Image, Text

class ImageDetailView(DetailView):
	model = Image

class ImageListView(ListView):
	model = Image

class TextDetailView(DetailView):
	model = Text

class TextListView(ListView):
	model = Text
