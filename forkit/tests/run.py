#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691."""
import argparse
import sys

import environ
from django import setup
from django.conf import settings
from django.test.runner import DiscoverRunner

env = environ.Env()


settings.configure(
    CACHES={'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}},
    DATABASES={'default': env.db(default='postgres:///forkit')},
    INSTALLED_APPS=('forkit', 'forkit.tests'),
)


setup()

parser = argparse.ArgumentParser()
parser.add_argument('tests', type=unicode, nargs='*', default=[])
parser.add_argument('-v', '--verbosity', type=int, default=1)
parser.add_argument('--failfast', action='store_true')
parser.add_argument('--reverse', action='store_true')

arg_dict = vars(parser.parse_args())
tests_to_run = arg_dict.pop('tests')

test_runner = DiscoverRunner(**arg_dict)
failures = test_runner.run_tests(tests_to_run)


if failures:
    sys.exit(1)
