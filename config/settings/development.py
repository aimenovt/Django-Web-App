"""
Development settings for config project.
"""
from .base import *
from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# Development-specific settings
if DEBUG:
    INSTALLED_APPS += ['django_extensions'] if 'django_extensions' in INSTALLED_APPS else []
