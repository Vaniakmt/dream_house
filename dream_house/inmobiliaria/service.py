from .models import Inmueble, User, SolicitudArriendo
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

def create_user(data):
    # Obtener los datos del usuario
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    RUT = data.get('RUT')
    address = data.get('address')
    phone = data.get('phone')
    user_type = data.get('user_type')

    # Crear el usuario
    user = User.objects.create_user(username=username, email=email, password=password)
    user.RUT = RUT
    user.address = address
    user.phone = phone
    user.user_type = user_type
    user.save()

    # Asignar el usuario al grupo correspondiente
    if user_type == 'arrendador':
        group, created = Group.objects.get_or_create(name='Arrendadores')
        user.groups.add(group)
    elif user_type == 'arrendatario':
        group, created = Group.objects.get_or_create(name='Arrendatarios')
        user.groups.add(group)

    return user


# Crear un inmueble
def create_inmueble(data):
    arrendador = get_object_or_404(User, id=data['arrendador_id'])
    inmueble = Inmueble.objects.create(
        name=data['name'],
        description=data['description'],
        m2_construidos=data['m2_construidos'],
        m2_totales=data['m2_totales'],
        num_estacionamientos=data['num_estacionamientos'],
        num_habitaciones=data['num_habitaciones'],
        num_banos=data['num_banos'],
        address=data['address'],
        comuna=data['comuna'],
        tipo_inmueble=data['tipo_inmueble'],
        precio_mensual=data['precio_mensual'],
        arrendador=arrendador
    )
    return inmueble

# Listar todos los inmuebles
def list_inmuebles():
    return Inmueble.objects.all()

# Actualizar un inmueble
def update_inmueble(id, data):
    inmueble = get_object_or_404(Inmueble, id=id)
    inmueble.name = data['name']
    inmueble.description = data['description']
    inmueble.m2_construidos = data['m2_construidos']
    inmueble.m2_totales = data['m2_totales']
    inmueble.num_estacionamientos = data['num_estacionamientos']
    inmueble.num_habitaciones = data['num_habitaciones']
    inmueble.num_banos = data['num_banos']
    inmueble.address = data['address']
    inmueble.comuna = data['comuna']
    inmueble.tipo_inmueble = data['tipo_inmueble']
    inmueble.precio_mensual = data['precio_mensual']
    inmueble.save()
    return inmueble

# Borrar un inmueble
def delete_inmueble(id):
    inmueble = get_object_or_404(Inmueble, id=id)
    inmueble.delete()
