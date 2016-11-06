# -*- coding: utf-8 -*-
from django.db import models
from writer.models import Writer

class Article(models.Model):
    # Se escoge foreign key porque 1 proyecto es de un usuario pero un usuario puede tener muchos proyecots
    writer          = models.ForeignKey(Writer, on_delete=models.CASCADE)
    name            = models.CharField(max_length = 50)
    content        = models.TextField(max_length = 400)
    creationDate    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.writer.username)+"-" + str(self.name)+"--" +str(self.content)+" "+str(self.creationDate) 