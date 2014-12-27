"""
Django settings for GreekPeek project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-=0(gm#_z#1_p)x)cow_jm+*di)0#9&pn97wz$lk3*c4%a)u72'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'home',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'chapters',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'GreekPeek.urls'

WSGI_APPLICATION = 'GreekPeek.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

chapter_names = ['Alpha Delta Phi',
 'Alpha Epsilon Pi',
 'Alpha Sigma Phi',
 'Alpha Tau Omega',
 'Chi Psi',
 'Delta Chi',
 'Delta Tau Delta',
 'Delta Upsilon',
 'Kappa Alpha Order',
 'Kappa Sigma',
 'Lambda Chi Alpha',
 'Phi Delta Theta',
 'Phi Gamma Delta',
 'Phi Kappa Psi',
 'Phi Kappa Sigma',
 'Phi Kappa Tau',
 'Phi Kappa Theta',
 'Pi Kappa Alpha',
 'Pi Kappa Phi',
 'Psi Upsilon',
 'Sigma Alpha Epsilon',
 'Sigma Beta Rho',
 'Sigma Chi',
 'Sigma Nu',
 'Sigma Phi Epsilon',
 'Tau Kappa Epsilon',
 'Theta Chi',
 'Theta Delta Chi',
 'Theta Xi',
 'Zeta Beta Tau',
 'Zeta Psi']

