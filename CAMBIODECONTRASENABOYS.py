from selenium import webdriver
import pandas as pd
import time

cambios_completos = []  # Lista para almacenar los cambios de contraseña completados
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

        # Ubica el elemento por su ID
        input_nombre = driver.find_element_by_id("contentForm:nombre")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_nombre = driver.find_element_by_name("contentForm:nombre")

        # Limpiar cualquier texto existente en el campo
        input_nombre.clear()

        # Escribir el texto deseado en el campo
        input_nombre.send_keys(row['Username'])

        # Ubica el elemento por su ID
        input_contrasenavieja = driver.find_element_by_id("contentForm:oldPassword")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_contrasenavieja = driver.find_element_by_name("contentForm:oldPassword")

        # Limpiar cualquier texto existente en el campo
        input_contrasenavieja.clear()

        # Escribir el texto deseado en el campo
        input_contrasenavieja.send_keys(row['Password'])

        # Ubica el elemento por su ID
        input_contrasenanueva = driver.find_element_by_id("contentForm:newPassword")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_contrasenanueva = driver.find_element_by_name("contentForm:oldPassword")

        # Limpiar cualquier texto existente en el campo
        input_contrasenanueva.clear()

        # Escribir el texto deseado en el campo
        input_contrasenanueva.send_keys(row['Password']+"1")

        # Ubica el elemento por su ID
        input_contrasenanuevar = driver.find_element_by_id("contentForm:newPasswordC")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_contrasenanueva = driver.find_element_by_name("contentForm:oldPassword")

        # Limpiar cualquier texto existente en el campo
        input_contrasenanuevar.clear()

        # Escribir el texto deseado en el campo
        input_contrasenanuevar.send_keys(row['Password']+"1")

        # Ubica el elemento por su ID
        input_guardar = driver.find_element_by_id("contentForm:actualiza")
        # O puedes usar find_element_by_name para ubicar por el atributo name:
        # input_contrasenanueva = driver.find_element_by_name("contentForm:oldPassword")

        # Limpiar cualquier texto existente en el campo
        input_guardar.click()

        # Agregar a listado de usuarios con cambios ya efectuados
        cambios_completos.append({'Username': row['Username'], 'Status': 'Cambio Exitoso'})

        # Crea un DataFrame con la información de los cambios completados
    cambios_df = pd.DataFrame(cambios_completos)

    # Guarda el DataFrame con los cambios completados en un archivo Excel
    cambios_df.to_excel('C:\\Users\\atrasfi\Downloads\chromedriver-win64\chromedriver-win64CambiosdeContraseñaCompletos.xlsx', index=False)

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
    excel_file = config['datoscambio']

    # Lee el archivo Excel y crea un DataFrame
    excel_data = pd.read_excel(excel_file)

    # Llama a la función para iniciar sesión con los datos del DataFrame
    login_to_website(website_url, excel_data)

    # Crear un nuevo DataFrame con los usuarios y contraseñas nuevos
    nuevos_datos = {
        'Username': excel_data['Username'],  # Usar los mismos nombres de usuario
        'New_Password': excel_data['Password'] + "1"  # Agregar "1" a las contraseñas antiguas
    }
    excel_data2 = pd.DataFrame(nuevos_datos)

    # Guardar el nuevo DataFrame en un archivo Excel
    excel_data2.to_excel('nuevos_usuarios.xlsx', index=False)
