from django.db import models


class Estado(models.Model):
     nombre = models.CharField('Estado: ', max_length=100, blank = True, null = True)
     
     def __str__(self):
        return self.nombre


class Municipio(models.Model):
     nombre = models.CharField('Municipio: ', max_length=100, blank = True, null = True)
     estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank = True, null = True)
     
     def __str__(self):
        return f"{self.nombre} ({self.estado.nombre})" if self.estado else self.nombre

class Parroquia(models.Model):
      nombre = models.CharField('Parroquia: ', max_length=100, blank = True, null = True)
      municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank = True, null = True)
      
      def __str__(self):
        return f"{self.nombre} ({self.municipio.nombre})" if self.municipio else self.nombre


class Universidad(models.Model):
    nombre = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    nombre = models.CharField(max_length=350)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class DatosPersonales(models.Model):
    
    TITULARIDAD_CHOICES = [
        ('pregrado','Pregado'),
        ('postgrado','Postgrado'),
        ('maestria',',Maestria'),
        ('doctorado','Doctorado'),
    ]
    
    NACIONALIDAD_CHOICES = [
        ('v','V'),
        ('e','E'),
    ]

    cedula = models.CharField('Cédula:', unique=True, max_length=20)
    nombres = models.CharField('Nombres:', max_length=200)
    apellidos = models.CharField('Apellidos:', max_length=200)
    email = models.EmailField("Correo Electrónico: ", unique=True, max_length=200)
    telefono = models.IntegerField("Teléfono Celular")
    telefono2 = models.IntegerField("Teléfono Local o Alternativo")
    fecha_naci = models.DateField ('Fecha de Nacimiento')
    lugar_naci = models.CharField('Lugar de Nacimiento:', max_length=200)
    nacionalidad = models.CharField('Nacionalidad:', choices=NACIONALIDAD_CHOICES, max_length=2)
    titularidad = models.CharField('Titularidad:', choices=TITULARIDAD_CHOICES, max_length=20)
    idiomas = models.CharField('Idiomas que Domina:', max_length=200)
    ocupacion = models.CharField('Ocupación Actual:', max_length=200)
    
    # Dirección de habitación
    direccion = models.CharField('Dirección en Venezuela:', max_length=200)
    estado_dir = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)
    municipio_dir = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    parroquia_dir = models.ForeignKey(Parroquia, on_delete=models.SET_NULL, null=True, blank=True)

    fecha_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"{self.cedula} ({self.nombres} {self.apellidos})"


class DatosAcademicos(models.Model):
    
     TIPO_BECA_CHOICES = [
        ('nacional','Nacional'),
        ('internacional','Internacional'),
    ]
    
     TIPO_BECARIO_CHOICES = [
        ('extran_venz','Extranjero en Venezuela'),
        ('venz_venz','Venezolano(a) en Venezuela'),
        ('venz_extran','Venezolano(a) en el Extranjero'),
    ]
     
     becario = models.OneToOneField(DatosPersonales, on_delete=models.CASCADE, related_name='datos_academicos')
     tipo_beca = models.CharField('Tipo de Beca:', choices=TIPO_BECA_CHOICES, max_length=20)
     carrera = models.CharField('Carrera Cursada:', max_length=200)
     fecha_ing = models.DateField ('Fecha de Ingreso')
     fecha_egr = models.DateField ('Fecha de Egreso/Graduación')
     tipo_becario = models.CharField('Tipo de Becario:', choices=TIPO_BECARIO_CHOICES, max_length=20)
     universidad = models.ForeignKey(Universidad, on_delete=models.SET_NULL, null=True, blank=True)

     def __str__(self):
          return f"Becario: {self.becario.nombres}, Universidad: {self.universidad.nombre}"
