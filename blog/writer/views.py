# -*- coding: utf-8 -*-
'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
from writer.form import WriterRegister
from django.views.generic import CreateView
from writer.models import Writer
# import the logging library
import logging
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

# Get an instance of a logger
logger = logging.getLogger(__name__)

class RegisterWriter(CreateView):
    form_class = WriterRegister
    model = Writer
    success_url = '/writer/register_done'

class RegisterWriterDone(TemplateView):
    template_name = "writer/writer_register_done.html"
    
class Profile(DetailView):
    model = Writer
    fields=['username','first_name','last_name','email','pseudonym']
    
class EditProfile(UpdateView):
    model = Writer
    fields=['username','first_name','last_name','email','pseudonym']
    success_url='/writer/Profile/'
    
    def form_valid(self, form):
        self.success_url= self.success_url + self.kwargs[ 'pk' ]
        return UpdateView.form_valid(self, form)