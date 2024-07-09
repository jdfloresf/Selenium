import unittest
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from dotenv import load_dotenv

from POM.Functions import Functions
from Locator import Locator

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.t = 0.1
        load_dotenv()
        self.user = os.getenv("ADMIN")
        self.password = os.getenv("PASSWORD")
        

    def test_login_and_navigate(self):
        print("Ejecutando TC 1")
        driver = self.driver
        f = Functions(driver)
        f.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 2)
        f.validate_and_send_keys("xpath", Locator.username, self.user, self.t)
        f.validate_and_send_keys("xpath", Locator.password, self.password, self.t)
        f.click("xpath", Locator.submit, self.t)
        f.click("css", Locator.admin, self.t)

        job = f.validate_element("xpath", Locator.job)
        job_categories = f.validate_element("css", Locator.categories)

        ActionChains(self.driver).move_to_element(job).click(job_categories).perform()

        f.tearDown(2)

    def test_double_click(self):
        print("Doble click en botón")
        driver = self.driver
        f = Functions(driver)
        f.navigate("https://demoqa.com/buttons", self.t)
        f.double_click("xpath", Locator.double_click, self.t)
        f.tearDown(2)
    
    def test_right_click(self):
        print("Doble click en botón")
        driver = self.driver
        f = Functions(driver)
        f.navigate("https://demoqa.com/buttons", self.t)
        f.right_click("xpath", Locator.right_click, self.t)
        f.tearDown(2)

    def test_draw_and_drop(self):
        print("Doble click en botón")
        driver = self.driver
        f = Functions(driver)
        f.navigate("https://demo.seleniumeasy.com/drag-and-drop-demo.html", self.t)
        f.navigate("https://testpages.herokuapp.com/styled/drag-drop-javascript.html", self.t)
        f.drag_and_drop("xpath", Locator.drop1, Locator.drop_zone, self.t)
        f.drag_and_drop("xpath", Locator.drop3, Locator.drop_zone, self.t)
        f.drag_and_drop("xpath", Locator.drop2, Locator.drop_zone, self.t)
        f.drag_and_drop("xpath", Locator.dr, Locator.pz, self.t)
        f.tearDown(2)

    def test_draw_and_drop_xy(self):
        driver = self.driver
        f = Functions(driver)
        f.navigate("https://jqueryui.com/draggable/", self.t)
        f.drag_and_drop_xy("xpath", Locator.drag, "150", "120", self.t)
        f.tearDown(2)
    
    def test_copy_paste(self):
        driver = self.driver
        f = Functions(driver)
        f.navigate("https://demoqa.com/automation-practice-form", self.t)
        f.copy_paste("xpath", Locator.first_name, "Juan", self.t)
        f.tearDown(2)
        
if __name__ == "__main__":
    unittest.main()
