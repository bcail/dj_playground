import os
from pathlib import Path

DEBUG = True
SECRET_KEY = '123456789'

PROJECT_ROOT = Path(__file__).resolve().parent

ROOT_URLCONF = 'playground.urls'

MIDDLEWARE = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dj_playground.db',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/playground_static'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]
MEDIA_ROOT = 'media'
MEDIA_URL = 'media/'

INSTALLED_APPS = [
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.auth',
        'django.contrib.messages',
        'django.contrib.admin',
        'django.contrib.staticfiles',
        'compressor',
        'polls.apps.PollsConfig',
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

TIME_ZONE = 'America/New_York'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = ''

from django.urls import get_script_prefix

class LazyScriptNamePrefixedUrl(str):
    """
    Lazy URL with ``SCRIPT_NAME`` WSGI param as path prefix.

    .. code-block :: python

        settings.STATIC_URL = LazyScriptNamePrefixedUrl('/static/')

        # HTTP request to '/some/page/' without SCRIPT_NAME
        str(settings.STATIC_URL) == '/static/'

        # HTTP request to '/app/prefix/some/page/` with SCRIPT_NAME = '/app/prefix/'
        str(settings.STATIC_URL) == '/app/prefix/static/'

        # HTTP request to '/another/prefix/some/page/` with SCRIPT_NAME = '/another/prefix/'
        str(settings.STATIC_URL) == '/another/prefix/static/'

    The implementation is incomplete, all ``str`` methods must be overridden
    in order to work correctly with the rest of Django core.
    """

    def __str__(self):
        return get_script_prefix() + self[1:] if self.startswith("/") else self

    def __unicode__(self):
        return str(self)

    def __hash__(self):
        return str.__hash__(str(self))

    def lstrip(self, *args, **kwargs):
        """
        Override ``.lstrip()`` method to make it work with ``{% static %}``.
        """
        return str(self).lstrip(*args, **kwargs)

    def split(self, *args, **kwargs):
        """
        Override ``.split()`` method to make it work with ``{% static %}``.
        """
        return str(self).split(*args, **kwargs)

    def replace(self, *args, **kwargs):
        """Override ``.replace()`` to make it work with ``{% static %}``.

        In ``django.core.files.storage``, ``FileSystemStorage.url()`` passes
        this object to ``urllib.parse.urljoin``.

        In ``urrlib.parse``, the function that calls ``replace()`` is
        ``_remove_unsafe_bytes_from_url()``.

        """
        return str(self).replace(*args, **kwargs)


# COMPRESS_URL = LazyScriptNamePrefixedUrl('/static/')
COMPRESS_URL = '/static/'
