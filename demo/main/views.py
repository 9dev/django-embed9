from django.views.generic import DetailView, ListView
from django.http import HttpResponse

from main.models import Image, Text


def index(request):
    return HttpResponse('Go to /texts or /images')


class ImageDetailView(DetailView):
    model = Image


class ImageListView(ListView):
    model = Image


class TextDetailView(DetailView):
    model = Text


class TextListView(ListView):
    model = Text
