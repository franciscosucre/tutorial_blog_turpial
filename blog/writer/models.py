# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Writer(models.Model):
    # Se escogio OneToOneField porque solo hay una relacion con un usuario en ambos sentidos
    user         = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    pseudonym    = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.user.id)+" : " + str(self.user.email)+" -- " + str(self.user.first_name)+" "+str(self.user.last_name)
    
'''
Manejo De Permisos
'''

