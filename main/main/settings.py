"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8cp!a#zj+mv&^1^7g$d#93u5^t)ql9u5-%r#(8(8c47e=%pv_+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['cartermyers.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    # CREATED APPS:
    'account.apps.AccountConfig',
    'posts.apps.PostsConfig',
    'user_messages.apps.UserMessagesConfig',

    #thumbnails:
    'easy_thumbnails',

    # DEFAULT APPS:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8,},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

AUTH_USER_MODEL = 'account.User'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Canada/Saskatchewan'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

"""
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    "/static/",
]
"""

# Media files (for us, images uploaded by users)

MEDIA_ROOT = os.path.join(BASE_DIR, "static/media")

# INVESTIGATE THIS MORE
MEDIA_URL = '/static/media/'
# MEDIA_URL = 'http://cartermyers.pythonanywhere.com/media'

LOGIN_URL = 'index'  #since user's login at the index

# Email info (to be used later)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'donotreply.ursell@gmail.com' #name of email username
EMAIL_HOST_PASSWORD = 'deadline'
EMAIL_USE_TLS = True
"""
EMAIL_HOST = 'smtp.sendgrid.net' #name of mail server
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ursell' #name of email username
EMAIL_HOST_PASSWORD = 'nicetry'
EMAIL_USE_TLS = True
"""
