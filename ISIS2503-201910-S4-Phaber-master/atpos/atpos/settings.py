"""
Django settings for atpos project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')qx6yr(#9yhxy2x=ual#a&nem$=45w4h3we4p($1tm!o=y$c#n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'cajas.apps.CajasConfig',
    'productos.apps.ProductosConfig',
    'ventas.apps.VentasConfig',
    'facturas.apps.FacturasConfig',
    'clientes.apps.ClientesConfig',
    'reportes.apps.ReportesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'social_django',
    #'rest_framework_jwt',
    #'rest_framework_auth0',
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

ROOT_URLCONF = 'atpos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'atpos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'atpos_db',
        'USER': 'admin_atpos',
        'PASSWORD': 'atpos2019',
        'HOST': '54.208.57.169',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

#REST_FRAMEWORK = {
#    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#    'PAGE_SIZE': 10,
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework_auth0.authentication.Auth0JSONWebTokenAuthentication',
#    ),
#}
# AUTH0 = {
#   'CLIENTS': {
#       'default': {
#           'AUTH0_CLIENT_ID': 'c1EK1CuheE2t8Ag39rhQFTWDUN7sLbnI',  #make sure it's the same string that aud attribute in your payload provides
#           'AUTH0_CLIENT_SECRET': '<aZPog2h3dd2GpgOfZukQlClWKlGVpRjlE9fC1G0VGw4sVDMPBuWNFQsraqTPCUNA>',
#           'CLIENT_SECRET_BASE64_ENCODED': True,  # default to True, if you're Auth0 user since December, maybe you should set it to False
#       }
#   },
#   'AUTH0_ALGORITHM': 'HS256',  # default used in Auth0 apps
#   'JWT_AUTH_HEADER_PREFIX': 'JWT',  # default prefix used by djangorestframework_jwt
#   'AUTHORIZATION_EXTENSION': False,  # default to False
#   'USERNAME_FIELD': 'sub',  # default username field in auth0 token scope to use as token user
# }

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

REPORTES_ROOT = os.path.join(BASE_DIR, 'reportes_generados/')

LOGIN_URL = "api/productos/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "https://atpos-phaber.auth0.com/v2/logout?returnTo=http%3A%2F%2F18.232.77.97:8080"
SOCIAL_AUTH_TRAILING_SLASH = False  # Remove end slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'atpos-phaber.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'c1EK1CuheE2t8Ag39rhQFTWDUN7sLbnI'
SOCIAL_AUTH_AUTH0_SECRET = 'aZPog2h3dd2GpgOfZukQlClWKlGVpRjlE9fC1G0VGw4sVDMPBuWNFQsraqTPCUNA'
SOCIAL_AUTH_AUTH0_SCOPE = ['openid','profile']
AUTHENTICATION_BACKENDS = {'productos.auth0backend.Auth0','django.contrib.auth.backends.ModelBackend',}