from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time


def login_to_website(url, data_frame):
    driver = webdriver.Chrome(ubicacion)  # Ruta al ChromeDriver
    driver.get(url)


    time.sleep(3)
    login_button1 = driver.find_element_by_id("btn-login")
    login_button1.click()
    time.sleep(3)

    username_input = driver.find_element_by_id("user")
    password_input = driver.find_element_by_id("password")
    login_button2 = driver.find_element_by_id("ingresar-btn")

    # Usuario Admin
    username_input.send_keys(excel_data.iloc[0]['Username'])
    password_input.send_keys(excel_data.iloc[0]['Password'])

    driver.implicitly_wait(3)
    login_button2.click()
    driver.implicitly_wait(3)

    # Espera adicional si es necesario para la carga o verificación de la página después del inicio de sesión
    time.sleep(3)

    # Buscar el boton de mostrar opciones y dar clic
    hideshow_input = driver.find_element_by_id("hideshow")
    hideshow_input.click()
    time.sleep(3)

    # Buscar el boton de Seguridad y dar clic
    wait = WebDriverWait(driver, 10)
    element_h3 = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(@class, 'ui-panelmenu-header') and contains(., 'Seguridad')]")))
    element_h3.click()
    time.sleep(3)

    # Buscar el boton de Usuarios y dar clic
    users_element = driver.find_element_by_xpath("//span[@class='ui-menuitem-text' and contains(text(),'Usuarios')]")
    users_element.click()
    time.sleep(3)
    iterador = 0

    for index, row in excel_info.iterrows():
        if iterador == 0:
            # Ubicar y llenar el campo con los valores del DataFrame
            correo_input = driver.find_element_by_id("contentForm:parCorreo")

            # Usar los valores del DataFrame para llenar el campo
            correo_input.send_keys(row['Correo'])
            time.sleep(5)

            # Encuentra el botón BUSCAR por su ID
            boton_buscar = driver.find_element_by_id("contentForm:j_idt95")
            time.sleep(5)


            # Haz clic en el botón para buscar
            boton_buscar.click()
            time.sleep(5)

            # Ubica el elemento tr deseado por su atributo data-ri (o cualquier otro)
            element = driver.find_element_by_xpath("//tr[@data-ri='0']")
            time.sleep(5)

            # Crea una instancia de ActionChains
            actions = ActionChains(driver)

            # Realiza doble clic en el elemento
            actions.double_click(element).perform()
            time.sleep(5)

            # Encuentra el elemento por su ID
            element = driver.find_element_by_id("editUsuarioForm:activo")
            time.sleep(5)

            # Haz clic para cambiar su estado
            element.click()
            time.sleep(5)

            # Encuentra el botón GUARDAR por su ID
            boton_guardar = driver.find_element_by_id("editUsuarioForm:j_idt288")

            # Haz clic en el botón para guardar
            boton_guardar.click()

            iterador = iterador + 1

            # Limpiar campo para ingresar lo que sigue
            correo_input.clear()
            time.sleep(5)
        else:

            time.sleep(5)
            # Ubicar y llenar el campo con los valores del DataFrame
            correo_input = driver.find_element_by_id("contentForm:parCorreo")
            time.sleep(5)

            # Usar los valores del DataFrame para llenar el campo
            correo_input.send_keys(row['Correo'])
            time.sleep(5)

            # Encuentra el botón BUSCAR por su ID
            boton_buscar = driver.find_element_by_id("contentForm:j_idt95")
            time.sleep(5)

            # Haz clic en el botón para buscar
            boton_buscar.click()
            time.sleep(5)


            # Ubica el elemento tr deseado por su atributo data-ri (o cualquier otro)
            element = driver.find_element_by_xpath("//tr[@data-ri='0']")
            time.sleep(5)

            # Crea una instancia de ActionChains
            actions = ActionChains(driver)

            # Realiza doble clic en el elemento
            actions.double_click(element).perform()
            time.sleep(5)

            # Encuentra el elemento por su ID
            element = driver.find_element_by_id("editUsuarioForm:activo")
            time.sleep(5)

            # Haz clic para cambiar su estado
            element.click()
            time.sleep(5)

            # Encuentra el botón GUARDAR por su ID
            boton_guardar = driver.find_element_by_id("editUsuarioForm:j_idt288")

            # Haz clic en el botón para guardar
            boton_guardar.click()


    # Ubicar el elemento del botón Logout
    logout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-button-icon-left.ui-icon.ui-c.fa.fa-power-off")))
    # Desplazarse hasta el botón Logout
    driver.execute_script("arguments[0].scrollIntoView();", logout_button)


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

    # Lee el archivo Excel y crea un DataFrame
    excel_data = pd.read_excel(admin)
    excel_info = pd.read_excel(data)

    # Llama a la función para iniciar sesión con los datos del DataFrame
    login_to_website(website_url, excel_data)
