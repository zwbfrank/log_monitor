import os
import sys

reload(sys)

sys.setdefaultencoding('utf8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE","log_monitor.settings")
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
