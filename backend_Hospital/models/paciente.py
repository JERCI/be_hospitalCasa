from django.db import models
from .usuario import Usuario
from .enfermero import Enfermero
from .medico import Medico
from .historia import Historia
from .familiar import Familiar

class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    familiar=models.ForeignKey(Familiar, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)
    enfermero=models.ForeignKey(Enfermero, on_delete=models.CASCADE)
    historia=models.ForeignKey(Historia, on_delete=models.CASCADE)