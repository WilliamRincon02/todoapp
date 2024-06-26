from .base import *

from decouple import config


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!

# ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS").split()

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': dj_database_url(
        default='',
        conn_max_age=600
    )
}