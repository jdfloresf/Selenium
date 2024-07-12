from selenium import webdriver
import unittest.test
from Functions import Functions
from Locator import Locator

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.t = 0.1

    def test1(self):
        print("Ejecutando TC 1")
        edge_driver = self.driver
        f = Functions(edge_driver)
        f.navigate("https://www.saucedemo.com/", 2)
        f.validate_and_send_keys("xpath", Locator.user_input, "standard_user", self.t)
        f.validate_and_send_keys("xpath", Locator.password_input, "secret_sauce", self.t)
        f.click("xpath",Locator.login_btn, self.t)
        f.tearDown(self.t)

    def test2(self):
        print("Ejecutando TC 2")
        edge_driver = self.driver
        f = Functions(edge_driver)
        # f.navigate("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", self.t)
        # f.select_by_type("xpath", Locator.lt, "text", self.t)
        f.navigate("https://demo.seleniumeasy.com/basic-checkbox-demo.html", 1)
        f.click("css", Locator.checkbox, self.t)
        f.click("xpath", Locator.checkbox2, self.t)
        f.click("xpath", Locator.check_all, self.t)
        
        for i in range(1, 5):
            f.click("xpath", Locator.checkbox2.replace(
                "//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[2]/label/input",
                f"//*[@id='easycont']/div/div[2]/div[2]/div[2]/div[{str(i)}]/label/input"), self.t)
        
        f.tearDown(self.t)

    def test3(self):
        print("Ejecutando TC 3")
        edge_driver = self.driver
        f = Functions(edge_driver)
        f.navigate("https://testpages.herokuapp.com/styled/file-upload-test.html", self.t)
        f.upload_file("css", Locator.select_file, "C://Users//sasum//Documents//Python//Selenium//venv//images//gato.jpg", self.t)
        f.click("css", Locator.submit_file, self.t)
        f.tearDown(self.t)


if __name__ == "__main__":
    unittest.main()