# -*- coding: utf-8 -*-
# Django settings for linky project
from os.path import join, dirname, abspath

PROJECT_ROOT = abspath(dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (    
    #('Konstantin Volia', 'kostyg@gmail.com'),
    #('Nata Obvintseva', 'nata@natkitten.name'),
    ('Alexander Schapov', 'alexanderad@gmail.com'),    
)

MANAGERS = ADMINS


TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = False

# serve media in old-school style :)
MEDIA_ROOT = join(PROJECT_ROOT, 'static/')
MEDIA_URL = '/static'

SECRET_KEY = ')v=tn^zxz9@be5qd69a2f&2!h+$!2^+wgi*y573j^dlfu4^+be'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'linky.urls'

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates/')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',    
    
    'south',    
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

APPEND_SLASH = False

try:
    from local_settings import *
except ImportError:
    pass