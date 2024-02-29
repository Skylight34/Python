from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def login_to_website(url, data_frame):
    driver = webdriver.Chrome(ubicacion)  # Ruta al ChromeDriver
    driver.get(url)

    for index, row in excel_info.iterrows():

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

        time.sleep(3)
        login_button2.click()
        time.sleep(3)

        # Espera adicional si es necesario para la carga o verificación de la página después del inicio de sesión
        time.sleep(3)

        # Buscar el boton de mostrar opciones y dar clic
        hideshow_input = driver.find_element_by_id("hideshow")
        hideshow_input.click()
        time.sleep(3)

        try:
            # Esperar hasta que el elemento SEGURIDAD esté presente en el DOM
            seguridad = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h3[contains(@class, 'ui-panelmenu-header') and contains(., 'Seguridad')]")
                )
            )
            # Obtener el valor del atributo aria-expanded
            aria_expanded = seguridad.get_attribute("aria-expanded")

            if aria_expanded == "true":
                # Si aria-expanded es true, hacer algo
                print("El elemento 'Seguridad' está expandido. Realizando una acción...")

                # Por ejemplo, hacer algo específico si el elemento está expandido

            else:
                # Si aria-expanded no es true, hacer otra cosa
                print("El elemento 'Seguridad' está colapsado. Realizando otra acción...")

                # Por ejemplo, hacer algo específico si el elemento está colapsado
                seguridad.click()
                time.sleep(3)

        except Exception as e:
            print(f"Se produjo un error: {str(e)}")
            # Manejar el error si es necesario

        try:
            # Esperar hasta que el elemento USUARIOS presente en el DOM
            users_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[@class='ui-menuitem-text' and contains(text(),'Usuarios')]"))
            )
            # Esperar hasta que el elemento USUARIOS sea clickeable
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[@class='ui-menuitem-text' and contains(text(),'Usuarios')]"))
            )
            # Hacer clic en el elemento USUARIOS
            users_element.click()
            time.sleep(3)
        except Exception as e:
            print(f"Se produjo un error: {str(e)}")
            # Aquí puedes realizar acciones específicas en caso de error, como capturar el error, tomar una captura de pantalla, etc.
            # Por ejemplo, podrías tomar una captura de pantalla:
            print("ERROR")

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

        # Esperar a que aparezca la lista de opciones y hacer clic en TIPO CLIENTE
        wait = WebDriverWait(driver, 10)
        option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:tipoUsuario_1")))

        option.click()

        # Cliente/Grupo
        # Encontrar y hacer clic en el label para abrir el menú desplegable
        wait = WebDriverWait(driver, 10)
        label2 = wait.until(EC.element_to_be_clickable((By.ID, "createUsuarioForm:listCliente_label")))
        label2.click()

        # Esperar a que aparezca la lista de opciones.
        wait = WebDriverWait(driver, 10)
        option = wait.until(EC.presence_of_element_located((By.ID, "createUsuarioForm:listCliente_288")))

        # Hacer clic en la opción deseada ("EATON TRUCK COMPONENTES S DE RL DE CV (SLP 2038)")
        # El numero cambia por cliente del 1 al 1154 (al 12 DIC 2023)
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
        # El numero de rol depende de la seleccion, checar el que quieramos
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

        # Ubicar el elemento del botón Logout
        logout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.ui-button-icon-left.ui-icon.ui-c.fa.fa-power-off")))

        # Desplazarse hasta el botón Logout y dar clic
        driver.execute_script("arguments[0].scrollIntoView();", logout_button)

        logout_button.click()


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
    admin = config['admin']
    data = config['datos']

    # Lee el archivo Excel y crea un DataFrame
    excel_data = pd.read_excel(admin)
    excel_info = pd.read_excel(data)

    # Llama a la función para iniciar sesión con los datos del DataFrame
    login_to_website(website_url, excel_data)