from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import random
import math
import datetime


def login_to_website(url, data_frame):
    # Ruta al ChromeDriver
    driver = webdriver.Chrome(ubicacion)
    driver.get(url)

    time.sleep(3)
    # La pantalla principal tiene un boton que hay que ubicar y dar clic
    # Lo ubicamos por ID
    login_button1 = driver.find_element_by_id("btn-login")
    login_button1.click()
    time.sleep(3)

    # La siguiente pantalla tiene tres botones que tenemos que ubicar
    username_input = driver.find_element_by_id("user")
    password_input = driver.find_element_by_id("password")
    login_button2 = driver.find_element_by_id("ingresar-btn")

    # Usuarios para generar reportes
    # En la ubicacion que ya tenemos ingresamos los datos del usuario admin que tenemos
    username_input.send_keys(excel_data.iloc[0]['Username'])
    password_input.send_keys(excel_data.iloc[0]['Password'])

    # Damos clic en el boton de login
    driver.implicitly_wait(3)
    login_button2.click()
    driver.implicitly_wait(3)

    # Espera adicional si es necesario para la carga o verificación de la página después del inicio de sesión
    time.sleep(3)

    # Buscar el boton de mostrar opciones y dar clic
    hideshow_input = driver.find_element_by_id("hideshow")
    hideshow_input.click()
    time.sleep(3)

    # Generar un número aleatorio entre 0 y 164 y se lo asigna al id del boton
    # 164 es el total de reportes que tiene la pagina
    # Agregamos un listado, ya que los reportes de anexo 24 son prioritarios
    # Esto es para evaluar todos los reportes
    # numerodereporte = random.randint(0, 165)

    numerodereporte = random.randint(0, 31)
    # Numero de reporte en especifico que se quiera probar
    # Tome en cuenta que los filtrados por nombre cambian el numero
    # numerodereporte = 29
    id_del_boton = f"reporteForm:dtReportes:{numerodereporte}:ReporteAnexoExpoBtn"

    # Cada pagina de reportes tiene 29 por pestaña
    # Esto hace que el paginado exista siempre y cuando el filtrado sea de mas de 29
    # Esto agrega una segunda/tercera/cuarta... pagina para el 30/60/90...

    paginareporte = math.ceil(numerodereporte / 29)
    paginado = f"//a[@class='ui-paginator-page ui-state-default ui-corner-all' and text()='{paginareporte}']"

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
    # De aqui en adelante se agrega esta parte de limpiar
    # Ya que muchos de los elementos/cookies se mantienen en el sitio de manera aleatoria
    # Limpiar cualquier texto existente en el campo
    input_cliente.clear()

    # Escribir "100141" en el campo
    input_cliente.send_keys("009687")

    # Esperar hasta que el elemento esté presente y visible
    try:
        label_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "reporteForm:cCliente_label"))
        )
        label_element.click()
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(3)


    # Ubica el elemento por su ID
    input_fechai = driver.find_element_by_id("reporteForm:cFechaI_input")
    # O puedes usar find_element_by_name para ubicar por el atributo name:
    # input_fecha = driver.find_element_by_name("reporteForm:cFechaI_input")
    # Limpiar cualquier texto existente en el campo
    input_fechai.clear()

    # Escribir "01/01/2023" en el campo
    input_fechai.send_keys("01/01/2022")

    # Ubicar por ID
    input_fechaf = driver.find_element_by_id("reporteForm:cFechaF_input")
    # O puedes usar find_element_by_name para ubicar por el atributo name:
    # input_fecha_fin = driver.find_element_by_name("reporteForm:cFechaF_input")
    # Limpiar cualquier texto existente en el campo
    input_fechaf.clear()

    # Escribir "01/10/2023" en el campo
    input_fechaf.send_keys("01/01/2023")

    time.sleep(3)

    # Encontrar el campo de filtro por su ID
    campo_filtro = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'reporteForm:dtReportes:j_idt67:filter'))
    )
    # Limpiar el campo (opcional, dependiendo del caso)
    campo_filtro.clear()

    # Escribir "anexo 24" en el campo de filtro
    campo_filtro.send_keys("anexo")
    campo_filtro.click()

    try:
        if paginareporte > 1:
            # Espera hasta que el elemento esté presente y visible
            paginados = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, paginado)))
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
    contenedor_toolbar = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'downloadForm:j_idt76')))
    print(numerodereporte)
    # Encontrar de nuevo el botón dentro del contenedor
    # Reemplaza con el ID correcto del botón
    try:
        boton_descarga = contenedor_toolbar.find_element(By.ID, 'downloadForm:j_idt77')
        boton_descarga.click()
        time.sleep(10)
    except Exception as e:
        print(f"Hubo un error: {e}")
        pass
        # Aquí podrías agregar acciones para manejar el error, como registrar, tomar una captura de pantalla, etc.

    # Registro de la ejecución
    with open(registro, 'a') as file:
        now = datetime.datetime.now()
        reporte_ejecutado = f"Reporte solicitado: {numerodereporte}, Fecha y hora: {now}\n"
        file.write(reporte_ejecutado)

    time.sleep(5)

    # Ubicar por ID
    button_element_download = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'downloadForm:j_idt79'))
    )

    # Hacer clic en el elemento de descarga
    button_element_download.click()

    # Esperar un tiempo para que la descarga se complete
    time.sleep(10)

    # Ubicar el elemento del botón Logout
    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-button-icon-left.ui-icon.ui-c.fa.fa-power-off")))
    # Desplazarse hasta el botón Logout
    driver.execute_script("arguments[0].scrollIntoView();", logout_button)

    time.sleep(5)


def read_config_from_txt(file_path):
    with open(file_path, 'r') as file:
        config = {}
        for line in file:
            key, value = line.strip().split(': ')
            config[key] = value
    return config


if __name__ == "__main__":
    # Ruta al archivo de configuración
    config_file = 'C:\\Users\\atrasfi\Downloads\chromedriver-win64\chromedriver-win64/Config.txt'

    # Lee la configuración desde el archivo txt
    config = read_config_from_txt(config_file)

    ubicacion = config['ubicacion']
    website_url = config['website_url']
    admin = config['excel_file']
    data = config['datos']
    registro = config['registro']
    reportes = config['reportes']

    # Lee el archivo Excel y crea un DataFrame
    excel_data = pd.read_excel(admin)
    excel_info = pd.read_excel(data)
    reportes_data = pd.read_excel(reportes)

    # Llama a la función para iniciar sesión con los datos del DataFrame
    login_to_website(website_url, excel_data)
