import os
import sys
import django
from django.db import connection

# Importa Django y otras librerías necesarias
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Añade el directorio del proyecto al PYTHONPATH
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dream_house.settings')  # Configura Django para usar el entorno del proyecto
django.setup()  # Configura Django

def get_inmuebles_by_region():
    # Utiliza un cursor para ejecutar una consulta SQL personalizada
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT r.name as region, c.name as comuna, i.name as inmueble, i.description
            FROM inmobiliaria_region r
            JOIN inmobiliaria_comuna c ON c.region_id = r.id
            JOIN inmobiliaria_inmueble i ON i.comuna_id = c.id
            ORDER BY r.name, c.name, i.name
        ''')
        # Obtiene los resultados de la consulta
        inmuebles = cursor.fetchall()

    # Verifica si se encontraron inmuebles
    if not inmuebles:
        print("No se encontraron inmuebles.")
        return

    # Escribe los resultados en un archivo de texto
    with open('inmuebles_por_region.txt', 'w') as file:
        current_region = None
        for region, comuna, inmueble, description in inmuebles:
            # Agrupa los inmuebles por región en el archivo de texto
            if region != current_region:
                file.write(f"\nRegión: {region}\n")
                current_region = region
            file.write(f"\tComuna: {comuna}\n\t\tInmueble: {inmueble}\n\t\tDescripción: {description}\n")

if __name__ == "__main__":
    # Llama a la función principal para obtener los inmuebles por región
    get_inmuebles_by_region()
