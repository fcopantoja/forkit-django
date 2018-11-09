#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691."""
import sys

import environ
from django import setup
from django.conf import settings

env = environ.Env()


settings.configure(
    CACHES={'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}},
    DATABASES={'default': env.db(default='postgres:///forkit')},
    INSTALLED_APPS=('forkit', 'forkit.tests'),
)

setup()

# This must be after settings.configure.
from django.test.runner import DiscoverRunner

test_runner = DiscoverRunner(verbosity=2)


failures = test_runner.run_tests([])
if failures:
    sys.exit(1)
