"""
Django settings for SistemaINADE2 project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9%%ck*j+2bh9m*a5g&dv3ptj6%f=g33&7$s)k-jpjdx31z6#y^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ID proyect: lucresys
ALLOWED_HOSTS = ['lucresys.appspot.com','192.168.x.x', 'localhost', '127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'facturacion'
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

ROOT_URLCONF = 'SistemaINADE2.urls'

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
                'accounts.context_processors.organization_logo',  # Añade aquí el context processor
                'accounts.context_processors.notificaciones_no_leidas',
            ],
        },
    },
]

WSGI_APPLICATION = 'SistemaINADE2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'accounts.CustomUser'


# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'accounts.backends.CustomUserBackend',# Este es el backend de autenticación predeterminado
# ]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'
DATE_INPUT_FORMATS = ['%d-%m-%Y']

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Ruta adicional para encontrar archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Configuración para la recopilación de archivos estáticos en producción
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Añade estas líneas para manejar archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL='accounts.Usuario'

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.me.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Tu nueva dirección de correo de iCloud
EMAIL_HOST_USER = 'proyectos.inade@icloud.com'
# La contraseña de la aplicación generada
EMAIL_HOST_PASSWORD = 'nvol-qhms-gvbt-adkj'#nvol-qhms-gvbt-adkj
DEFAULT_FROM_EMAIL = 'proyectos.inade@icloud.com'
SUPPORT_EMAIL = 'proyectos.inade@icloud.com'

# settings.py
LOGIN_URL = 'login/'  # Cambia esto a la URL correcta de tu página de inicio de sesión

# API FACTURAMA
USERNAME = "AranzaInade"
PASSWORD = "Puebla4990"
SANDBOX_URL = "https://apisandbox.facturama.mx"

