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

# Get an instance of a logger
logger = logging.getLogger(__name__)

class RegisterWriter(CreateView):
    form_class = WriterRegister
    model = Writer
    success_url = '/writer/register_done'

class RegisterWriterDone(TemplateView):
    template_name = "writer/writer_register_done.html"