*************
django-embed9
*************

``django-embed9`` allows you to create widgets from your model objects and embed them on external websites.

Requirements
============

- `django.contrib.sites <https://docs.djangoproject.com/en/1.7/ref/contrib/sites/>`_

Installation
============

- Install via pip::

    pip install django-embed9

- Add ``embed9`` to your ``INSTALLED_APPS``

- Add url pattern to your urls.py::

    url(r'^embed/', include('embed9.urls', namespace='embed9'))

- Create a site in your database and set the SITE_ID setting

- (Optional) Add the following line to your ``robots.txt`` file::

    Disallow: /embed/widget/

Usage
=====

For every model that you want to make embeddable, create a class extending ``embed9.main.Embeddable`` in ``embed.py`` file inside your app folder. Class name has to consists of your model name and a word ``Embed``.

For example model ``Image``::

    # embed.py
    from embed9.main import Embeddable

    class ImageEmbed(Embeddable):
        pass

In order to provide your own template of the widget, add ``widget_template`` to the class (or define ``get_widget_template()`` method)::

    class ImageEmbed(Embeddable):
        widget_template = 'myapp/mywidget.html'

Inside the template you can access a context variable named after your model (but in lower case). In this example it would be ``{{ image }}``.

By default, defined widget template will render as an ``iframe`` on external websites. 

To display a widget preview or raw embed code for an object in the template use the following::

	{% load embed %}
	
	{% widget_code myobject %}
	{% widget_preview myobject %}
	
To display an URL to the preview/customization page you can use templatetag ``widget_preview_url``::

	{% widget_preview_url myobject %}

``django-embed9`` provides a simple demo with example usage. To install it from the console, navigate to ``embed9/demo`` directory and execute ``make install`` command. To run it, type ``make``.

Customization
=============

Templates
---------

You may want to change the default templates for embed code or for the JavaScript loader. To do that, specify these templates in your ``Embeddable`` class::

    class ImageEmbed(Embeddable):
        code_template = 'myapp/mycode.html'
        loader_template = 'myapp/myloader.js'

Again, if you need to provide these names dynamically, define ``get_code_template()`` and ``get_loader_template()`` methods.

Remember to use ``{{ widget_name }}`` as shown in the default templates. It is required if you want to allow many widgets on a single page.

Of course, sometimes JavaScript loader is not necessary. If this is the case, you will just need to create a code template similar to::

	<iframe src="{{ domain }}{{ iframe_url }}"></iframe>

Parameters
----------

You may want to add some custom parameters such as widget size or color and allow your users to adjust them.

To define such parameters, create a form class and tell ``django-embed9`` where it should look for it::

	# embed.py
	class ImageEmbed(Embeddable):
		form_class = MyAwesomeForm
        form_template = 'myapp/myform.html'
        
Example form::

	# forms.py
	class MyAwesomeForm(forms.Form):
		size = forms.IntegerField(max_value=500, min_value=100, initial=200)
		color = forms.CharField(max_length=6)
	
Now all these parameters are going to be passed to the templates as a dictionary named ``{{ params }}``::

	<p>Size of this widget should be: {{ params.size }}</p>

Widget customization is available on the preview page. To display a link to it, write::

	{% load embed %}
	{% widget_preview_url myobject %}

You can also pass the parameters directly to templatetags::

	{% load embed %}
	{% widget_code myobject size=1000 %}

Caching
=======

By default, widgets (iframes and javascript loaders) are cached for an hour. In order to adjust this behaviour, set the ``WIDGET_CACHE_TIME`` setting::

    WIDGET_CACHE_TIME = 24 * 60 * 60

In progress
===========

- oEmbed API.

Notes
=========

- Tested with Python 3.4 and Django 1.7.4.
