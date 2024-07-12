from selenium import webdriver
import unittest.test
from POM.Functions import Functions

import unittest

class SelectUpload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.t = 10

    def test1(self):
        edge_driver = self.driver
        f = Functions(edge_driver)
        f.navigate("https://www.techlistic.com/p/selenium-practice-form.html", self.t)
        f.select_by_type("xpath", "//*[@id='continents']", "text", "North America", self.t)
        f.select_by_type("xpath", "//*[@id='selenium_commands']", "index", "1", self.t)
        f.upload_file("xpath", "//*[@id='photo']", "C://Users//sasum//Documents//Python//Selenium//venv//images//gato.jpg", self.t)
        f.tearDown(self.t)

if __name__ == "__main__":
    unittest.main()