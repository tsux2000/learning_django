#!/usr/bin/env python

"""
Generate Secret Key
"""

from django.core.management.utils import get_random_secret_key

print("SECRET_KEY={}".format(get_random_secret_key()))
