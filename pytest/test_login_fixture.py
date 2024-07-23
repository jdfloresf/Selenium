import pytest

from selenium import webdriver
from POM.Functions import Functions
from Locator import Locator

# Fixture para la configuración del driver de Selenium y la navegación inicial
@pytest.fixture
def setup():
    driver = webdriver.Edge()  # Inicializa el driver de Edge
    t = 0.1  # Tiempo de espera entre acciones
    f = Functions(driver)  # Instancia de la clase Functions
    # Navega a la página de login
    f.navigate("https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F", t)
    driver.maximize_window()  # Maximiza la ventana del navegador
    yield t, f  # Retorna el tiempo de espera y la instancia de Functions

# Prueba del login exitoso
def test_login(setup):
    t, f = setup
    
    # Ingresa el correo y la contraseña
    f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin", t)
    f.click("xpath", Locator.submit, t)  # Clic en el botón de login
    
    # Verifica que el elemento dashboard exista
    dashboard = f.exit_element("xpath", Locator.dashboard, t)
    if dashboard == "Existe":
        print("Login Correcto")

# Prueba del login con el campo de email vacío
def test_login_missing_email(setup):
    t, f = setup

    # Deja el campo de correo vacío e ingresa la contraseña
    f.validate_and_send_keys("xpath", Locator.email, "", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin", t)
    f.click("xpath", Locator.submit, t)  # Clic en el botón de login
    
    # Verifica el mensaje de error por falta de correo
    error = f.validate_element("xpath", Locator.enter_email).text
    if error == "Please enter your email":
        print(error)
        print("Falta email")

# Prueba del login con el campo de contraseña vacío
def test_login_missing_password(setup):
    t, f = setup

    # Ingresa el correo y deja el campo de contraseña vacío
    f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "", t)
    f.click("xpath", Locator.submit, t)  # Clic en el botón de login
    
    # Verifica el mensaje de error por falta de contraseña
    error = f.validate_element("xpath", Locator.enter_pass).text
    if error == "The credentials provided are incorrect":
        print(error)
        print("Falta password")

# Prueba del login con un email incorrecto
def test_login_incorrect_email(setup):
    t, f = setup

    # Ingresa un correo incorrecto y la contraseña correcta
    f.validate_and_send_keys("xpath", Locator.email, "admin@asdrome.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin", t)
    f.click("xpath", Locator.submit, t)  # Clic en el botón de login
    
    # Verifica el mensaje de error por cuenta no encontrada
    error = f.validate_element("xpath", Locator.no_account).text
    if error == "No customer account found":
        print(error)
        print("Email incorrecto")

# Prueba del login con una contraseña incorrecta
def test_login_incorrect_password(setup):
    t, f = setup

    # Ingresa el correo correcto y una contraseña incorrecta
    f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin123", t)
    f.click("xpath", Locator.submit, t)  # Clic en el botón de login
    
    # Verifica el mensaje de error por credenciales incorrectas
    error = f.validate_element("xpath", Locator.incorrect_credentials).text
    if error == "The credentials provided are incorrect":
        print(error)
        print("Password incorrecto")

# Prueba del login con email y contraseña incorrectos
def test_login_incorrect_credentials(setup):
    t, f = setup

    # Ingresa un correo y una contraseña incorrectos
    f.validate_and_send_keys("xpath", Locator.email, "admin@asdrome.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admidan", t)
    f.click("xpath", Locator.submit, t)  # Clic en el botón de login
    
    # Verifica el mensaje de error por cuenta no encontrada
    error = f.validate_element("xpath", Locator.no_account).text
    if error == "No customer account found":
        print(error)
        print("Credenciales incorrectas")
