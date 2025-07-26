"""
WSGI config for citadel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citadel.settings')

# application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application
import os
import sys

# add the virtualenv site-packages path to the sys.path
site_packages = '/home/ec2-user/citadel_final/env/lib/python3.12/site-packages'
if site_packages not in sys.path:
    sys.path.append(site_packages)

project_path = '/home/ec2-user/citadel_final/citadel'
project_path2 = '/home/ec2-user/citadel_final/citadel/citadel'

if project_path not in sys.path:
    sys.path.append(project_path)
if project_path2 not in sys.path:
    sys.path.append(project_path2)

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'citadel.settings')

application = get_wsgi_application()
