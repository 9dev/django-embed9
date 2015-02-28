from django.db import models
from django.core.urlresolvers import reverse


class Text(models.Model):
    text = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('main:text_detail', kwargs={'pk':str(self.id)})


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', blank=True, null=True)
    awesome = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('main:image_detail', kwargs={'pk':str(self.id)})
