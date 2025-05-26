from .base import *
from os import environ

SECRET_KEY=environ.get('SECRET_KEY', None)
DEBUG=False

ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
  'http://localhost:8000',
)