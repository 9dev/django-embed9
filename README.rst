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

Usage
=====

For every model you want to make embeddable, create a class extending ``embed9.main.Embeddable`` in ``embed.py`` file inside your app folder. Class name has to be a concatenation of your model name and a word ``Embed``.

For example model ``Image``::

    # embed.py
    from embed9.main import Embeddable

    class ImageEmbed(Embeddable):
        pass

...

``django-embed9`` provides a simple demo with example usage. To install it from the console, navigate to ``embed9/demo`` directory and execute ``make install`` command. To run it, type ``make``.

Customization
=============

...

Notes
=====

- ...

