from django.db import models




class Estado(models.Model):
     nombre = models.CharField('Estado: ', max_length=100, blank = True, null = True)
     def __str__(self):
        return self.nombre # Muestra el nombre del estado


class Municipio(models.Model):
     nombre = models.CharField('Municipio: ', max_length=100, blank = True, null = True)
     estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank = True, null = True, related_name='municipios')
     def __str__(self):
        # Es útil incluir el estado para mayor claridad si el nombre del municipio no es único globalmente
        return f"{self.nombre} ({self.estado.nombre})" if self.estado else self.nombre

class Parroquia(models.Model):
      nombre = models.CharField('Parroquia: ', max_length=100, blank = True, null = True)
      municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE,related_name='parroquias', blank = True, null = True)
      def __str__(self):
        # Incluye el municipio para mayor claridad
        return f"{self.nombre} ({self.municipio.nombre})" if self.municipio else self.nombre








class DatosPersonales(models.Model):
    

    titularidad = [
        
        ('pregrado','Pregado'),
        ('postgrado','Postgrado'),
        ('maestria',',Maestria'),
        ('doctorado','Doctorado'),
    ]
    
    nacionalidad = [
        
        ('v','V'),
        ('e','E'),
    ]

    id = models.AutoField(primary_key=True)

    cedula = models.CharField('Cédula:', unique=True, blank = False, null = False)
    nombres = models.CharField('Nombres:', max_length=200,blank = False, null = False)
    apellidos = models.CharField('Apellidos:', max_length=200, blank = False, null = False)
    email = models.EmailField("Correo Electrónico: ", max_length=200, unique=True, blank = False, null = False)
    telefono = models.IntegerField("Teléfono Celular", blank=False,null=False)
    telefono2 = models.IntegerField("Teléfono Local o Alternativo", blank=False,null=False)
    fecha_naci = models.DateField ('Fecha de Nacimiento', blank = False, null = False)
    lugar_naci = models.CharField('Lugar de Nacimiento:', max_length=200,blank = False, null = False)
    nacionalidad = models.CharField('Nacionalidad:', choices=nacionalidad, max_length=200, blank = False, null = False)
    titularidad = models.CharField('Titularidad:', choices=titularidad, max_length=200, blank = False, null = False)
    idiomas = models.CharField('Idiomas qué Domina:', max_length=200, blank = False, null = False)
    ocupacion = models.CharField('Ocupación Actual:', max_length=200, blank = False, null = False)
    # Dirección de habitación
    direccion = models.CharField('Dirección en Venezuela:', max_length=200,blank = False, null = False)
    estado = models.ForeignKey(Estado, max_length=100, on_delete=models.CASCADE, blank = True, null = True)
    municipio = models.ForeignKey(Municipio, max_length=100, on_delete=models.CASCADE, blank = True, null = True)
    parroquia = models.ForeignKey(Parroquia, max_length=100, on_delete=models.CASCADE, blank = True, null = True)

    fecha_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"{self.cedula} ({self.nombres} pc(s))"
    

class DatosAcademicos(models.Model):
    

     tipo_beca = [
        
        ('nacional','Nacional'),
        ('internacional','Internacional'),
    ]
    
     tipo_becario = [
        
        ('extran_venz','Extranjero en Venezuela'),
        ('venz_venz','Venezolano(a) en Venezuela'),
        ('venz_extran','Venezolano(a) en el Extranjero'),
    ]
     

     becario = models.OneToOneField(DatosPersonales, on_delete=models.CASCADE, related_name='datos_academicos')
     tipo_beca = models.CharField('Tipo de Beca:', choices=tipo_beca, max_length=200, blank = False, null = False)
     carrera = models.CharField('Carrera Cursada:', max_length=200, blank = False, null = False)
     fecha_ing = models.DateField ('Fecha de Ingreso', blank = False, null = False)
     fecha_egr = models.DateField ('Fecha de Egreso/Graduación', blank = False, null = False)
     tipo_becario = models.CharField('Tipo de Becario:', choices=tipo_becario, max_length=200, blank = False, null = False)
     universidad = models.CharField('Nombre de la Universidad:', max_length=200, blank = False, null = False)

     def __str__(self):
          return f"{self.becario} ({self.universidad} pc(s))"