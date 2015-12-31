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
SECRET_KEY = 'l8rh*#06^65=+n7x=(4^)m^n3kfnx-g!zw2%aazzjt%0#u9u_z'

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
	'denuncias',
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


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
	# 'default': {
	# 	'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	# 	'NAME': 'dam35dl4hmr6dl',                      # Or path to database file if using sqlite3.
	# 	'USER': 'qdimcviawfcrqt',
	# 	'PASSWORD': 'B71NlKZN91_LDvL2aHMRZOo8vp',
	# 	'HOST': 'ec2-54-204-8-138.compute-1.amazonaws.com', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	# 	'PORT': '5432',                      # Set to empty string for default.
	# }

	# 'default': {
	# 	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	# 	#'ENGINE': 'django.db.backends.postgresql',
	# 	'NAME': 'defensoria',                   
	# 	'USER': 'postgres',
	# 	'PASSWORD': 'mcli28',
	# 	'HOST': '',
	# 	'PORT': '',
	# }
}
#-----------------------------heroku config--------------------------
# DATABASES['default'] =  dj_database_url.config(default=os.getenv('DATABASE_URL'))
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
# DATABASES['default']['HOST'] = 'ec2-54-204-8-138.compute-1.amazonaws.com'
# DATABASES['default']['NAME'] = 'dam35dl4hmr6dl'
# DATABASES['default']['USER'] = 'qdimcviawfcrqt'
# DATABASES['default']['PASSWORD'] = 'B71NlKZN91_LDvL2aHMRZOo8vp'
# DATABASES['default']['PORT'] = '5432'

#------------------------local config------------------------------
# DATABASES['default'] =  dj_database_url.config(default=os.getenv('DATABASE_URL'))
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
# DATABASES['default']['NAME'] = 'defensoria'
# DATABASES['default']['USER'] = 'postgres'
# DATABASES['default']['PASSWORD'] = 'mcli28'



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

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)
