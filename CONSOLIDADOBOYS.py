from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time


def login_to_website(url, data_frame):
    driver = webdriver.Chrome(ubicacion)  # Ruta al ChromeDriver
    driver.get(url)

    for index, row in data_frame.iterrows():
        time.sleep(3)

        # Ubica el boton antes de ingresar credenciales pre-login
        login_button1 = driver.find_element_by_id("btn-login")
        login_button1.click()
        time.sleep(3)

        # Ubica los botones de usuarios, contraseña e ingresar. Pobla los dos primeros y da clic en el ultimo
        username_input = driver.find_element_by_id("user")
        password_input = driver.find_element_by_id("password")
        login_button2 = driver.find_element_by_id("ingresar-btn")
        username_input.send_keys(row['Username'])  # 'Username' es el nombre de la columna en el archivo Excel
        password_input.send_keys(row['Password'])  # 'Password' es el nombre de la columna en el archivo Excel
        driver.implicitly_wait(3)
        login_button2.click()
        driver.implicitly_wait(3)

        # Espera adicional si es necesario para la carga o verificación de la página después del inicio de sesión
        time.sleep(3)

        # Buscar el boton de mostrar opciones y dar clic
        hideshow_input = driver.find_element_by_id("hideshow")
        hideshow_input.click()
        time.sleep(3)

        # Ingresar al apartado de pedimento/exp legal y dar clic
        explegal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//h3[a[text()="Pedimento/Exp Legal"]]')))
        explegal.click()

        # Ingresar al apartado de consolidados y dar clic
        consolidados = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="ui-menuitem-text" and text()="Pagados"]')))
        consolidados.click()

        # Espera hasta que el campo PATENTE esté presente y sea visible
        campo_patente = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "findForm:parPatente")))

        # Limpiar el campo ADUANA de texto
        campo_patente.clear()

        # Espera hasta que el campo ADUANA esté presente y sea visible
        campo_aduana = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "findForm:parAduana")))

        # Limpiar el campo ADUANA de texto
        campo_aduana.clear()

        # Espera hasta que el campo SECCION esté presente y sea visible
        campo_par = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "findForm:parSeccion")))

        # Limpiar el campo SECCION de texto
        campo_par.clear()

        # Espera hasta que el botón BUSCAR esté presente y sea clickeable
        boton_buscar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "findForm:j_idt97")))

        # Hacer clic en el botón BUSCAR
        boton_buscar.click()

        # Ubicar fecha inicial y fecha final para limpiarlas

        fecha_inicial = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'findForm:parFechaInicial_input'))
        )

        fecha_inicial.clear()

        fecha_inicial.send_keys('01/01/2022')

        fecha_final = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'findForm:parFechaFinal_input'))
        )

        fecha_final.clear()

        fecha_final.send_keys('01/01/2023')

        # Esperar a que el elemento SELECCIONAR TODA LAS COLUMNAS esté presente y sea clickeable
        elemento_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ui-chkbox-icon ui-icon ui-icon-blank ui-c']")))

        # Hacer clic en el elemento SELECCIONAR TODA LAS COLUMNAS
        elemento_span.click()

        # Esperar a que el botón DESCARGAR esté presente y sea clickeable
        boton_descarga1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "listForm:pedimentos:downloadBtn")))

        # Hacer clic en el botón de DESCARGAR
        boton_descarga1.click()

        # Esperar a que el botón DESCARGAR esté presente y sea clickeable
        boton_descarga2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "downloadForm:j_idt297")))

        # Hacer clic en el botón de DESCARGAR
        boton_descarga2.click()

        # Esperar a que el elemento X esté presente y sea clickeable
        elemento_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Close']")))

        # Hacer clic en el elemento X
        elemento_close.click()

        # LogOut por cada usuario. Ubica el boton y da clic
        logout_button = driver.find_element_by_css_selector(".ui-button-icon-left.ui-icon.ui-c.fa.fa-power-off")
        logout_button.click()

        # Regresar a la página de inicio para el próximo inicio de sesión
        driver.get(url)


    # Cerrar el navegador al finalizar
    driver.quit()

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
    excel_file = config['excel_file']

    # Lee el archivo Excel y crea un DataFrame
    excel_data = pd.read_excel(excel_file)

    # Llama a la función para iniciar sesión con los datos del DataFrame
    login_to_website(website_url, excel_data)
