from __future__ import absolute_import, unicode_literals
import os
from .base import *
import dj_database_url

env = os.environ.copy()
SECRET_KEY = '2d@rek2b(=n(q-h3)tho+kz19p+z@+-d4sd4pjs-zpu3in*d6v'

DEBUG = False
DATABASES['default'] =  dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['localhost', '127.0.0.1','*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
