from django.db import models
from .enfermero import Enfermero
from .paciente import Paciente

class EnfermeroPaciente (models.Model):
    id=models.AutoField(primary_key=True)
    enfermero=models.ForeignKey(Enfermero, on_delete=models.CASCADE)
    paciente= models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cita=models.TimeField(verbose_name= 'Cita', editable=True)
    notas=models.TextField(verbose_name = 'Notas', max_length= 8000)