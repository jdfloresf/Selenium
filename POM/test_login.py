from selenium import webdriver
import unittest.test
from Funtions import Functions
from Locator import Locator

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test1(self):
        print("Ejecutando TC 1")
        edge_driver = self.driver
        f = Functions(edge_driver)
        f.navigate("https://www.saucedemo.com/", 2)
        f.validate_by_locator("xpath", Locator.user_input, "standard_user", 0.5)
        f.validate_by_locator("xpath", Locator.password_input, "secret_sauce", 0.5)
        f.click_element_by_locator("xpath",Locator.login_btn, 2)
        f.tearDown()

    def test2(self):
        print("Ejecutando TC 2")
        edge_driver = self.driver
        f = Functions(edge_driver)
        # f.navigate("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", 1)
        # f.select_by_type("xpath", Locator.lt, "text", 0.5)
        f.navigate("https://demo.seleniumeasy.com/basic-checkbox-demo.html", 1)
        f.click_element_by_locator("css", Locator.checkbox, 0.5)
        f.click_element_by_locator("xpath", Locator.checkbox2, 0.5)
        f.click_element_by_locator("xpath", Locator.check_all, 0.5)
        
        for i in range(1, 5):
            f.click_element_by_locator("xpath", Locator.checkbox2.replace(
                "//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[2]/label/input",
                f"//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[{str(i)}]/label/input"), 0.5)
        
        f.tearDown()

    def test3(self):
        print("Ejecutando TC 3")
        edge_driver = self.driver
        f = Functions(edge_driver)
        f.navigate("https://testpages.herokuapp.com/styled/file-upload-test.html", 0.5)
        f.upload_file("css", Locator.select_file, "C://Users//sasum//Documents//Python//Selenium//venv//images//gato.jpg", 0.5)
        f.click_element_by_locator("css", Locator.submit_file, 0.5)
        f.tearDown()


if __name__ == "__main__":
    unittest.main()