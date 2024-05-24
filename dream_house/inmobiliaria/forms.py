# Importa las clases y funciones necesarias desde Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User, Profile, Inmueble, SolicitudArriendo

# Define un formulario personalizado para la creación de usuarios
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Campos adicionales para el formulario de creación de usuario
        fields = UserCreationForm.Meta.fields + ('RUT', 'email', 'first_name', 'last_name', 'address', 'phone', 'user_type')

# Define un formulario personalizado para la modificación de usuarios
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # Campos permitidos para el formulario de modificación de usuario
        fields = ('RUT', 'email', 'first_name', 'last_name', 'address', 'phone', 'user_type')

# Define un formulario para el perfil de usuario
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Campos del perfil de usuario
        fields = ['bio', 'location', 'imagen']

# Define un formulario para agregar una nueva vivienda
class NuevaViviendaForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        # Campos para el formulario de nueva vivienda
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'num_estacionamientos', 'num_habitaciones', 'num_banos', 'direccion', 'comuna', 'tipo_inmueble', 'precio_mensual', 'imagen']

# Define un formulario para actualizar información de una vivienda
class ActualizarInmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        # Campos para el formulario de actualización de vivienda
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'num_estacionamientos', 'num_habitaciones', 'num_banos', 'direccion', 'comuna', 'tipo_inmueble', 'precio_mensual', 'imagen']

# Define un formulario para solicitudes de arriendo
class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        # Campos para el formulario de solicitud de arriendo
        fields = ['inmueble', 'arrendatario', 'estado']

# Define un formulario personalizado para la autenticación de usuarios
class CustomAuthenticationForm(AuthenticationForm):
    # Etiquetas personalizadas para los campos de usuario y contraseña
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
