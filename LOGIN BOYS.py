from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Suponiendo que tienes una lista de usuarios y contraseñas
users = ['user1', 'user2', 'user3']
passwords = ['pass1', 'pass2', 'pass3']

# Especificar la ruta al archivo chromedriver.exe
path_to_chromedriver = 'C:\\Users\\atrasfi\OneDrive - Uber Freight\Desktop\INSTALL'  # Reemplaza con tu ruta

# Configurar el servicio del ChromeDriver
service = Service(path_to_chromedriver)

# Iniciar el navegador (en este caso, Chrome) con la ruta del chromedriver
driver = webdriver.Chrome(service=service)

# Iterar sobre la lista de usuarios y contraseñas
for i in range(len(users)):
    driver.get("https://uatcustomsportal.transplace.com/Portal/index.xhtml")  # Reemplaza con tu URL
    time.sleep(2)  # Espera unos segundos para que la página cargue completamente

    # Encontrar campo de boton de ingresar
    try:
        btn_login = driver.find_element_by_name("btn-login")
        btn_login.click()
    except Exception as e:
        print("No se encontró el botón 'btn-login'. Se procede sin hacer clic.")

    time.sleep(3)

    # Encontrar los campos de usuario y contraseña e ingresar los datos
    username_field = driver.find_element_by_id("user")  # Reemplaza con el ID real
    password_field = driver.find_element_by_id("password")  # Reemplaza con el ID real

    username_field.send_keys(users[i])
    password_field.send_keys(passwords[i])

    # Enviar el formulario (puedes encontrar el botón de inicio de sesión y hacer click en él)
    login_button = driver.find_element_by_id("ingresar-btn")  # Reemplaza con el ID real
    login_button.click()

    time.sleep(3)  # Espera unos segundos para ver el resultado antes de continuar con el siguiente usuario

# Cerrar el navegador al finalizar
driver.quit()
