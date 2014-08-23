# flake8: noqa

from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fifa',  # Database
        'USER': '',  # Blank normally
        'PASSWORD': '',  # Blank normally
        'HOST': 'localhost',  # localhost
        'PORT': '',  # Blank normally
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}

CORS_ORIGIN_ALLOW_ALL = True
