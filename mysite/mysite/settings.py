"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.conf import settings
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i#==571l45#n60ki2ut^k^qm(yd(p^o671_)pbt#b3&ke-_^_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'filebrowser',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'django_mptt_admin',
    'taggit',
    'blog',
    'main',
    'library',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite',
        'USER': 'django',
        'PASSWORD': '34652817',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Irkutsk'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# STATIC_URL = 'static/'

# Add these new lines
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
PROJECT_DIR = os.path.dirname(__file__)

TINYMCE_SPELLCHECKER = True
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")

FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''

X_FRAME_OPTIONS = 'SAMEORIGIN'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TINYMCE_JS_URL = STATIC_URL / 'tinymce/tinymce.min.js'
# TINYMCE_DEFAULT_CONFIG = {
#     "height": "320px",
#     "width": "960px",
#     "menubar": "file edit view insert format tools table help",
#     "plugins": "media image preview advlist autolink lists link  charmap print preview anchor searchreplace visualblocks code "
#                "fullscreen insertdatetime media table paste code help wordcount spellchecker",
#     "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
#                "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
#                "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
#                "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
#                "a11ycheck ltr rtl | showcomments addcomment code",
#     "custom_undo_redo_levels": 10,
#     "language": "ru",  # To force a specific language instead of the Django current language.
#     "image_title": "true",
#     "image_caption": "true",
#     "automatic_uploads": "true",
# }

TINYMCE_DEFAULT_CONFIG = {
    "relative_urls": False,
    "remove_script_host": False,
    "convert_urls": True,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',

    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    "language": "en_US",
}

GRAPPELLI_ADMIN_TITLE = "mineev03"
GRAPPELLI_SWITCH_USER = True

DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

EXTENSIONS = getattr(settings, "FILEBROWSER_EXTENSIONS", {
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
})

VERSIONS = getattr(settings, "FILEBROWSER_VERSIONS", {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
})

VERSION_QUALITY = getattr(settings, 'FILEBROWSER_VERSION_QUALITY', 90)

TAGGIT_CASE_INSENSITIVE = True

LOGIN_REDIRECT_URL = 'main:index'
LOGOUT_REDIRECT_URL = 'main:index'
LOGIN_URL = reverse_lazy('login')