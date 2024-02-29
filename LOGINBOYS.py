from selenium import webdriver
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
