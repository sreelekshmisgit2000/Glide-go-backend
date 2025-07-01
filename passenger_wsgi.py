import os
import sys

# Add the project base directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
