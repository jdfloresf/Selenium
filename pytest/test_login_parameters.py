import pytest
from selenium import webdriver
from POM.Functions import Functions
from Locator import Locator

@pytest.mark.login
@pytest.mark.parametrize("user, password", [
    ("admin@yourstore.com", "admin"),
    ("admin@asdrome.com", "admin"),
    ("admin@yourstore.com", "admin123"),])
def test_login(user, password):
    driver = webdriver.Edge()
    try:
        t = 0.1
        f = Functions(driver)
        f.navigate("https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F", t)
        f.validate_and_send_keys("xpath", Locator.email, user, t)
        f.validate_and_send_keys("xpath", Locator.password, password, t)
        f.click("xpath", Locator.submit, t)
        
        # Verifica si se accede al dashboard
        if f.validate_element("xpath", Locator.dashboard):
            print("Login Correcto")
        else:
            # Verifica si el mensaje de error por cuenta no encontrada está presente
            texto1 = f.validate_element("xpath", Locator.no_account)
            texto2 = f.validate_element("xpath", Locator.incorrect_credentials)
            if texto1:
                error = texto1.text
                if error == "No customer account found":
                    print(error)
                    print("Email incorrecto")
            # Verifica si el mensaje de error por credenciales incorrectas está presente
            elif texto2:
                error = texto2.text
                if error == "The credentials provided are incorrect":
                    print(error)
                    print("Password incorrecto")
    finally:
        driver.quit()  # Asegúrate de cerrar el navegador después de cada prueba
