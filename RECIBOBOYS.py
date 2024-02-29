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

    # Find the link with the text "Recibo Mercancia"
    link = driver.find_element_by_link_text("Recibo Mercancia")

    # Click on the link
    link.click()
    time.sleep(3)

    # Find the link with the text "Recibo"
    link = driver.find_element_by_link_text("Recibo")

    # Click on the link
    link.click()
    time.sleep(3)

    # Find the element by its XPath and click on it
    element = driver.find_element_by_xpath("//img[@src='/resources/images/dock/FolderDoc.png']")
    element.click()
    time.sleep(3)

    # Encontrar el elemento por su ID (o cualquier otro selector que funcione)
    elemento = driver.find_element(By.ID, "contentForm:bodega_label")

    # Obtener el texto del elemento
    texto_elemento = elemento.text

    # Verificar si el texto contiene "UBER FREIGHT UF3"
    if "UBER FREIGHT UF3" in texto_elemento:
        print("El elemento contiene 'UBER FREIGHT UF3', se mantiene.")
    else:
        print("El elemento no contiene 'UBER FREIGHT UF3', se selecciona.")

    # Close the browser
    driver.quit()

    # Ubicar el elemento del botón Logout
    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-button-icon-left.ui-icon.ui-c.fa.fa-power-off")))
    # Desplazarse hasta el botón Logout
    driver.execute_script("arguments[0].scrollIntoView();", logout_button)

    # Ubicar elemento por ID
    def ubicarporID(x):
        elementoID = driver.find_element(By.ID, x)
        return elementoID

    # Ubicar elemento por XPATH
    def ubicarporXPATH(x):
        elementoXPATH = driver.find_element_by_xpath(x)
        return elementoXPATH

    # Ubicar element por TEXT
    def ubicarporTEXT(x):
        elementoTEXT = driver.find_element_by_link_text(x)
        return elementoTEXT

    # Ubicar elemento por CSS
    def ubicarporCSS(x):
        elementoTEXT = driver.find_element_by_link_text(x)
        return elementoTEXT

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
