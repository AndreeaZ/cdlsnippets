import os

DATABASES = {
    'default': {
        'USER': 'cristian',
        'PASSWORD': '',
    }
}

INSTALLED_APPS = (
)


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../media')
MEDIA_URL = '/media/'

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(os.path.dirname(__file__), '../static')
