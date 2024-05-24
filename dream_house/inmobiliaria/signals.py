from django.db.models.signals import post_save  # Importa la señal post_save
from django.dispatch import receiver  # Importa el decorador receiver
from .models import User, Profile  # Importa los modelos User y Profile

# Define un receptor para la señal post_save del modelo User
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Verifica si se ha creado una nueva instancia de User
    if created:
        # Crea un nuevo perfil asociado a la instancia de User creada
        Profile.objects.create(user=instance)

# Define otro receptor para la señal post_save del modelo User
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Guarda el perfil asociado a la instancia de User
    instance.profile.save()
