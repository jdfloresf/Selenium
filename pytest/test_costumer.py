import pytest
import time

from selenium import webdriver
from POM.Functions import Functions
from Locator import Locator

@pytest.fixture(scope="module")
def setup():
    global driver, f, t
    driver = webdriver.Edge()
    t = 0.1
    f = Functions(driver)
    f.navigate("https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F", t)
    f.validate_and_send_keys("xpath", Locator.email, "admin@yourstore.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin", t)
    f.click("xpath", Locator.submit, t)
    f.click("xpath", Locator.costumers, t)
    f.click("xpath", Locator.costumers_form, t)
    yield

@pytest.mark.usefixtures("setup")
def test_search_costumers():
    f.validate_and_send_keys("xpath", Locator.search_first_name, "Victoria", t)
    f.click("xpath", Locator.search_costumers, t)

@pytest.mark.usefixtures("setup")
def test_add_costumer():
    f.click("xpath", Locator.add_costumer, t)
    f.validate_and_send_keys("xpath", Locator.email, "jonathan@asdrome.com", t)
    f.validate_and_send_keys("xpath", Locator.password, "admin123", t)
    f.validate_and_send_keys("xpath", Locator.first_name, "Jonathan", t)
    f.validate_and_send_keys("xpath", Locator.last_name, "Flores", t)
    f.click("xpath", Locator.gender_male, t)
    f.validate_and_send_keys("xpath", Locator.date_birth, "19/05/2000", t)
    f.validate_and_send_keys("xpath", Locator.company, "Asdrome", t)
    f.validate_and_send_keys("xpath", Locator.roles, "Registered", t)
    f.click("xpath", Locator.save_costumer, t)
    time.sleep(5)