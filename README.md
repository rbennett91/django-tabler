# django-tabler

This project transforms the [Tabler](https://github.com/tabler/tabler) dashboard
into a Django package. It provides an extensible base template, error page templates,
and the necessary static assets. django-tabler is based on the latest Tabler
release [v0.0.32](https://github.com/tabler/tabler/releases/tag/v0.0.32).

# Installation
* `pip install git+https://github.com/rbennett91/django-tabler`
* Add `django_tabler` to your `INSTALLED_APPS`

# Usage
django-tabler's [base template](https://github.com/rbennett91/django-tabler/blob/master/django_tabler/templates/django_tabler/base.html) adds your site's name to the browser's titlebar using Django's
[Sites](https://docs.djangoproject.com/en/1.11/ref/contrib/sites/) framework.
Follow these steps for setup:
* Add a `SITE_ID` value to Django settings
* Add `'django.contrib.sites'` to `INSTALLED_APPS`
* Add `'django.contrib.sites.middleware.CurrentSiteMiddleware'` to `MIDDLE_WARE`
* Run `python manage.py migrate` if necessary
* Update the `django-site` database record that cooresponds to the `SITE_ID`
value with an appropriate name and domain. A custom migration might be helpful.


To load a favicon, create an `img/` folder inside your application's `static` directory.
Place `favicon.ico` inside, and the icon will be loaded by the base template.


Once installed, templates inside your application can extend django-tabler's
base template. A quick example:
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


django-tabler overrides Django's [default error views](https://docs.djangoproject.com/en/1.11/topics/http/views/#customizing-error-views)
by rendering a custom error template. Your application can access these by
adding the following to your applications' `urls.py` file:
```
handler400 = 'django_tabler.views.error400'
handler403 = 'django_tabler.views.error403'
handler404 = 'django_tabler.views.error404'
handler500 = 'django_tabler.views.error500'
```
