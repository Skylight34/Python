import openpyxl
from docx import Document

# Ruta de tu archivo Excel
archivo_excel = "C:\\Users\\atrasfi\OneDrive - Uber Freight\Documents\ListadodeManagers2.xlsx"

# Nombre de la hoja de Excel en la que se encuentra la columna de correos
nombre_hoja = "Sheet1"  # Cambia a la hoja correcta

# Nombre de la columna que contiene los correos
nombre_columna = "Correo"  # Cambia al nombre correcto

# Ruta donde se guardará el archivo de Word
archivo_word = "C:\\Users\\atrasfi\OneDrive - Uber Freight\Documents\correos_separadosq4.docx"

# Cargar el archivo Excel
workbook = openpyxl.load_workbook(archivo_excel, data_only=True)
sheet = workbook[nombre_hoja]

# Crear un nuevo documento de Word
doc = Document()

# Inicializa una cadena vacía para almacenar los valores separados por comas
valores = []

# Iterar a través de las celdas en Excel y agregar sus valores a la cadena
for row in sheet.iter_rows(values_only=True):
    for cell in row:
        valores.append(str(cell))

# Combina los valores con comas y sin saltos de línea
lista_en_comas = ", ".join(valores)

# Agrega la lista en el documento de Word
doc.add_paragraph(lista_en_comas)

# Guarda el documento de Word
doc.save(archivo_word)

print(f"Se ha copiado el listado de Excel a {archivo_word} sin saltos de línea.")