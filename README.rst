****************
django-embed9
****************

``django-embed9``

...

Requirements
============

- `django.contrib.flatpages <https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/>`_

- ...

Installation
============

- Install via pip::

    pip install django-embed9

- Add ``embed9`` to your ``INSTALLED_APPS``

- ...

- Add url pattern to your urls.py::

    url(r'^embed/', include('embed9.urls', namespace='embed9'))

Usage
=====

For every model you want to make embeddable, create a class extending ``embed9.main.Embeddable`` in ``embed.py`` file inside your app folder. Class name has to be a concatenation of your model name and a word ``Embed``.

For example model ``Image``::

    # embed.py
    from embed9.main import Embeddable

    class ImageEmbed(Embeddable):
        pass

In order to provide your own template of the widget, add ``widget_template`` to the class (or define ``get_widget_template()`` method)::

    class ImageEmbed(Embeddable):
        widget_template = 'myapp/mywidget.html'

Inside the template you can access a context variable named after your model (but in lower case). In this example it would be ``{{ image }}``.

By default, defined widget template will render as an `iframe` on external websites. 

``django-embed9`` provides a simple demo with example usage. To install it from the console, navigate to ``embed9/demo`` directory and execute ``make install`` command. To run it, type ``make``.

Customization
=============

...

Notes
=====

- ...

