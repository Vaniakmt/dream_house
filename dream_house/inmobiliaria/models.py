from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Define un modelo de usuario personalizado que hereda de AbstractUser
class User(AbstractUser):
    # Atributos adicionales para el modelo de usuario
    RUT = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    USER_TYPE_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='arrendatario')

# Define un modelo para representar regiones geográficas
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define un modelo para representar comunas dentro de una región
class Comuna(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Define un modelo para representar inmuebles disponibles para arriendo
class Inmueble(models.Model):
    # Atributos del inmueble
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_totales = models.DecimalField(max_digits=10, decimal_places=2)
    num_estacionamientos = models.PositiveIntegerField()
    num_habitaciones = models.PositiveIntegerField()
    num_banos = models.PositiveIntegerField()
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipo_inmueble_choices = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    )
    tipo_inmueble = models.CharField(max_length=12, choices=tipo_inmueble_choices)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    arrendador = models.ForeignKey(User, related_name='inmuebles', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='propiedades/', null=True, blank=True)

# Define un modelo para representar las solicitudes de arriendo
class SolicitudArriendo(models.Model):
    inmueble = models.ForeignKey(Inmueble, related_name='solicitudes_de_arriendo', on_delete=models.CASCADE)
    arrendatario = models.ForeignKey(User, related_name='solicitudes_de_arriendo', on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado')], default='pendiente')

# Define un modelo para el perfil de usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    imagen = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username
