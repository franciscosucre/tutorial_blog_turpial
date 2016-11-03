"""
Django settings for BlogApp project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0h-h#j7ve0&eiiuq-u@5&x9rwth)lb^g)fopwl(!idig6d#x10'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

'''
INSTALLED_APPS: Define la lista de modulos que formaran parte de la aplicacion, por cada modulo en esta
lista, se importaran los modelos y demas
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commons',
    'writer',
    'writer.article',
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
'''
ROOT_URLCONF: Define el archivo en el cual se definiran los URLs
'''
ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'commons/templates'),
                 os.path.join(BASE_DIR, 'writer/templates'),
                 os.path.join(BASE_DIR, 'writer/articles/templates')],
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



WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
'''
STATIC_URL: Define la direccion de la carpeta statiic
'''
STATIC_URL = '/commons/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "commons/static")
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'BlogApp.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file','console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
# Direccion a la cual redirigira la pagina cuando haga falta iniciar sesion
LOGIN_URL='/login'
# Direccion a la cual redirigira la pagina cuando se inicie sesion
LOGIN_REDIRECT_URL='/home'
# Direccion a la cual redirigira la pagina cuando se cierre sesion
LOGOUT_REDIRECT_URL='/index'
# Directorio donde encontrar FIXTURES que son archivos .xml o .json con data inicial

# Para cargar esta data se debe correr:
#    python3 manage.py loaddata <nombredelarchivo>

# Esto se puede hacer rapidamente con una run configuration de eclipse en la cual definamos
# en la seccion de la seccion de arguments lo siguiente
#    loaddata <nombredelarchivo>
FIXTURE_DIRS=[os.path.join(BASE_DIR, 'commons/')]

AUTH_USER_MODEL = 'writer.Writer'