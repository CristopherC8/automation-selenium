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

    def verificar_header_elements(self):
         # Esperar a que el encabezado esté presente en el DOM
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div"))
        )


    def test_01_iniciar_sesion(self):
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
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]"))
        )

        # Completar el formulario de inicio de sesión
        campo_email = self.driver.find_element(By.XPATH, "//*[@id='input-44']")
        campo_email.send_keys("test@enviaflores.com")

        campo_password = self.driver.find_element(By.XPATH, "//*[@id='input-46']")
        campo_password.send_keys("2121")

        boton_enviar = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[3]/div/form/div/div[5]/button")
        boton_enviar.click()

    def test_02_header_elements(self):
        # # Esperar a que el encabezado esté presente en el DOM
        # header = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div"))
        # )
        # time.sleep(3)
        self.verificar_header_elements()
        # Screenshot del encabezado
        self.driver.save_screenshot("screenshots/header_sesion_iniciada/header.png")

    def test_03_buscar(self):
        # Esperar a que el overlay desaparezca
        WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "v-overlay__scrim"))
        )
        # Esperar a que el botón de buscar sea clickeable y hacer clic
        boton_buscar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/div/div/div"))
        )
        boton_buscar.click()

        # Screenshot del formulario de búsqueda
        boton_buscar.screenshot("screenshots/header_sesion_iniciada/buscar.png")

    def test_04_idioma_moneda(self):
        # Esperar a que el overlay desaparezca
        WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "v-overlay__scrim"))
        )
        
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
        time.sleep(1)
        menu_idioma_moneda.screenshot("screenshots/header_sesion_iniciada/idioma_moneda.png")

    def test_05_boton_perfil(self):
        # Esperar a que el botón de perfil sea clickeable y hacer clic
        boton_perfil = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/div[2]/button"))
        )
        boton_perfil.click()

        # Esperar a que el menú de perfil sea visible
        menu_perfil = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/div[2]/button"))
        )

        # Screenshot del menú de perfil
        time.sleep(1)
        menu_perfil.screenshot("screenshots/header_sesion_iniciada/perfil.png")

    def test_06_boton_carrito(self):
        time.sleep(1)
        # Esperar a que el botón de carrito esté presente y hacer clic
        boton_carrito = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[3]"))
        )
        boton_carrito.click()

        # Esperar a que el carrito esté visible
        carrito = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='v-menu-33']/div/div"))
        )

        # Screenshot del carrito
        carrito.screenshot("screenshots/header_sesion_iniciada/carrito.png")

        # Esperar a que el botón de cerrar esté presente y hacer clic
        boton_cerrar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-33']/div/div/div[1]/button/span[3]/i"))
        )
        boton_cerrar.click()

    def test_07_seleccionar_idioma(self):
        # Esperar a que el botón de idioma sea clickeable y hacer clic
        boton_idioma_moneda = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__nuxt']/div[2]/div/header/div/div[2]/button[1]"))
        )
        boton_idioma_moneda.click()

        # Esperar a que se muestre el menú de idioma
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='v-menu-1']/div"))
        )

        # Hacer clic en English
        boton_english = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-1']/div/div/div[2]/div[2]/div/div/div[2]"))
        )
        boton_english.click()

        # Hacer clic en el botón de aplicar
        boton_aplicar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='v-menu-1']/div/div/div[2]/button"))
        )
        boton_aplicar.click()
        
        # Llamar a la función para verificar los elementos del encabezado
        self.verificar_header_elements()
        
        # Screenshot del encabezado después de cambiar el idioma
        time.sleep(1)
        self.driver.save_screenshot("screenshots/header_sesion_iniciada/header_ingles.png")

   
    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar las pruebas
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()