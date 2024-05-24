from django.urls import path, include
from . import views

urlpatterns = [
    # Ruta para la página de inicio
    path('', views.home_view, name='home'),
    # Ruta para ver el perfil del usuario
    path('profile/', views.profile_view, name='profile'),
    # Ruta para registrar un nuevo usuario
    path('register/', views.register_view, name='register'),
    # Ruta para iniciar sesión
    path('login/', views.login_view, name='login'),
    # Ruta para editar el perfil del usuario
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    # Incluye las rutas de autenticación proporcionadas por Django
    path('accounts/', include('django.contrib.auth.urls')), 
    # Ruta para la página de perfil del usuario
    path('accounts/profile/', views.profile_view, name='profile'),
    # Ruta para agregar una nueva vivienda al sistema
    path('nueva-vivienda/', views.agregar_vivienda, name='agregar_vivienda'),
    # Ruta para actualizar los detalles de una vivienda
    path('actualizar_inmueble/<int:inmueble_id>/', views.actualizar_inmueble, name='actualizar_inmueble'),
    # Ruta para borrar una vivienda del sistema
    path('borrar_inmueble/<int:inmueble_id>/', views.borrar_inmueble, name='borrar_inmueble'),
    # Ruta para ver las propiedades del usuario actual
    path('mis_propiedades/', views.mis_propiedades, name='mis_propiedades'),
    # Ruta para ver todas las propiedades disponibles
    path('ver_inmuebles/', views.ver_inmuebles, name='ver_inmuebles'),
    # Ruta para ver los detalles de una vivienda específica
    path('inmuebles/<int:inmueble_id>/', views.detalles_inmueble, name='detalles_inmueble'),
    # Ruta para solicitar arriendo de una vivienda específica
    path('solicitar_arriendo/<int:inmueble_id>/', views.solicitar_arriendo, name='solicitar_arriendo'),
]

