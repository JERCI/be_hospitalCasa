from django.db import models

class Historia (models.Model):
    id=models.AutoField(primary_key=True)
    oximetria=models.CharField('Oximetra', max_length=50)
    f_respiratoria=models.CharField('Frecuencia Respiratoria', max_length=50)
    f_cardiaca=models.CharField('Frecuencia Cardiaca', max_length=50)
    temperatura=models.CharField('Temperatura', max_length=50)
    presion_arterial=models.CharField('Presion Arterial', max_length=50)
    glicemias=models.CharField('Glicemias', max_length=50)
    diagnosticos=models.CharField('Diagnosticos', max_length=8000)
    cuidados=models.CharField('Cuidados', max_length=8000)
