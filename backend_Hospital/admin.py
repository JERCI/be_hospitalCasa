from django.contrib import admin
from .models.usuario import Usuario
from .models.enfermero import Enfermero
from .models.medico import Medico
from .models.historia import Historia
from .models.familiar import Familiar
from .models.paciente import Paciente

admin.site.register(Usuario)
admin.site.register(Enfermero)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Historia)
# Register your models here.
