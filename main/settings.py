from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

if len(os.environ.get('DEBUG')):
    DEBUG = True
else:
    DEBUG = False
    
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), os.environ.get('ALLOWED_HOSTS2'), 'localhost']

INSTALLED_APPS = [
    'corsheaders',
    'oauth2_provider',
    'rest_framework',
    'users.apps.UsersConfig',
    'projects.apps.ProjectsConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

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

ROOT_URLCONF = 'main.urls'

if DEBUG:
    CORS_ALLOWED_ORIGINS = [
        'http://127.0.0.1:3000',
        'http://localhost:3000',
        'https://echonetwork.app',
        'https://www.echonetwork.app',
        'https://turcotte.tech',
        'https://www.turcotte.tech',
        'https://social.turcotte.tech',
        'https://echo.turcotte.tech',
    ]

else:
    CORS_ALLOWED_ORIGINS = [
        'https://echonetwork.app',
        'https://www.echonetwork.app',
        'https://turcotte.tech',
        'https://www.turcotte.tech',
        'https://social.turcotte.tech',
        'https://echo.turcotte.tech',
    ]

CORS_ALLOW_CREDENTIALS = True

CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = None

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = None

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

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": os.environ['ENGINE'],
        "NAME": os.environ['NAME'],
        "USER": os.environ['USER'],
        "PASSWORD": os.environ['PASSWORD'],
        "HOST": os.environ['HOST'],
        "PORT": "",
    }
}

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

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
AUTH_SERVER_URI = os.environ.get("AUTH_SERVER_URI")
REDIRECT_URI = os.environ.get("REDIRECT_URI")
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/hour',
        'user': '5000/hour'
    }
}

OAUTH2_PROVIDER = {
    'RESOURCE_SERVER_INTROSPECTION_URL': f'{AUTH_SERVER_URI}/o/introspect/',
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (CLIENT_ID, CLIENT_SECRET)
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_ROOT = os.environ.get('MEDIA_ROOT')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
