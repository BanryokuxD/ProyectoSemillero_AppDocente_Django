from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings

# Define your custom models

class CentroCostos(models.Model):
    STATUS_CHOICES = [
        ("A", "Prueba centro costos"),
        ("B", ""),
        ("C", ""),
    ]
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Curso(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.AutoField(primary_key=True)
    numero_horas = models.DecimalField(max_digits=20, decimal_places=0)
    nivel = models.CharField(max_length=45) 
    proyecto_curricular = models.CharField(max_length=45)

class Dedicacion(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

class Departamento(models.Model):
    STATUS_CHOICES = [
        ("A", "Ingeniería"),
        ("B", ""),
        ("C", ""),
    ]
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Facultad(models.Model):
    STATUS_CHOICES = [
        ("A", "Sistemas"),
        ("B", ""),
        ("C", ""),
    ]
    
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Nivel(models.Model):
    STATUS_CHOICES = [
        ("A", "Pregrado"),
        ("B", "Maestría"),
        ("C", "Doctorado"),
    ]
    descripcion = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_dedicacion = models.IntegerField()
    categoria_docente = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vinculacion = models.ForeignKey('Vinculacion', on_delete=models.CASCADE)
    dedicacion = models.ForeignKey(Dedicacion, on_delete=models.CASCADE)

class ProyectoCurricular(models.Model):
    STATUS_CHOICES = [
        ("A", "Curricular prueba"),
        ("B", ""),
        ("C", ""),
    ]

    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

class TipoActividad(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    centro_costos = models.ForeignKey(CentroCostos, on_delete=models.CASCADE)
    horas_semanales = models.IntegerField()

class Vinculacion(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

# Define the rest of your custom models (e.g., ActividadDocente, ActividadGestion, ActividadInvestigativa)

class ActividadDocente(models.Model):
    codigo = models.AutoField(primary_key=True)
    funcion = models.CharField(max_length=45)
    numero_estudiantes = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    es_compartido = models.IntegerField(default=0)
    actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    proyecto_curricular = models.ForeignKey(ProyectoCurricular, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()

class ActividadGestion(models.Model):
    id = models.OneToOneField(Profesor, on_delete=models.CASCADE, primary_key=True)
    actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

class ActividadInvestigativa(models.Model):
    id = models.AutoField(primary_key=True)
    funcion = models.CharField(max_length=45)
    acta_departamento = models.CharField(max_length=15)
    acta_facultad = models.CharField(max_length=15)
    titulo_proyecto = models.CharField(max_length=45)
    usuarios = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

class User(AbstractUser):
    departamentos = models.ManyToManyField(Departamento, related_name='usuarios', blank=True)
    facultades = models.ManyToManyField(Facultad, related_name='usuarios', blank=True)

    def __str__(self):
        return self.username
