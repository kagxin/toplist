"""
Django settings for djangotemplate project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from rest_framework import ISO_8601
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(''.join([BASE_DIR, os.path.sep, '..']))
STATIC_ROOT = os.path.join(ROOT_DIR, 'apps/static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!^v$5+4ji33%+rx#0o$y#f!kfu^8hze2kmkmrl7v3bv*wa4xrr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]



# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

THIRD_APPS = [
    'rest_framework',
    # 'django_filters',
    'corsheaders',
]

LOCAL_APPS = [
    'apps.account',
    'apps.demo'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'
TIME_FORMAT = 'H:i:s'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'apps.utils.exception_handler.exception_handler',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DATE_FORMAT': '%Y-%m-%d',
    'DATE_INPUT_FORMATS': (
        '%Y-%m-%d', ISO_8601
    ),
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATETIME_INPUT_FORMATS': (
        '%Y-%m-%d %H:%M:%S', ISO_8601
    )
}
## JWT
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_PAYLOAD_HANDLER':
    'apps.utils.jwt.jwt_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'apps.utils.jwt.jwt_response_payload_handler',
    # how long the original token is valid for
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

## cors
CORS_ORIGIN_ALLOW_ALL = True


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


# ==================
# = Configurations from other file
# ==================
site_env = os.getenv('SITE_TYPE', "local")

if site_env == 'production':
    from .production import *  # NOQA
elif site_env == 'staging':
    from .staging import *  # NOQA
elif site_env == 'local':
    from .local import *  # NOQA
else:
    raise Exception("Env[SITE_TYPE] error!")

"""
# if use mongodb
from mongoengine import connect
connect(
    db=MONGODB_DATABASES['default']['name'],
    username=MONGODB_DATABASES['default']['username'],
    password=MONGODB_DATABASES['default']['password'],
    host=MONGODB_DATABASES['default']['host'].split(":")[0],
    port=int(MONGODB_DATABASES['default']['host'].split(":")[1]),
)
"""

