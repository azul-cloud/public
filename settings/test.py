from .base import *

'''
Test settings and globals which
allow us to run our test suite
locally.
'''

SOUTH_TESTS_MIGRATE = False

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}