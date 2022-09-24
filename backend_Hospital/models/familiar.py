from django.db import models
from .usuario import Usuario

class Familiar(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('Nombre', max_length = 50)
    parentesco= models.CharField('Parentesco', max_length=50)