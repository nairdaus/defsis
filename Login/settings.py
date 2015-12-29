"""
Django settings for Login project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import psycopg2
import urlparse
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0u!s^akobl=$l+9ige6b%y*nc1mv&w89743p6h@-s35^o$mdul'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'usuarios',
]

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Login.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, '../Login/static'))
#import os
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#PROJECT_DIR = os.path.join(PROJECT_ROOT,'../Login')
#STATIC_ROOT = os.path.join(PROJECT_ROOT,'staticfiles/')
#STATIC_URL = '/static/'
#STATICFILES_DIRS = (
#    os.path.join(PROJECT_DIR,'static/'),
#)
#<<<<<<< HEAD
#=======
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#>>>>>>> 956f1574bc8c5b6ffc41e445aa787ec4e76bbab8
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Login.wsgi.application'



urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
	database=url.path[1:],
	user=url.username,
	password=url.password,
	host=url.hostname,
	port=url.port
)

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
	# 'default': {
	# 	'ENGINE': 'django.db.backends.sqlite3',
	# 	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	# }
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'd6dfbfbh614ta',                      # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': 'dxkwrlsrgphyyr',
		'PASSWORD': 'V_sGy4sopdB86efFrozkykMiSq',
		'HOST': 'ec2-107-22-170-249.compute-1.amazonaws.com', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': '5432',                      # Set to empty string for default.
	}
}
DATABASES['default'] =  dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



