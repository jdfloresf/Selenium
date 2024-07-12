import pytest
import time

from selenium import webdriver
from POM.Functions import Functions
from Locator import Locator

from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Edge()
    t = 0.1
    f = Functions(driver)
    f.navigate("https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F", t)
    f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin", t)
    f.click("xpath", Locator.submit, t)
    f.click("xpath", Locator.catalog, t)
    f.click("xpath", Locator.products, t)
    yield t, f

def test_search_product(setup):
    t, f = setup
    
    f.validate_and_send_keys("xpath", Locator.product_name1, "computer", t)
    f.click("xpath", Locator.search, t)

 
def test_add_new(setup):
    t, f = setup

    f.click("xpath", Locator.add_new, t)
    f.validate_and_send_keys("xpath", Locator.product_name2, "Laptop HP", t)
    f.validate_and_send_keys("xpath", Locator.sku, "HP-B123", t)
    f.validate_and_send_keys("xpath", Locator.price, "400", t)
    f.select_by_type("xpath", Locator.inventory, "text", "Track inventory", t)
    f.click("xpath", Locator.save_button, t)
    f.tearDown(t)

def test_set_image(setup):
    t, f = setup

    f.validate_and_send_keys("xpath", Locator.product_name1, "Laptop HP", t)
    f.click("xpath", Locator.search, t)
    time.sleep(2)
    f.click("css", Locator.edit_button, t)
    time.sleep(2)
    existe = f.exit_element("css", Locator.upload, t)
    if existe == "Existe":
        f.upload_file("css", Locator.upload, "C://Users//sasum//Documents//Python//Selenium//venv//images//hp.jpg", t)
    else:
        print("Algo salio mal")
    
