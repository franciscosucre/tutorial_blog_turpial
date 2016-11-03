# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser  

class Writer(AbstractUser):
    # Se escogio OneToOneField porque solo hay una relacion con un usuario en ambos sentidos
    REQUIRED_FIELDS=['email','first_name','last_name']
    pseudonym    = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.username)+" : " + str(self.user.email)+" -- " + str(self.user.first_name)+" "+str(self.user.last_name)
    
    def get_pseudonym(self):
        return self.pseudonym
    
    def update(self,username=None,email=None,first_name=None,last_name=None,pseudonym=None):
        if username: self.username=username
        if email: self.email=email
        if first_name: self.first_name=first_name
        if last_name: self.last_name=last_name
        if pseudonym: self.pseudonym=pseudonym
        self.save()