from django import forms
from aplicaciones.formulario_egresados.models import *
from .models import *




class datos_pesonales_formModel(forms.ModelForm):
    
    class Meta:
        model=DatosPersonales
        
        fields= "__all__"
        widgets = {
               # Los widgets se usarán en el template, pero la lógica de filtrado va en JS
            #'estado':  forms.Select(attrs={'onchange':"filtrarMunicipio(this.value)"}),
          #  'municipio':  forms.Select(attrs={'onchange':"filtrarParroquia(this.value)"}),
          #  'parroquia': forms.Select(),

        }

    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aquí puedes precargar los estados, pero los municipios y parroquias
        # se cargarán con JavaScript.
        self.fields['estado'].queryset = estado.objects.all()
        self.fields['municipio'].queryset = municipio.objects.none()
        self.fields['parroquia'].queryset = parroquia.objects.none()

        if 'estado' in self.data:
            try:
                estado_id = int(self.data.get('estado'))
                self.fields['municipio'].queryset = municipio.objects.filter(estado_id=estado_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        
        if 'municipio' in self.data:
            try:
                municipio_id = int(self.data.get('municipio'))
                self.fields['parroquia'].queryset = parroquia.objects.filter(municipio_id=municipio_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
                
                """

class datos_academicos_formModel(forms.ModelForm):
    
    class Meta:
        model=DatosAcademicos

        exclude = ('becario',)
        
        fields= "__all__"
        widgets = {
       #    'estado': forms.Select(attrs={'onchange':"filtrarDireccion(this.value)"}),
        #   'municipio': forms.Select(attrs={'onchange':"filtrarDireccion(this.value)"}),
         #  'parroquia': forms.Select(attrs={'onchange':"filtrarDireccion(this.value)"}),

        }