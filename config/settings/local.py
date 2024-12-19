from os import getenv, path 
from dotenv import load_dotenv
from .base import * # noqa 
from .base import BASE_DIR

SECRET_KEY = "django-insecure-px%dmbayevr1yk0t!_^wo7g_781&x=v%%c%^u%^d*_#o^1bm*h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []