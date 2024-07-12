from selenium import webdriver
from POM.Functions import Functions
from Locator import Locator

def setUp():
    driver = webdriver.Edge()
    t = 0.1
    f = Functions(driver)
    f.navigate("https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F", t)
    driver.maximize_window() 
    return driver, t, f

def test_login():
    driver, t, f = setUp()
    
    f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin", t)
    f.click("xpath", Locator.submit, t)
    
    dashboard = f.exit_element("xpath", Locator.dashboard, t)
    if dashboard == "Existe":
        print("Login Correcto")

    f.tearDown(t)

# def test_login_missing_email():
#     driver, t, f = setUp()

#     f.validate_and_send_keys("xpath", Locator.email, "", t)
#     f.validate_and_send_keys("xpath", Locator.password, "admin", t)
#     f.click("xpath", Locator.submit, t)
    
#     error = f.validate_element("xpath", Locator.enter_email).text
#     if error == "Please enter your email":
#         print(error)
#         print("Falta email")

#     f.tearDown(t)

# def test_login_missing_password():
#     driver, t, f = setUp()

#     f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
#     f.validate_and_send_keys("xpath", Locator.password, "", t)
#     f.click("xpath", Locator.submit, t)
    
#     error = f.validate_element("xpath", Locator.enter_pass).text
#     if error == "The credentials provided are incorrect":
#         print(error)
#         print("Falta password")

#     f.tearDown(t)

# def test_login_incorrect_email():
#     driver, t, f = setUp()

#     f.validate_and_send_keys("xpath", Locator.email, "admin@asdrome.com", t)
#     f.validate_and_send_keys("xpath", Locator.password, "admin", t)
#     f.click("xpath", Locator.submit, t)
    
#     error = f.validate_element("xpath", Locator.no_account).text
#     if error == "No customer account found":
#         print(error)
#         print("Email incorrecto")

#     f.tearDown(t)

# def test_login_incorrect_password():
#     driver, t, f = setUp()

#     f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
#     f.validate_and_send_keys("xpath", Locator.password, "admin123", t)
#     f.click("xpath", Locator.submit, t)
    
#     error = f.validate_element("xpath", Locator.incorrect_credentials).text
#     if error == "The credentials provided are incorrect":
#         print(error)
#         print("Password incorrecto")

#     f.tearDown(t)

# def test_login_incorrect_credentials():
#     driver, t, f = setUp()

#     f.validate_and_send_keys("xpath", Locator.email, "admin@asdrome.com", t)
#     f.validate_and_send_keys("xpath", Locator.password, "admidan", t)
#     f.click("xpath", Locator.submit, t)
    
#     error = f.validate_element("xpath", Locator.no_account).text
#     if error == "No customer account found":
#         print(error)
#         print("Email y password incorrectos")

#     f.tearDown(t)