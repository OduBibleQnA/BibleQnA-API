from .base import *
from dotenv import load_dotenv

load_dotenv()


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