"""
Django settings for Roomate project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f&2jh2uw)mlq@!1g=#ok_1!rlxu95q_oal3&t%lpk6ux!yvebl'

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
    'captcha',
    'web',
	'bootstrap3',
    'dbbackup',  # django-dbbackup
    'dropbox',
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

ROOT_URLCONF = 'Roomate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Roomate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

DBBACKUP_STORAGE = 'dbbackup.storage.dropbox_storage'
DBBACKUP_TOKENS_FILEPATH = 'tokens'
DBBACKUP_DROPBOX_APP_KEY = 'tnbo7trh24hk32a'
DBBACKUP_DROPBOX_APP_SECRET = 'tuuljgl8x38hau4'
DBBACKUP_DROPBOX_DIRECTORY ='Roomate_Backups'

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#A continuacion esta la config. para usar una cuenta de correo
EMAIL_HOST = 'mail.gandi.net'
EMAIL_HOST_USER = 'no-reply@magnasis.com'
EMAIL_HOST_PASSWORD = 'magnarenove2016'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'no-reply@magnasis.com'
SERVER_EMAIL = 'no-reply@magnasis.com'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True

#Clave publica para usar en ReCaptcha
RECAPTCHA_PUBLIC_KEY = '6LccDhkTAAAAALWXFAQSivIXYLNsiHL8pUElVzGQ'
RECAPTCHA_PRIVATE_KEY = '6LccDhkTAAAAAKwu3cOcPn3sW0x_oIcaSKjTzq19'
NOCAPTCHA = True


import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # Formatos en los que se imprimen los logs. Es como dar formato en un printf de c. Sirven caracteres especiales como '\n', '\r', etc.
        # Con etiquetas como %(atributo)s se pueden añadir los atributos de un Record. Todos los record tienen los mismos atributos.
        # Aqui la lista: https://docs.python.org/2/library/logging.html#logrecord-attributes
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'dbVerbose':{
            'format' : "[%(asctime)s] %(levelname)s \n    duration: %(duration)s\n   operation: %(sql).10s\n   parameters: %(params)s\n",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        # Los Handlers determinan el proceso que sequira un Record. Basicamente dice a donde ira el Record, si a un fichero,
        # un socket, un correo electronico, etc. Solamente tratarán aqullos Records que tengan el mismo o superior nivel.
        # Ademas, los Handlers pueden aplicar uno o mas filtros para decidir si tratar un Record o no.
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
        'DBQfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'dbAccess.log',
            'formatter': 'dbVerbose'
        },
    },
    'loggers': {
        # Los Loggers son los objetos que crean y envian los records a los Handlers. Solo enviaran aquellos Redors que tengan
        # el mismo o superior nivel. En tu programa instancias uno de los Loggers a continuacion declarados. A traves de el
        # envias Records. Ej: loggerDejemplo = logging.getLogger('nombre')
        #                     loggerDejemplo.info("mensaje del record") <------ hay una funcion para lanzar Records de cada
        #                                                                       nivel.
        # Los niveles son: DEBUG, INFO, WARNING, ERROR y CRITICAL
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'INFO',
        },
        'web': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'database': {
            'handlers': ['DBQfile'],
            'level': 'INFO',
        },
        # Este Logger solo se usa si la variable DEBUG de settings.py esta en True. Enviara un Record por cada sentencia SQL.
        'django.db.backends': {
            'handlers': ['DBQfile'],
            'level': 'DEBUG'
       }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # Formatos en los que se imprimen los logs. Es como dar formato en un printf de c. Sirven caracteres especiales como '\n', '\r', etc.
        # Con etiquetas como %(atributo)s se pueden añadir los atributos de un Record. Todos los record tienen los mismos atributos.
        # Aqui la lista: https://docs.python.org/2/library/logging.html#logrecord-attributes
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'dbVerbose':{
            'format' : "[%(asctime)s] %(levelname)s \n    duration: %(duration)s\n   operation: %(sql).10s\n   parameters: %(params)s\n",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        # Los Handlers determinan el proceso que sequira un Record. Basicamente dice a donde ira el Record, si a un fichero,
        # un socket, un correo electronico, etc. Solamente tratarán aqullos Records que tengan el mismo o superior nivel.
        # Ademas, los Handlers pueden aplicar uno o mas filtros para decidir si tratar un Record o no.
        'null': {
            'class': 'logging.NullHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
        'DBQfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'dbAccess.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # Los Loggers son los objetos que crean y envian los records a los Handlers. Solo enviaran aquellos Redors que tengan
        # el mismo o superior nivel. En tu programa instancias uno de los Loggers a continuacion declarados. A traves de el
        # envias Records. Ej: loggerDejemplo = logging.getLogger('nombre')
        #                     loggerDejemplo.info("mensaje del record") <------ hay una funcion para lanzar Records de cada
        #                                                                       nivel.
        # Los niveles son: DEBUG, INFO, WARNING, ERROR y CRITICAL
        'django': {
            'handlers':['null'],
            'propagate': False,
            'level':'INFO',
        },
        'web': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'database': {
            'handlers': ['DBQfile'],
            'level': 'INFO',
        },
        # Este Logger se activara solo enviando un Record por cada sentencia SQL, y solo lo hara si la variable DEBUG de settings.py esta en True.
        # Todos los Records que envie seran de nivel DEBUG (el mas bajo) y por tanto, si se quiere poner en debug pero que no se hagan logs de las
        # instrucciones sql (pues tienen un gran coste), se puede cambiar el nivel del logger a uno superior (como INFO o ERROR).
#        'django.db.backends': {
#            'handlers': ['DBQfile'],
#            'level': 'INFO'
#       }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # Formatos en los que se imprimen los logs. Es como dar formato en un printf de c. Sirven caracteres especiales como '\n', '\r', etc.
        # Con etiquetas como %(atributo)s se pueden añadir los atributos de un Record. Todos los record tienen los mismos atributos.
        # Aqui la lista: https://docs.python.org/2/library/logging.html#logrecord-attributes
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s'
        },
        'dbVerbose':{
            'format' : "[%(asctime)s] %(levelname)s \n    duration: %(duration)s\n   operation: %(sql).10s\n   parameters: %(params)s\n",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        # Los Handlers determinan el proceso que sequira un Record. Basicamente dice a donde ira el Record, si a un fichero,
        # un socket, un correo electronico, etc. Solamente tratarán aqullos Records que tengan el mismo o superior nivel.
        # Ademas, los Handlers pueden aplicar uno o mas filtros para decidir si tratar un Record o no.
        'null': {
            'class': 'logging.NullHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'roomate.log',
            'formatter': 'simple'
        },
        'sessionfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'session.log',
            'formatter': 'verbose'
        },
        'DBQfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'dbAccess.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # Los Loggers son los objetos que crean y envian los records a los Handlers. Solo enviaran aquellos Redors que tengan
        # el mismo o superior nivel. En tu programa instancias uno de los Loggers a continuacion declarados. A traves de el
        # envias Records. Ej: loggerDejemplo = logging.getLogger('nombre')
        #                     loggerDejemplo.info("mensaje del record") <------ hay una funcion para lanzar Records de cada
        #                                                                       nivel.
        # Los niveles son: DEBUG, INFO, WARNING, ERROR y CRITICAL
        'django': {
            'handlers':['null'],
            'propagate': False,
            'level':'INFO',
        },
        'web': {
            'handlers': ['file','sessionfile'],
            'level': 'INFO',
        },
        'database': {
            'handlers': ['file','DBQfile'],
            'level': 'INFO',
        },
        # Este Logger se activara solo enviando un Record por cada sentencia SQL, y solo lo hara si la variable DEBUG de settings.py esta en True.
        # Todos los Records que envie seran de nivel DEBUG (el mas bajo) y por tanto, si se quiere poner en debug pero que no se hagan logs de las
        # instrucciones sql (pues tienen un gran coste), se puede cambiar el nivel del logger a uno superior (como INFO o ERROR).
#        'django.db.backends': {
#            'handlers': ['DBQfile'],
#            'level': 'INFO'
#       }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # Formatos en los que se imprimen los logs. Es como dar formato en un printf de c. Sirven caracteres especiales como '\n', '\r', etc.
        # Con etiquetas como %(atributo)s se pueden añadir los atributos de un Record. Todos los record tienen los mismos atributos.
        # Aqui la lista: https://docs.python.org/2/library/logging.html#logrecord-attributes
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s'
        },
        'dbVerbose':{
            'format' : "[%(asctime)s] %(levelname)s \n    duration: %(duration)s\n   operation: %(sql).10s\n   parameters: %(params)s\n",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        # Los Handlers determinan el proceso que sequira un Record. Basicamente dice a donde ira el Record, si a un fichero,
        # un socket, un correo electronico, etc. Solamente tratarán aqullos Records que tengan el mismo o superior nivel.
        # Ademas, los Handlers pueden aplicar uno o mas filtros para decidir si tratar un Record o no.
        'null': {
            'class': 'logging.NullHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'roomate.log',
            'formatter': 'simple'
        },
        'sessionfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'session.log',
            'formatter': 'verbose'
        },
        'DBQfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'dbAccess.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # Los Loggers son los objetos que crean y envian los records a los Handlers. Solo enviaran aquellos Redors que tengan
        # el mismo o superior nivel. En tu programa instancias uno de los Loggers a continuacion declarados. A traves de el
        # envias Records. Ej: loggerDejemplo = logging.getLogger('nombre')
        #                     loggerDejemplo.info("mensaje del record") <------ hay una funcion para lanzar Records de cada
        #                                                                       nivel.
        # Los niveles son: DEBUG, INFO, WARNING, ERROR y CRITICAL
        'django': {
            'handlers':['null'],
            'propagate': False,
            'level':'INFO',
        },
        'web': {
            'handlers': ['file','sessionfile'],
            'level': 'INFO',
        },
        'database': {
            'handlers': ['file','DBQfile'],
            'level': 'INFO',
        },
        # Este Logger se activara solo enviando un Record por cada sentencia SQL, y solo lo hara si la variable DEBUG de settings.py esta en True.
        # Todos los Records que envie seran de nivel DEBUG (el mas bajo) y por tanto, si se quiere poner en debug pero que no se hagan logs de las
        # instrucciones sql (pues tienen un gran coste), se puede cambiar el nivel del logger a uno superior (como INFO o ERROR).
#        'django.db.backends': {
#            'handlers': ['DBQfile'],
#            'level': 'INFO'
#       }
    }
}



try:
    from .local_settings import *
except ImportError:
    pass

