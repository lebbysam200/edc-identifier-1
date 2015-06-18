#!/usr/bin/env python3
import os
import sys

SOURCE_ROOT = os.path.expanduser('~/git')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edc_identifier.settings")
    sys.path.insert(1, os.path.join(SOURCE_ROOT, 'edc-base/'))
    sys.path.insert(1, os.path.join(SOURCE_ROOT, 'edc-device/'))
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)