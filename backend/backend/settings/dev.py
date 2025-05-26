from .base import *

SECRET_KEY = 'django-insecure-1-*@dwqufi3nmavnbtw8l7fuows%2mi__0-cmirm89!q77e2nw'

DEBUG=True

ALLOWED_HOSTS = ['localhost:8000', '127.0.0.1:8000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#   'http://localhost:8000',
# )