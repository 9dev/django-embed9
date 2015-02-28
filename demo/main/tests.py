from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from main.models import Image


class ViewTestCase(TestCase):
    def setUp(self):
        self.image = Image(image=SimpleUploadedFile(name='x.jpg', content='x', content_type='image/jpeg'), title='Example')
        self.image.save()
        self.params = {
            'app': 'main',
            'model': 'image',
            'pk': self.image.pk
        }

    def get_page(self, url):
        """ Ensures given url returns HTTP 200. """
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def test_get_widget_iframe(self):
        """ User requests an iframe with the widget and gets an expected result """
        self.get_page(reverse('embed9:widget', kwargs=self.params))

    def test_get_widget_loader(self):
        """ User requests a JavaScript loader of the widget and gets an expected result """
        self.get_page(reverse('embed9:loader', kwargs=self.params))

    def test_get_widget_preview(self):
        """ User requests a widget preview and gets an expected result """
        self.get_page(reverse('embed9:preview', kwargs=self.params))
