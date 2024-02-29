from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor

def login_and_operations(url, username, password, ubicacion, excel_info):
    driver = webdriver.Chrome(ubicacion)
    driver.get(url)

    # Resto del código de inicio de sesión y operaciones...
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
    element_h3 = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h3[contains(@class, 'ui-panelmenu-header') and contains(., 'Seguridad')]")))
    element_h3.click()
    time.sleep(3)

    # Buscar el boton de Usuarios y dar clic
    users_element = driver.find_element_by_xpath("//span[@class='ui-menuitem-text' and contains(text(),'Usuarios')]")
    users_element.click()
    time.sleep(3)

    # Ubicamos boton de agregar y damos clic
    add_button = driver.find_element_by_id("listForm:j_idt97:addBtn")
    add_button.click()
    time.sleep(3)
    iterador = 0
    for index, row in excel_info.iterrows():
        if iterador == 0:
            try:
                # Ubicar y llenar los campos con los valores del DataFrame
                nombre_input = driver.find_element_by_id("createUsuarioForm:nombre")
                correo_input = driver.find_element_by_id("createUsuarioForm:correoElectronico")
                usuario_input = driver.find_element_by_id("createUsuarioForm:usuario")
                contrasena_input = driver.find_element_by_id("createUsuarioForm:password")

                # Usar los valores del DataFrame para llenar los campos
                nombre_input.send_keys(row['Nombre'])
                correo_input.send_keys(row['Correo'])
                usuario_input.send_keys(row['Usuario'])
                contrasena_input.send_keys(row['Contrasena'])

                # Poblar pestañas
                # Tipo de usuario
                # Hacer clic en el formulario para desplegar las opciones
                # Encontrar y hacer clic en el label para abrir el menú desplegable
                label1 = driver.find_element_by_id("createUsuarioForm:tipoUsuario_label")
                label1.click()

                # Esperar a que aparezca la lista de opciones
                wait = WebDriverWait(driver, 10)
                option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:tipoUsuario_1")))

                # Hacer clic en la opción deseada (CLIENTE)
                option.click()

                # Cliente/Grupo
                # Encontrar y hacer clic en el label para abrir el menú desplegable
                label2 = driver.find_element_by_id("createUsuarioForm:listCliente_label")
                label2.click()

                # Esperar a que aparezca la lista de opciones
                wait = WebDriverWait(driver, 10)
                option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:listCliente_1")))

                # Hacer clic en la opción deseada (" SHANGHAI RESOURCES SA DE CV")
                option.click()

                # Rol
                # Hacer clic en el formulario para desplegar las opciones
                # Encontrar y hacer clic en el label para abrir el menú desplegable
                label3 = driver.find_element_by_id("createUsuarioForm:rol_label")
                label3.click()

                # Esperar a que aparezca la lista de opciones
                wait = WebDriverWait(driver, 10)
                option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:rol_10")))

                # Hacer clic en la opción deseada (CLIENTE)
                option.click()

                # Idioma
                # Encontrar y hacer clic en el label para abrir el menú desplegable
                label4 = driver.find_element_by_id("createUsuarioForm:locale_label")
                label4.click()

                # Esperar a que aparezca la lista de opciones
                wait = WebDriverWait(driver, 10)
                option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:locale_2")))

                # Hacer clic en la opción deseada (" SHANGHAI RESOURCES SA DE CV")
                option.click()
                time.sleep(3)

                # Ubicar el boton de Guardar y dar clic
                button_element = driver.find_element_by_id("createUsuarioForm:j_idt219")
                button_element.click()
                time.sleep(3)

                iterador = iterador + 1

            except Exception as e:
                print(f"Se produjo un error: {str(e)}")
                # Aquí puedes realizar acciones específicas en caso de error, como capturar el error, tomar una captura de pantalla, etc.
                # Por ejemplo, podrías tomar una captura de pantalla:
                print("ERROR PAPA 1")
        else:
            # Ubicamos boton de agregar y damos clic
            add_button = driver.find_element_by_id("listForm:j_idt97:addBtn")
            add_button.click()
            time.sleep(3)

            # Ubicar y llenar los campos con los valores del DataFrame
            nombre_input = driver.find_element_by_id("createUsuarioForm:nombre")
            correo_input = driver.find_element_by_id("createUsuarioForm:correoElectronico")
            usuario_input = driver.find_element_by_id("createUsuarioForm:usuario")
            contrasena_input = driver.find_element_by_id("createUsuarioForm:password")

            # Usar los valores del DataFrame para llenar los campos
            nombre_input.send_keys(row['Nombre'])
            correo_input.send_keys(row['Correo'])
            usuario_input.send_keys(row['Usuario'])
            contrasena_input.send_keys(row['Contrasena'])

            # Poblar pestañas
            # Tipo de usuario
            # Hacer clic en el formulario para desplegar las opciones
            # Encontrar y hacer clic en el label para abrir el menú desplegable
            label1 = driver.find_element_by_id("createUsuarioForm:tipoUsuario_label")
            label1.click()

            # Esperar a que aparezca la lista de opciones
            wait = WebDriverWait(driver, 10)
            option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:tipoUsuario_1")))

            # Hacer clic en la opción deseada (CLIENTE)
            option.click()

            # Cliente/Grupo
            # Encontrar y hacer clic en el label para abrir el menú desplegable
            label2 = driver.find_element_by_id("createUsuarioForm:listCliente_label")
            label2.click()

            # Esperar a que aparezca la lista de opciones
            wait = WebDriverWait(driver, 10)
            option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:listCliente_1")))

            # Hacer clic en la opción deseada (" SHANGHAI RESOURCES SA DE CV")
            option.click()

            # Rol
            # Hacer clic en el formulario para desplegar las opciones
            # Encontrar y hacer clic en el label para abrir el menú desplegable
            label3 = driver.find_element_by_id("createUsuarioForm:rol_label")
            label3.click()

            # Esperar a que aparezca la lista de opciones
            wait = WebDriverWait(driver, 10)
            option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:rol_10")))

            # Hacer clic en la opción deseada (CLIENTE)
            option.click()

            # Idioma
            # Encontrar y hacer clic en el label para abrir el menú desplegable
            label4 = driver.find_element_by_id("createUsuarioForm:locale_label")
            label4.click()

            # Esperar a que aparezca la lista de opciones
            wait = WebDriverWait(driver, 10)
            option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:locale_2")))

            # Hacer clic en la opción deseada (" SHANGHAI RESOURCES SA DE CV")
            option.click()

            # Ubicar el boton de Guardar y dar clic
            button_element = driver.find_element_by_id("createUsuarioForm:j_idt219")
            button_element.click()
            time.sleep(3)

    # Ubicar el elemento del botón Logout
    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-button-icon-left.ui-icon.ui-c.fa.fa-power-off")))
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
    config_file = 'C:\\Users\\atrasfi\Downloads\chromedriver-win64\chromedriver-win64/Config.txt'

    config = read_config_from_txt(config_file)

    ubicacion = config['ubicacion']
    website_url = config['website_url']
    admin = config['excel_file']
    data = config['datos']

    excel_data = pd.read_excel(admin)
    excel_info = pd.read_excel(data)

    # Lista para almacenar los procesos de inicio de sesión
    login_processes = []

    with ThreadPoolExecutor(max_workers=len(excel_data)) as executor:
        for index, row in excel_data.iterrows():
            username = row['Username']
            password = row['Password']
            login_processes.append(
                executor.submit(login_and_operations, website_url, username, password, ubicacion, excel_info.iloc[[index]])
            )

    # Espera a que todos los procesos de inicio de sesión finalicen
    for process in login_processes:
        process.result()
