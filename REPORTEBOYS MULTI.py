import datetime
import math
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor


# TO DO LIST
# 1.- Diccionario de reportes para facil consulta
# 2.- Schedules para ejeccucion de reportes
# 3.- Prioridad, Severidad y Periodos/Frecuencia de ejecucion de los reportes (muy baja, baja, media, alta y muy alta)
# 4.- Log de ejecucion con mensajes de error o vacio (MAPEAR LOS ERRORES VA A SER UN CASTRE)
# 5.- 
def login_and_operations(url, username, password, ubicacion, excel_info):
    driver = webdriver.Chrome(ubicacion)  # Ruta al ChromeDriver
    driver.get(url)

    time.sleep(3)
    login_button1 = driver.find_element_by_id("btn-login")
    login_button1.click()
    time.sleep(3)

    username_input = driver.find_element_by_id("user")
    password_input = driver.find_element_by_id("password")
    login_button2 = driver.find_element_by_id("ingresar-btn")

    # Usuarios para generar reportes
    username_input.send_keys(username)
    password_input.send_keys(password)

    driver.implicitly_wait(3)
    login_button2.click()
    driver.implicitly_wait(3)

    # Generar un número aleatorio entre 0 y 164 y se lo asigna al id del boton
    # 164 es el total de reportes que tiene la pagina
    # Agregamos un listado, ya que los reportes de anexo 24 son prioritarios
    # Esto es para evaluar todos los reportes
    # numerodereporte = random.randint(0, 165)
    # Esta es una lista de reportes ya optimizados a evaluar
    # optimizados = [19,144,168,169,170,232,233,261,284,285,305,306,307,308,326,329,330]
    numerodereporteenpagina =[2,5,6,7,8,12,13,20,28,29,40,41,42,43,51,54,55]
    # longitud = len(numerodereporteenpagina)
    # numerodereporte = random.randint(0, longitud)

    # Evaluar posicion del listado de numerodereporteenpagina
    numerodereporte = 16

    # numerodereporte = random.randint(0, 31)

    # Numero de reporte en especifico que se quiera probar
    # Tome en cuenta que los filtrados por nombre cambian el numero
    # numerodereporte = 29
    id_del_boton = f"reporteForm:dtReportes:{numerodereporteenpagina[numerodereporte]}:ReporteAnexoExpoBtn"

    # Cada pagina de reportes tiene 29 por pestaña
    # Esto hace que el paginado exista siempre y cuando el filtrado sea de mas de 29
    # Esto agrega una segunda/tercera/cuarta... pagina para el 30/60/90...

    paginareporte = math.ceil(numerodereporteenpagina[numerodereporte] / 29)
    paginado = f"//a[@class='ui-paginator-page ui-state-default ui-corner-all' and text()='{paginareporte}']"

    # Registro de la ejecución
    with open(registro, 'a') as file:
        reporte_ejecutado = f"Usuario: {username}, Reporte a solicitar: {numerodereporteenpagina[numerodereporte]}\n"
        file.write(reporte_ejecutado)

    for i in numerodereporteenpagina:

        # Espera adicional si es necesario para la carga o verificación de la página después del inicio de sesión
        time.sleep(3)

        # Buscar el boton de mostrar opciones y dar clic
        hideshow_input = driver.find_element_by_id("hideshow")
        hideshow_input.click()
        time.sleep(3)

        # Buscar el menu de Reportes y dar clic
        menureportes = driver.find_element_by_xpath(
            "//h3[contains(@class, 'ui-widget ui-panelmenu-header') and .//a[contains(text(), 'Reportes')]]")
        menureportes.click()
        time.sleep(3)

        # Buscar el boton de Reportes y dar clic
        reportes = driver.find_element_by_xpath(
            "//a[@class='ui-menuitem-link ui-corner-all' and contains(@href, '/Portal/Reportes/FiltroReportes.xhtml')]")
        reportes.click()
        time.sleep(3)

        # Ubica el elemento por su ID
        input_cliente = driver.find_element_by_id("reporteForm:idCliente")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_cliente = driver.find_element_by_name("reporteForm:idCliente")

        # Limpiar cualquier texto existente en el campo
        input_cliente.clear()

        # Escribir "100141" en el campo
        input_cliente.send_keys("009687")

        # Esperar hasta que el elemento esté presente y visible
        try:
            time.sleep(3)
            label_element = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.ID, "reporteForm:cCliente_label"))
            )
            label_element.click()
        except Exception as e:
            print(f"Error: {e} 1")

        # Ubica el elemento por su ID
        input_fechai = driver.find_element_by_id("reporteForm:cFechaI_input")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_fecha = driver.find_element_by_name("reporteForm:cFechaI_input")

        # Limpiar cualquier texto existente en el campo
        input_fechai.clear()
        time.sleep(3)
        # Escribir "01/09/2023" en el campo
        input_fechai.send_keys("01/01/2023")

        # Ubicar por ID
        input_fechaf = driver.find_element_by_id("reporteForm:cFechaF_input")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_fecha_fin = driver.find_element_by_name("reporteForm:cFechaF_input")

        # Limpiar cualquier texto existente en el campo
        input_fechaf.clear()
        time.sleep(3)

        # Escribir "01/10/2023" en el campo
        input_fechaf.send_keys("06/01/2023")

        # Encontrar el campo de filtro por su ID
        campo_filtro = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'reporteForm:dtReportes:j_idt67:filter'))
        )
        # Limpiar el campo (opcional, dependiendo del caso)
        campo_filtro.clear()

        # Escribir "anexo 24" en el campo de filtro
        # campo_filtro.send_keys("anexo")
        # campo_filtro.click()

        try:
            if paginareporte > 1:

                # Espera a que el elemento sea clickeable
                paginados = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, paginado)))
                # Hacer clic en el elemento
                paginados.click()
        except NoSuchElementException:
            print("El elemento a seleccionar esta en la pagina 1 o no existe paginado.")
            # Manejar la excepción o realizar acciones correspondientes

        # Ubicar por ID random que se genero al inicio
        time.sleep(5)
        try:
            button_element1 = driver.find_element_by_id(id_del_boton)
            button_element1.click()
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el elemento: {e}")
            # Aquí puedes añadir acciones adicionales en caso de que el botón no se encuentre

        # Ubicar por ID
        # button_element2 = driver.find_element_by_id("downloadForm:j_idt77")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # button_element = driver.find_element_by_name("downloadForm:j_idt77")

        # Esperar a que el elemento contenedor esté presente
        # Reemplaza con el ID correcto del contenedor
        time.sleep(5)

        # Contar tiempo de inicio de descarga
        tiempoa = datetime.datetime.now()
        # Ubicar por ID
        button_element_download = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'downloadForm:j_idt79')))

        # Hacer clic en el elemento de descarga
        time.sleep(3)
        button_element_download.click()

        # Esperar un tiempo para que la descarga se complete
        time.sleep(10)
        print(numerodereporteenpagina[numerodereporte])
        # Encontrar de nuevo el botón dentro del contenedor
        # Reemplaza con el ID correcto del botón
        try:
            boton_descarga = button_element_download.find_element(By.ID, 'downloadForm:j_idt77')
            boton_descarga.click()
            time.sleep(10)
        except Exception as e:
            print(f"Hubo un error: {e}")
            pass
            # Aquí podrías agregar acciones para manejar el error, como registrar, tomar una captura de pantalla, etc.

        # Registro de la ejecución
        with open(registro, 'a') as file:
            now = datetime.datetime.now()
            duracion = now - tiempoa
            reporte_ejecutado = f"Usuario: {username}, Reporte solicitado: {numerodereporteenpagina[numerodereporte]},Fecha y hora: {now}, Duracion de la peticion: {duracion}\n"
            file.write(reporte_ejecutado)

        # time.sleep(5)
        # close_icon = driver.find_element(By.CLASS_NAME, "ui-icon-closethick")

        # Click on the element
        # close_icon.click()

        # time.sleep(5)

        # Ubicar el elemento del botón Logout
        # logout_button = WebDriverWait(driver, 10).until(
            # EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-button-icon-left.ui-icon.ui-c.fa.fa-power-off")))
        # Desplazarse hasta el botón Logout
        # driver.execute_script("arguments[0].scrollIntoView();", logout_button)

        # time.sleep(5)
        numerodereporte = numerodereporte +1
def read_config_from_txt(file_path):
    with open(file_path, 'r') as file:
        config = {}
        for line in file:
            key, value = line.strip().split(': ')
            config[key] = value
    return config

if __name__ == "__main__":

    config_file = 'C:\\Users\\atrasfi\Downloads\chromedriver-win64\chromedriver-win64/Config.txt'

    config = read_config_from_txt(config_file)

    ubicacion = config['ubicacion']
    website_url = config['website_url']
    admin = config['excel_file']
    data = config['datos']
    registro = config['registro']

    excel_data = pd.read_excel(admin)
    excel_info = pd.read_excel(data)

    # Lista para almacenar los procesos de inicio de sesión
    login_processes = []

    with ThreadPoolExecutor(max_workers=len(excel_data)) as executor:
        for index, row in excel_data.iterrows():
            username = row['Username']
            password = row['Password']
            login_processes.append(
                executor.submit(login_and_operations, website_url, username, password, ubicacion,
                                excel_info.iloc[[index]])
            )

            # Esperar a que todos los procesos de inicio de sesión finalicen
        for process in login_processes:
            process.result()
