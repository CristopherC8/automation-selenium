from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestCalendario(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración inicial del navegador
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get("https://ef-storefront-web.enviaflores.com/")

    def verificar_calendario(self):
        # Esperar a que el componente esté presente en el DOM
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/div[3]/div/div[1]/div[3]/div"))
        )
    
    def test_01_calendario(self):
        self.verificar_calendario()
        # Screenshot del calendario
        self.driver.save_screenshot("screenshots/calendario/calendario.png")

    def test_02_hacer_click_fecha_de_entrega(self):
        # Esperar a que el botón de fecha de entrega sea clickeable y hacer clic
        boton_fecha_entrega = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div[3]/div/button"))
        )
        boton_fecha_entrega.click()

        # Screenshot del calendario
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div[3]/div/button"))
        )
        self.driver.save_screenshot("screenshots/calendario/fecha_entrega.png")
    
    def test_3_seleccionar_hoy(self):
        # Esperar a que el botón de hoy sea clickeable y hacer clic
        boton_hoy = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-39']/div/div/div/div/div[1]/button"))
        )
        boton_hoy.click()

        # Screenshot del calendario
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='v-menu-39']/div/div/div/div/div[1]/button"))
        )
        self.driver.save_screenshot("screenshots/calendario/hoy.png")

    @classmethod
    def tearDownClass(cls):
        # Cierra el navegador
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()