import os
import sys
import django
from django.db import connection

# Añade el directorio del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Configura Django para usar el entorno del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dream_house.settings')
django.setup()

def get_inmuebles_by_comuna():
    # Utiliza un cursor para ejecutar una consulta SQL personalizada
    with connection.cursor() as cursor:
        # Ejecuta la consulta SQL para obtener información sobre los inmuebles agrupados por comuna
        cursor.execute('''
            SELECT c.name as comuna, i.name as inmueble, i.description
            FROM inmobiliaria_comuna c
            JOIN inmobiliaria_inmueble i ON i.comuna_id = c.id
            ORDER BY c.name, i.name
        ''')
        # Obtiene los resultados de la consulta
        inmuebles = cursor.fetchall()
    
    # Verifica si se encontraron inmuebles
    if not inmuebles:
        print("No se encontraron inmuebles.")
        return
    
    # Escribe los resultados en un archivo de texto
    with open('inmuebles_por_comuna.txt', 'w') as file:
        current_comuna = None
        for comuna, inmueble, description in inmuebles:
            # Agrupa los inmuebles por comuna en el archivo de texto
            if comuna != current_comuna:
                file.write(f"\nComuna: {comuna}\n")
                current_comuna = comuna
            file.write(f"\tInmueble: {inmueble}\n\tDescripción: {description}\n")

if __name__ == "__main__":
    # Llama a la función principal para obtener los inmuebles por comuna
    get_inmuebles_by_comuna()
