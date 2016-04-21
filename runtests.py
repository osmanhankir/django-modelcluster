#!/usr/bin/env python
import os
import shutil
import sys

from django.conf import settings
from django.core.management import execute_from_command_line

MODELCLUSTER_ROOT = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(MODELCLUSTER_ROOT, 'test-media')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DATABASE_NAME', 'modelcluster'),
        'USER': os.environ.get('DATABASE_USER', None),
        'PASSWORD': os.environ.get('DATABASE_PASS', None),
        'HOST': os.environ.get('DATABASE_HOST', None),
    }
}

if not settings.configured:
    settings.configure(
        DATABASES=DATABASES,
        INSTALLED_APPS=[
            'modelcluster',

            'django.contrib.contenttypes',
            'taggit',

            'tests',
        ],
        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),
        USE_TZ=True,
        TIME_ZONE='America/Chicago',
        ROOT_URLCONF='tests.urls',
        MEDIA_ROOT=MEDIA_ROOT,
    )


def runtests():
    argv = sys.argv[:1] + ['test'] + sys.argv[1:]
    try:
        execute_from_command_line(argv)
    finally:
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)


if __name__ == '__main__':
    runtests()
