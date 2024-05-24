from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserProfileForm, CustomUserCreationForm, CustomUserChangeForm, NuevaViviendaForm, ActualizarInmuebleForm ,SolicitudArriendoForm, CustomAuthenticationForm
from .models import Profile , Inmueble , Region, Comuna

@login_required
def profile_view(request):
    # Vista para ver el perfil de un usuario
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'profile.html', {'user': user, 'profile': profile})

def register_view(request):
    """
    Vista para registrar un nuevo usuario.
    """
    # Vista para el registro de un nuevo usuario
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    # Vista para iniciar sesión
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def edit_profile_view(request):
    # Vista para editar el perfil de un usuario
    user = request.user
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = CustomUserChangeForm(instance=user)
        profile_form = UserProfileForm(instance=user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'edit_profile.html', context)

def home_view(request):
    # Vista para la página de inicio
    return render(request, 'home.html')

@login_required
def agregar_vivienda(request):
    # Vista para agregar una nueva vivienda al sistema
    if request.method == 'POST':
        form = NuevaViviendaForm(request.POST, request.FILES)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user  
            inmueble.save()
            return redirect('mis_propiedades')
    else:
        form = NuevaViviendaForm()
    return render(request, 'agregar_vivienda.html', {'form': form})

@login_required
def actualizar_inmueble(request, inmueble_id):
    # Vista para actualizar los detalles de una vivienda
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
    if request.method == 'POST':
        form = ActualizarInmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ActualizarInmuebleForm(instance=inmueble)
    return render(request, 'actualizar_inmueble.html', {'form': form})

def borrar_inmueble(request, inmueble_id):
    # Vista para borrar una vivienda del sistema
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('profile') 
    return render(request, 'borrar_inmueble.html', {'inmueble': inmueble})

def mis_propiedades(request):
    # Vista para ver las propiedades del usuario actual
    inmuebles = Inmueble.objects.filter(arrendador=request.user)
    return render(request, 'mis_propiedades.html', {'inmuebles': inmuebles})

def ver_inmuebles(request):
    # Vista para ver todas las propiedades disponibles
    # Obtener y ordenar las comunas alfabéticamente
    comunas = Comuna.objects.all().order_by('name')
    # Obtener y ordenar las regiones
    regiones = Region.objects.all().order_by('name')
    # Obtener los inmuebles
    inmuebles = Inmueble.objects.all()

    # Filtrar por región si se ha seleccionado una
    region_id = request.GET.get('region')
    if region_id:
        inmuebles = inmuebles.filter(comuna__region_id=region_id)

    # Filtrar por comuna si se ha seleccionado una
    comuna_id = request.GET.get('comuna')
    if comuna_id:
        inmuebles = inmuebles.filter(comuna_id=comuna_id)

    context = {
        'comunas': comunas,
        'regiones': regiones,
        'inmuebles': inmuebles,
    }

    return render(request, 'ver_inmuebles.html', context)
def detalles_inmueble(request, inmueble_id):
    # Obtener el inmueble usando su ID
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    return render(request, 'detalles_inmueble.html', {'inmueble': inmueble})

def solicitar_arriendo(request, inmueble_id):
    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('solicitud_exitosa')  
    else:
        form = SolicitudArriendoForm()
    return render(request, 'solicitar_arriendo.html', {'form': form})
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'