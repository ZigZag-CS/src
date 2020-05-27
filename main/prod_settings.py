
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '=yniyby9f^j8qwr@%f1=+27h74l2jfe&dge+6i_!3ulsz%5#o@'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '92.39.50.59']

INTERNAL_IPS = ['127.0.0.1', '92.39.50.59']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'miki',
        'PASSWORD': 'Qwerty96068',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# DEFAULT_FROM_EMAIL = 'email'
# EMAIL_HOST = 'smtp'
# EMAIL_HOST_USER = 'email'
# EMAIL_HOST_PASSWORD = 'pass'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False