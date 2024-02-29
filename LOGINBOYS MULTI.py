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
