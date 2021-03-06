"""
Django settings for dragon project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, warnings
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

envSecretKey = 'DRAGON_SECRET_KEY'
envDebug = 'DRAGON_DEBUG'
envHosts = 'DRAGON_ALLOWED_HOSTS'
envConfig = 'DRAGON_RUN_CONFIG'

SECRET_KEY = os.environ.get(envSecretKey)

if SECRET_KEY is None:
    os.environ[envSecretKey] = get_random_secret_key()
    warnings.warn("No secret key found, generating one")
    SECRET_KEY = os.environ[envSecretKey]

# SECURITY WARNING: don't run with debug turned on in production!
debug_var = os.environ.get(envDebug)

if debug_var is None:
    os.environ[envDebug] = "True"
    debug_var = "True"

DEBUG = debug_var == "True"

if DEBUG:
    warnings.warn("Using debug mode")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'library.apps.LibraryConfig',
    'members.apps.MembersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guardian',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dragon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dragon/templates')],
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

WSGI_APPLICATION = 'dragon.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

use_mysql = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dragon',
        'USER': 'dungeonmaster',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
} if use_mysql else {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dragon.sqlite3'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/dragon/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dragon/static')
]
