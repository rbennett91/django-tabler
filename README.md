# django-tabler

This project transforms the [Tabler](https://github.com/tabler/tabler) dashboard
into a Django package. It provides extensible base templates + static files.
It tracks the latest Tabler release [v0.0.32](https://github.com/tabler/tabler/releases/tag/v0.0.32).

# Installation
* pip install ...

### Configure Django settings
* Add `django-tabler` to your `INSTALLED_APPS`

##### Missing the site title in browser tab?
Install and add settings for the Django Sites framework:
* Add `SITE_ID` to Django settings
* Add `'django.contrib.sites'` to `INSTALLED_APPS`
* Add `'django.contrib.sites.middleware.CurrentSiteMiddleware'` to `MIDDLE_WARE`
* Either update the `django-site` table with appropriate name and domain, or create a custom migration
  to handle this.
