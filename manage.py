#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # GETTING-STARTED: change 'myproject' to your project name:
    if 'OPENSHIFT_REPO_DIR' in os.environ:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cars4driver.settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cars4driver.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
