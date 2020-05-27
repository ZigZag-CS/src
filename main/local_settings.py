
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '24b(&_)kj4i81z3t0p&#$@oaea!b)c4&k5oea6rz8&_mx7nm#='

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'static'),
                os.path.join(BASE_DIR, 'apps/home/static'),
                os.path.join(BASE_DIR, 'apps/dashboard/static'),
                # os.path.join(BASE_DIR, 'apps/pages/static'),
                # os.path.join(BASE_DIR, 'apps/scontent2/static'),
                # os.path.join(BASE_DIR, 'static/utils/bootstrap44'),
                # os.path.join(BASE_DIR, 'static/utils/custom'),
]

# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# )
