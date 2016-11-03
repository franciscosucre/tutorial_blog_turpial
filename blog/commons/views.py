'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
# import the logging library
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"
    
class About(TemplateView):
    template_name = "about.html"

class Logout(TemplateView):
    template_name = "logout.html"
    
class Home(LoginRequiredMixin,TemplateView):
    template_name = "home.html"
