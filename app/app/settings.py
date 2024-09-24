from pathlib import Path
import os
import environ

from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# 環境変数の読み込み
env = environ.Env(DEBUG=(bool,False))
env.read_env(os.path.join(BASE_DIR,'.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
#SECRET_KEY = 'django-insecure-q@6@wvt7&)c68j6x3qiqy0e8yu$v*06r7i_)1&-n4w)@w5h8e4' 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get_value('DEBUG', cast = bool, default = True)
SQLITE = env.get_value('SQLITE', cast = bool, default = True)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [env('IP_ADDRESS'), 'xxx.com', 'www.xxx.com', 'localhost']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdownx', #markdownxを使用する場合
    'article', #追加したapp名
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls' #プロジェクト名をxxxに入れる

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

WSGI_APPLICATION = 'app.wsgi.application' #プロジェクト名をxxxに入れる


if SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME_SQL'),
        'USER': env('DB_USER_SQL'),
        'PASSWORD': env('DB_PASSWORD_SQL'),
        'HOST': 'localhost',
        'PORT': 3306 if DEBUG else '',
    }
    }



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

# 英語対応の場合は 下記コメントアウトを外す
LANGUAGES = [
    ('ja', _('日本語')),
    # ('en', _('English')),
]

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media files
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


# Upload Settings

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640


### --- MarkdownX --- ###
# Markdownxを使用する場合はコメントアウトを外す

## Extention
MARKDOWNX_MARKDOWN_EXTENSIONS = [
     'markdown.extensions.sane_lists',
     'markdown.extensions.nl2br',
     'markdown.extensions.extra',
     'markdown.extensions.toc',
     'markdown.extensions.tables'
 ]

## Content Type
MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/svg+xml', 'application/pdf']


