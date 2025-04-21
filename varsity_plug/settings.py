import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from .env file
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key: Make sure to always use a secret key in production
SECRET_KEY = os.environ.get('SECRET_KEY', os.getenv('DJANGO_SECRET_KEY', 'django-insecure-your-fallback-secret-key'))

# Debug mode: False on Render, True during local development
DEBUG = 'RENDER' not in os.environ

# Allowed hosts: Add the Render hostname dynamically if it exists
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com']
RENDER_EXTERNAL_HOSTNAME = os.getenv('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helper.apps.HelperConfig',  # Custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Enable static file serving
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'varsity_plug.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'helper_tags': 'helper.templatetags.helper_tags',
            },
        },
    },
]

WSGI_APPLICATION = 'varsity_plug.wsgi.application'

# Database configuration: Use PostgreSQL on Render, SQLite locally
if 'RENDER' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            default=os.getenv('DATABASE_URL')  # Ensure DATABASE_URL is set in Render environment
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation: Secure password settings for production
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (Uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth redirect URLs
LOGIN_REDIRECT_URL = 'redirect_after_login'
LOGOUT_REDIRECT_URL = '/'

# Production security settings
SECURE_SSL_REDIRECT = not DEBUG  # Redirect HTTP to HTTPS in production
SESSION_COOKIE_SECURE = not DEBUG  # Use secure cookies in production
CSRF_COOKIE_SECURE = not DEBUG  # Use secure cookies for CSRF
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0  # Enable HSTS in production
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG  # Apply HSTS to all subdomains in production
SECURE_HSTS_PRELOAD = not DEBUG  # Include preload directive in HSTS header for production

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_HTTPONLY = True  # Make session cookies HttpOnly
SESSION_COOKIE_SAMESITE = 'Lax'  # Limit cross-site cookie usage
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Sessions persist until expiry time
SESSION_COOKIE_AGE = 1209600  # Two weeks

# OpenAI API Key (used in AI features)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
