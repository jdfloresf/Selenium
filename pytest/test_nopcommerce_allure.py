import pytest
import allure
import time

from selenium import webdriver
from allure_commons.types import AttachmentType

from POM.Functions import Functions
from Locator import Locator

# Pytest fixture para configurar el entorno de pruebas
@pytest.fixture
def setup():
    # Inicializa el controlador Edge de Selenium
    driver = webdriver.Edge()
    # Tiempo de espera predeterminado entre acciones
    t = 0.1
    # Inicializa una instancia de la clase Functions con el controlador
    f = Functions(driver)
    # Navega a la página de inicio de sesión
    f.navigate("https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F", t)
    # Ingresa el correo electrónico en el campo de inicio de sesión
    f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
    # Ingresa la contraseña en el campo de inicio de sesión
    f.validate_and_send_keys("xpath", Locator.password, "admin", t)
    # Hace clic en el botón de enviar
    f.click("xpath", Locator.submit, t)
    # Navega al catálogo
    f.click("xpath", Locator.catalog, t)
    # Navega a los productos
    f.click("xpath", Locator.products, t)
    # Devuelve el tiempo de espera, las funciones y el controlador para usarlos en las pruebas
    yield t, f, driver

# Prueba para buscar un producto
def test_search_product(setup):
    # Recupera las variables configuradas en el fixture
    t, f, driver = setup
    
    # Ingresa "computer" en el campo de búsqueda de productos
    f.validate_and_send_keys("xpath", Locator.product_name1, "computer", t)
    # Hace clic en el botón de buscar productos
    f.click("xpath", Locator.search_products, t)
    # Toma una captura de pantalla y la adjunta al reporte de Allure
    allure.attach(driver.get_screenshot_as_png(), name="search_product", 
                  attachment_type=AttachmentType.PNG)

# Prueba para agregar un nuevo producto
def test_add_new(setup):
    # Recupera las variables configuradas en el fixture
    t, f, driver = setup

    # Hace clic en el botón de agregar nuevo producto
    f.click("xpath", Locator.add_new, t)
    # Ingresa el nombre del producto
    f.validate_and_send_keys("xpath", Locator.product_name2, "Laptop HP", t)
    # Toma una captura de pantalla y la adjunta al reporte de Allure
    allure.attach(driver.get_screenshot_as_png(), name="add_product", 
                  attachment_type=AttachmentType.PNG)
    # Ingresa el SKU del producto
    f.validate_and_send_keys("xpath", Locator.sku, "HP-B123", t)
    # Toma una captura de pantalla y la adjunta al reporte de Allure
    allure.attach(driver.get_screenshot_as_png(), name="model_product", 
                  attachment_type=AttachmentType.PNG)
    # Ingresa el precio del producto
    f.validate_and_send_keys("xpath", Locator.price, "400", t)
    # Toma una captura de pantalla y la adjunta al reporte de Allure
    allure.attach(driver.get_screenshot_as_png(), name="price_product", 
                  attachment_type=AttachmentType.PNG)
    # Selecciona la opción "Track inventory" en el campo de inventario
    f.select_by_type("xpath", Locator.inventory, "text", "Track inventory", t)
    # Hace clic en el botón de guardar
    f.click("xpath", Locator.save_button, t)
    # Finaliza la sesión del controlador
    f.tearDown(t)

# Prueba para establecer una imagen para un producto
def test_set_image(setup):
    # Recupera las variables configuradas en el fixture
    t, f, driver = setup

    # Ingresa el nombre del producto en el campo de búsqueda
    f.validate_and_send_keys("xpath", Locator.product_name1, "Laptop HP", t)
    # Hace clic en el botón de buscar productos
    f.click("xpath", Locator.search_products, t)
    # Espera 2 segundos
    time.sleep(2)
    # Hace clic en el botón de editar producto
    f.click("css", Locator.edit_button, t)
    # Espera implícitamente 2 segundos
    driver.implicitly_wait(2)
    # Sube un archivo de imagen para el producto
    f.upload_file("xpath", Locator.upload, "C://Users//sasum//Documents//Python//Selenium//venv//images//hp.jpg", t)
