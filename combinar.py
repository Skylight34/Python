import os
import PyPDF2
from datetime import datetime


def combinar_pdf(archivos, directorio_salida):
    archivos_ordenados = sorted(archivos, key=os.path.getmtime)  # Ordenar por fecha de modificación
    fusionador = PyPDF2.PdfMerger()

    for archivo in archivos_ordenados:
        fusionador.append(archivo)

    fecha_actual = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    archivo_salida = os.path.join(directorio_salida, f'combinado_{fecha_actual}.pdf')

    with open(archivo_salida, 'wb') as salida:
        fusionador.write(salida)
    return archivo_salida

# Función para obtener la lista de archivos PDF en un directorio
def obtener_archivos_pdf(directorio):
    archivos_pdf = [
        os.path.join(directorio, archivo) for archivo in os.listdir(directorio)
        if archivo.lower().endswith('.pdf')  # Filtrar solo archivos PDF
    ]
    return archivos_pdf

# Obtener la ruta del directorio donde se encuentra el script actual
directorio_programa = os.path.dirname(__file__)

# Obtener la lista de archivos PDF en el directorio del script
archivos_a_combinar = obtener_archivos_pdf(directorio_programa)

# Verificar si se encontraron archivos PDF en el directorio
if archivos_a_combinar:
    # Llamada a la función para combinar los archivos y obtener la ruta del archivo combinado
    ruta_archivo_combinado = combinar_pdf(archivos_a_combinar, directorio_programa)
    print(f"Archivos combinados con éxito. El archivo combinado se encuentra en: {ruta_archivo_combinado}")
else:
    print("No se encontraron archivos PDF en el directorio del programa/ejecutable.")
