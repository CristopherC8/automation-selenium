from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestHeader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración inicial del navegador
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get("https://ef-storefront-web.enviaflores.com/")

    def test_01_header_elements(self):
        # Esperar a que el encabezado esté presente en el DOM
        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div"))
        )
        
        # Screenshot del encabezado
        header.screenshot("inicio/screenshots/header.png")

    def test_02_buscar(self):
        # Esperar a que el botón de buscar sea clickeable y hacer clic
        boton_buscar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/div/div/div"))
        )
        boton_buscar.click()

        # Screenshot del formulario de búsqueda
        boton_buscar.screenshot("screenshots/header/buscar.png")

    def test_03_idioma_moneda(self):
        # Esperar a que el botón de idioma y moneda sea clickeable y hacer clic
        boton_idioma_moneda = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[1]"))
        )
        boton_idioma_moneda.click()

        # Esperar a que el menú de idioma y moneda sea visible
        menu_idioma_moneda = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='v-menu-1']/div"))
        )

        # Screenshot del menú de idioma y moneda
        menu_idioma_moneda.screenshot("screenshots/header/idioma_moneda.png")

    def test_04_boton_perfil(self):
        # Esperar a que el botón de perfil sea clickeable y hacer clic
        boton_perfil = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[3]"))
        )
        boton_perfil.click()

        # Esperar a que el menú de perfil sea visible
        menu_perfil = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='v-menu-4']/div/div"))
        )

        # Screenshot del menú de perfil
        menu_perfil.screenshot("screenshots/header/perfil.png")

    def test_05_crear_cuenta(self):
        # Esperar a que el botón de crear cuenta esté presente y hacer clic
        boton_crear_cuenta = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-4']/div/div/div[2]"))
        )
        boton_crear_cuenta.click()

        # Esperar a que el formulario de creación de cuenta esté visible
        formulario_crear_cuenta = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]"))
        )

        # Screenshot del formulario de creación de cuenta
        formulario_crear_cuenta.screenshot("screenshots/header/crear_cuenta.png")

        # Esperar a que el botón de cerrar esté presente y hacer clic
        boton_cerrar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/button"))
        )
        boton_cerrar.click()

    def test_06_iniciar_sesion(self):
        # Esperar a que el botón de perfil sea clickeable y hacer clic
        boton_perfil = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[3]"))
        )
        boton_perfil.click()

        # Esperar a que el botón de iniciar sesión esté presente y hacer clic
        boton_iniciar_sesion = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-4']/div/div/div[1]"))
        )
        boton_iniciar_sesion.click()

        # Esperar a que el formulario de inicio de sesión esté visible
        formulario_inicio_sesion = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]"))
        )

        # Screenshot del formulario de inicio de sesión
        formulario_inicio_sesion.screenshot("screenshots/header/iniciar_sesion.png")

        # Esperar a que el botón de cerrar esté presente y hacer clic
        boton_cerrar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/button"))
        )
        boton_cerrar.click()

    def test_07_boton_carrito(self):
        # Esperar a que el botón de carrito esté presente y hacer clic
        boton_carrito = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[4]"))
        )
        boton_carrito.click()

        # Esperar a que el carrito esté visible
        carrito = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='v-menu-33']/div/div"))
        )

        # Screenshot del carrito
        carrito.screenshot("screenshots/header/carrito.png")

        # Esperar a que el botón de cerrar esté presente y hacer clic
        boton_cerrar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-33']/div/div/div[1]/button/span[3]/i"))
        )
        boton_cerrar.click()
   
    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar las pruebas
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()