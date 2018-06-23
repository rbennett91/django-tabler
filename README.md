# django-tabler

This project transforms the [Tabler](https://github.com/tabler/tabler) dashboard
into a Django package. It provides an extensible base template, error page templates,
and the necessary static assets. django-tabler is based on the latest Tabler
release [v0.0.32](https://github.com/tabler/tabler/releases/tag/v0.0.32).

# Installation
django-tabler was built with Python 3.6 and Django 1.11. Other versions should be compatible, but they haven't been tested. To install:
* `pip install git+https://github.com/rbennett91/django-tabler`
* Add `django_tabler` to your `INSTALLED_APPS`

# Usage
Once installed, templates inside your application can extend django-tabler's
[base template](https://github.com/rbennett91/django-tabler/blob/master/django_tabler/templates/django_tabler/base.html). A quick example:
```
{% extends "django_tabler/base.html" %}

{% block extra_css %}
    {# add your custom css here #}
{% endblock extra_css %}

{% block content %}
    <h1>This is a Heading</h1>
    <p>This is a paragraph</p>
    <p>{{ some_context_variable }}</p>
{% endblock content %}

{% block extra_js %}
<script>
    {# add your custom javascript here #}
</script
{% endblock extra_js %}
```
Need some inspiration? Check out the [templates](https://github.com/tabler/tabler/tree/dev/dist)
provided by the original project.


### Missing a title in the browser window?
django-tabler's base template adds your site's name to the browser's titlebar using Django's
[Sites](https://docs.djangoproject.com/en/1.11/ref/contrib/sites/) framework.
Follow these steps for setup:
* Add a `SITE_ID` value to your application's settings file
* Add `'django.contrib.sites'` to `INSTALLED_APPS`
* Add `'django.contrib.sites.middleware.CurrentSiteMiddleware'` to `MIDDLE_WARE`
* Run `python manage.py migrate` if necessary
* Inside your application's `django_site` database table, update the record that cooresponds to the `SITE_ID`
value with an appropriate name and domain. A custom migration might be helpful.


### Missing a favicon?
To load a favicon, create an `img/` folder inside your application's `static` directory.
Place `favicon.ico` inside, and the icon will be loaded by the base template.


### Custom error views
django-tabler overrides Django's [default error views](https://docs.djangoproject.com/en/1.11/topics/http/views/#customizing-error-views)
by rendering a custom error template. Your application can access these by
adding the following to your applications' `urls.py` file:
```
handler400 = 'django_tabler.views.error400'
handler403 = 'django_tabler.views.error403'
handler404 = 'django_tabler.views.error404'
handler500 = 'django_tabler.views.error500'
```
