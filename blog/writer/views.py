# -*- coding: utf-8 -*-
'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
from writer.form import WriterRegister
from django.views.generic import CreateView
from writer.models import Writer
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# import the logging library
import logging
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Get an instance of a logger
logger = logging.getLogger(__name__)

class RegisterWriter(CreateView,SuccessMessageMixin):
    form_class = WriterRegister
    model = Writer
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request,"Haz registrado exitosamente a " + form.cleaned_data['username'])
        return CreateView.form_valid(self, form)

class RegisterWriterDone(TemplateView):
    template_name = "writer/writer_register_done.html"
    
class Profile(DetailView):
    model = Writer
    fields=['username','first_name','last_name','email','pseudonym']
    
class EditProfile(UpdateView):
    model = Writer
    fields=['username','first_name','last_name','email','pseudonym']
    
    def get_success_url(self):
        return reverse_lazy('EditWriterProfile', kwargs={'pk':self.kwargs[ 'pk' ]})
    
    def form_valid(self, form):
        messages.success(self.request,"Haz editado exitosamente el perfil")
        return UpdateView.form_valid(self, form)