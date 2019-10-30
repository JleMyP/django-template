import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__ + "/..")))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e@8eoyx0g=o%^wnj5#kk68$$yt)5%q6(o06o0m0zl6u^sp2toh'

DEBUG = True

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
