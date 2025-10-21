import os
import sys

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jeceProject.settings')

from jeceProject.wsgi import application
