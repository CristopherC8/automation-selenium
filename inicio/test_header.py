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
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Cambiar a otro navegador si es necesario
        cls.driver.maximize_window()
        cls.driver.get("https://ef-storefront-web.enviaflores.com/")  # Reemplazar con la URL de prueba

    def test_header_elements(self):
        # Esperar a que el encabezado esté presente en el DOM
        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div"))
        )
        # Verificar que el encabezado no sea None
        self.assertIsNotNone(header, "El encabezado no está presente en la página")
        # Verificar que el encabezado tenga el color de fondo correcto

    def test_boton_carrito(self):
        time.sleep(1)
        # Esperar a que el botón de carrito esté presente y hacer clic
        boton_carrito = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[4]"))
        )
        boton_carrito.click()

        # Esperar a que el carrito esté visible
        carrito = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='v-menu-33']/div/div"))
        )
        self.assertIsNotNone(carrito, "El carrito no está visible después de hacer clic en el botón")
        self.driver.save_screenshot("inicio/screenshots/carrito2.png")

        # Esperar a que el botón de cerrar esté presente y hacer clic
        boton_cerrar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-33']/div/div/div[1]/button/span[3]/i"))
        )
        boton_cerrar.click()

    def test_boton_perfil(self):
        # Esperar a que el botón de perfil sea clickeable y hacer clic
        boton_perfil = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[3]"))
        )
        boton_perfil.click()

        # Esperar a que el menú de perfil sea visible
        menu_perfil = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='v-menu-4']/div/div"))
        )
        self.assertIsNotNone(menu_perfil, "El menú de perfil no está visible después de hacer clic en el botón")

    def test_crear_cuenta(self):
        # Esperar a que el botón de crear cuenta esté presente y hacer clic
        boton_crear_cuenta = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-4']/div/div/div[2]"))
        )
        boton_crear_cuenta.click()

        # Esperar a que el formulario de creación de cuenta esté visible
        formulario_crear_cuenta = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]"))
        )
        self.assertIsNotNone(formulario_crear_cuenta, "El formulario de creación de cuenta no está visible después de hacer clic en el botón")

        # Esperar a que el botón de cerrar esté presente y hacer clic
        boton_cerrar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/button"))
        )
        boton_cerrar.click()

    def test_iniciar_sesion(self):
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
        self.assertIsNotNone(formulario_inicio_sesion, "El formulario de inicio de sesión no está visible después de hacer clic en el botón")

        # Esperar a que el botón de cerrar esté presente y hacer clic
        boton_cerrar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/button"))
        )
        boton_cerrar.click()
   
    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar las pruebas
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()