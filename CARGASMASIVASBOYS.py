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

    # Ubicar el enlace "Recibo Mercancia" por su texto
    enlace_recibo_mercancia = driver.find_element_by_xpath("//a[text()='Recibo Mercancia']")

    # Hacer clic en el enlace
    enlace_recibo_mercancia.click()

    # Esperar un momento para que la página se cargue completamente
    time.sleep(3)

    # Esperar hasta que el elemento sea interactuable (presente y visible)
    enlace_carga_masiva = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//a[@class='ui-menuitem-link ui-corner-all' and @href='/Portal/OrdenCompra/Recibo/CargaMasiva.xhtml']"))
    )

    # Hacer clic en el enlace
    enlace_carga_masiva.click()

    # Esperar un momento para que la página cargue después de hacer clic
    time.sleep(5)

    # Esperar hasta que el elemento sea interactuable (presente y visible)
    imagen_busqueda = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@src='/resources/images/dock/Search.png']"))
    )

    # Hacer clic en la imagen
    imagen_busqueda.click()

    # Esperar un momento para que la página cargue después de hacer clic
    time.sleep(5)

    # Esperar hasta que el elemento sea interactuable (presente y visible)
    enlace = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='listForm:recibos:0:j_idt271:0:j_idt272']"))
    )

    # Hacer clic en el enlace
    enlace.click()

    # Esperar un momento para que la página cargue después de hacer clic
    time.sleep(5)


    # Esperar hasta que el elemento sea interactuable (presente y visible)
    span_buscar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-button-icon-left ui-icon ui-c fa fa-search']"))
    )

    # Hacer clic en el span
    span_buscar.click()

    # Esperar un momento para que la página cargue después de hacer clic
    time.sleep(5)

    # Encontrar el elemento de entrada por su ID
    elemento_input = driver.find_element_by_id("contentForm:idRecibo")

    # Limpiar el contenido del elemento de entrada
    elemento_input.clear()

    # Esperar un momento para que la página cargue después de hacer clic
    time.sleep(5)

    # Escribir "1924849" en el elemento de entrada
    elemento_input.send_keys("1924849")


    # Esperar un momento para que la página cargue después de hacer clic
    time.sleep(5)

    # Hacer clic en el span
    span_buscar.click()







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
