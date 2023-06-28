from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#Declaramos el valor de servicio con la ubicacion de nuestro webdriver
service = Service(executable_path="C:\\WebDrivers\\chromedriver.exe")

#Declaramos nuestro navegador y damos el servicio para usarlo
driver = webdriver.Chrome(service=service)

#M A X I M I Z A R para suprema eficiencia
driver.maximize_window()

#Sitio a evaluar
driver.get("https://about.google/")

#Localizar headliners por clase
elements = driver.find_elements(By.CLASS_NAME, "glue-header")
for element in elements:
    print (element.text)

print("\n")

#Localizar headliners por css selector
elements = driver.find_elements(By.CSS_SELECTOR, ".glue-header")
for element in elements:
    print (element.text)

print("\n")

#Localizar headliners por xpath
elements = driver.find_elements(By.XPATH, "/html/body/header")
for element in elements:
    print (element.text)



