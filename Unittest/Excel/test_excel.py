import unittest

from selenium import webdriver
import unittest.test

from POM.Functions import Functions
from Locator import Locator
from Excel_Functions import *

class TestExcel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.t = 0.1
    
    def test1(self):
        edge_driver = self.driver
        f = Functions(edge_driver)
        ef = ExcelFunctios(edge_driver)

        f.navigate("https://demoqa.com/text-box", 2)

        path = "C://Users//sasum//Documents//Python//Selenium//venv//Unittest//Excel//Datos.xlsx"
        rows = ef.getRowCount(path, "Hoja1")

        for row in range(2, rows+1):
            nombre = ef.readData(path, "Hoja1", row, 1)
            email = ef.readData(path, "Hoja1", row, 2)
            dir1 = ef.readData(path, "Hoja1", row, 3)
            dir2 = ef.readData(path, "Hoja1", row, 4)

            f.validate_and_send_keys("xpath", Locator.name, nombre, self.t)
            f.validate_and_send_keys("xpath", Locator.email, email, self.t)
            f.validate_and_send_keys("xpath", Locator.current_address, dir1, self.t)
            f.validate_and_send_keys("xpath", Locator.permanet_address, dir2, self.t)
            f.click("xpath", Locator.sumit, self.t)

            existe = f.exit_element("xpath", Locator.exist_name, self.t)
            if existe == "Existe":
                print("Elemento insertado correctamente")
                ef.writeData(path, "Hoja1", row, 5, "Insertado")
            else:
                print("Elemento no insertado")
                ef.writeData(path, "Hoja1", row, 5, "Error")

if __name__ == "__main__":
    unittest.main()








