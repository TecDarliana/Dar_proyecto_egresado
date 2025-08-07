from django.contrib import admin
from .models import Estado, Municipio, Parroquia, Universidad, DatosPersonales, DatosAcademicos, Direccion

# Register your models here.

admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Parroquia)
admin.site.register(Universidad)
admin.site.register(DatosPersonales)
admin.site.register(DatosAcademicos)
admin.site.register(Direccion)