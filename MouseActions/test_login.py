import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

from POM.Functions import Functions
from Locator import Locator

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.t = 0.1
        load_dotenv()
        self.user = os.getenv("ADMIN")
        self.password = os.getenv("PASSWORD")
        

    def test1(self):
        print("Ejecutando TC 1")
        edge_driver = self.driver
        f = Functions(edge_driver)
        f.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 2)
        f.validate_and_send_keys_by_locator("xpath", Locator.username, self.user, self.t)
        f.validate_and_send_keys_by_locator("xpath", Locator.password, self.password, self.t)
        f.click_element_by_locator("xpath", Locator.submit, self.t)
        f.click_element_by_locator("css", Locator.admin, self.t)

        job = f.validate_by_locator("xpath", Locator.job, self.t)
        job_categories = f.validate_by_locator("css", Locator.categories, self.t)

        ActionChains(self.driver).move_to_element(job).click(job_categories).perform()

        f.tearDown(2)

if __name__ == "__main__":
    unittest.main()