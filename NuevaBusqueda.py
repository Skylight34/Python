from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Declaramos el valor de servicio con la ubicacion de nuestro webdriver
service = Service(executable_path="C:\\WebDrivers\\chromedriver.exe")

#Declaramos nuestro navegador y damos el servicio para usarlo
driver = webdriver.Chrome(service=service)

#M A X I M I Z A R para suprema eficiencia
driver.maximize_window()

#Sitio a evaluar
driver.get("https://www.google.com/search?q=1")

#Localizamos el logo y la barra de busqueda por sus clases
logo = driver.find_element(By.CLASS_NAME, "jfN4p")
search = driver.find_element(By.CLASS_NAME, "gLFyf")

#Checar si el logo de la esquina superior izquierda y la barra de busqueda estan visibles
if logo.is_displayed():
    if search.is_displayed():
        print("Elementos visibles")

#Lo que queremos buscar
Query = "Trabajo"

#Limpiamos la barra de busqueda
action = ActionChains(driver)
action.click(search)
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
action.send_keys(Keys.BACKSPACE)
action.send_keys(Query)
action.perform()

#Checar si lo que buscamos se encuentran resultados
Resultados = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']//h3")
is_search_query_present = any(Query.lower() in result.text.lower() for result in Resultados)
print("Search query present:", is_search_query_present)


#Checar que no haya un dummy en la barra de busqueda
is_placeholder_present = "placeholder" in search.get_attribute("outerHTML")
print("Placeholder present:", not is_placeholder_present)

# Cerrar el driver
driver.quit()
