#AGREGAR LIBRERIAS
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
	from_field = (By.ID, 'from')
	to_field = (By.ID, 'to')
	call_taxi_button = (By.XPATH, '//button[has(text(), "Call a taxi")]')
# Reemplazar has por CONTAINS algo asi call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')

	tariff_cards = (By.CLASS_NAMED, 'tariff-cards')
# correccion CLASS_NAME

	supportive_plan_card = (By.XPATH, 'div[@class="tcard"]//div[contains(text(), "Supportive")]')
# Debe empezar con //, si queremos evaluar dos o mas elementos agregar la comparativa AND con la misma sintaxis inicial
# Quedaria algo asi //div[@class="tcard"]//div[contains(text(), "Supportive")]
# Y aplicando el criterio AND //div[@class="tcard"] and [@text="Supportive"]


	def __init__(driver):
		self.driver = driver
#Hay que autollamarse def __init__(self,driver)


	def set_from(self, from_address):
		self.driver.find_element(*self.from_field).send_keys(from_address)


	def set_to(self, to_address):
		self.driver.find_elements(*self.to_field).send_keys(to_address)
#

	def get_from(self):
		return self.driver.find_element(*self.from_field).get_property('value')


	def get_to(self):
		return self.driver.find_element(*self.to_field).get_property('value')


	def click_call_taxi_button(self):
		WebDriverWait(self.driver,"3").until(expected_conditions.visibility_of_element_located(call_taxi_button))
		self.driver.find_element(*call_taxi_button).click()


	def set_route(self, from_address, to_address):
		self.set_from(from_address)
		self.set_to(to_address)
		self.click_call_taxi_button()


	def select_supportive_plan(self):
		card = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.supportive_plan_card))
		driver.execute_script("arguments[0].scrollIntoView();", card)
		card.click().click()
	#Cambiar expected_conditions por EC de la libreria
	#Agregar self al driver para llamarse
	#Doble click? typo?
