from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url
import os
DEBUG = False

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
print("sdsd")
env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']
try:
    from .local import *
except ImportError:
    pass
