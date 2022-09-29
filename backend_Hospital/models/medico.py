from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE) #usuario_id
    especialidad=models.CharField('Especialidad', max_length=50)
    registro=models.CharField('Registro', max_length=50) 