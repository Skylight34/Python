import configparser
import pyodbc
import pandas as pd

# Crea un objeto ConfigParser y lee el archivo de configuración
config = configparser.ConfigParser()
config.read('config.txt')  # Asegúrate de que el archivo esté en el mismo directorio que tu script

# Obtiene la configuración desde el archivo
server = config['SQL_Config']['server']
database = config['SQL_Config']['database']
driver = config['SQL_Config']['driver']
archivo_a_cargar = config['SQL_Config']['archivo_a_cargar']
nombre_tabla = config['SQL_Config']['nombre_tabla']

# Configura la conexión a SQL Server utilizando la configuración del archivo
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes')

try:
    # Crear un cursor SQL
    cursor = conn.cursor()

    # Verificar si la tabla existe
    cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ?", nombre_tabla)
    tabla_existe = cursor.fetchone()[0] > 0

    if not tabla_existe:
        # La tabla no existe, crearla con los campos especificados
        cursor.execute(f"CREATE TABLE {nombre_tabla} ("
                       "NumeroDeParte NVARCHAR(MAX), "
                       "NPLimpio NVARCHAR(MAX), "
                       "DescripcionSAP NVARCHAR(MAX), "
                       "HTSSiemens2020NICo NVARCHAR(MAX), "
                       "HTSSiemens2022NICo NVARCHAR(MAX), "
                       "DescripcionSiemens NVARCHAR(MAX), "
                       "ValidacionHTS2020 NVARCHAR(MAX), "
                       "ValidacionHTS2022 NVARCHAR(MAX)"
                       ")")
        conn.commit()
        print(f"Tabla '{nombre_tabla}' creada exitosamente.")

    # Leer el archivo Excel usando pandas
    df = pd.read_excel(archivo_a_cargar)

    # Contador para rastrear las filas procesadas
    filas_procesadas = 0

    # Insertar los datos en la tabla
    for _, row in df.iterrows():
        cursor.execute(f"INSERT INTO {nombre_tabla} ("
                       "NumeroDeParte, NPLimpio, DescripcionSAP, "
                       "HTSSiemens2020NICo, HTSSiemens2022NICo, "
                       "DescripcionSiemens, ValidacionHTS2020, "
                       "ValidacionHTS2022"
                       ") VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       str(row['Numero de Parte']), str(row['NP Limpio']), str(row['Descripcion SAP']),
                       str(row['HTS Siemens 2020+NICo']), str(row['HTS Siemens 2022+NICo']),
                       str(row['Descripcion Siemens']), str(row['Validacion HTS 2020']),
                       str(row['Validacion HTS 2022']))
        conn.commit()

        filas_procesadas += 1

    print(f"Total de filas procesadas: {filas_procesadas}")

    print(f"Datos del archivo Excel cargados exitosamente en la tabla '{nombre_tabla}'.")

except Exception as e:
    print(f"Error al cargar los datos del archivo Excel en la tabla: {str(e)}")

finally:
    conn.close()
