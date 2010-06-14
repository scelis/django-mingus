import os
import sys
import site

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
root_dir = os.path.join(project_dir, '..')
site.addsitedir(os.path.join(root_dir, 'lib/python2.6/site-packages'))
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mingus.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
