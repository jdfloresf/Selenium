
from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

class Functions:
    def __init__(self, driver:webdriver):
        """Inicializa una instancia de la clase WebAutomation.
        Args:
            driver (webdriver): WebDriver de Selenium
        """
        self.driver = driver

    def wait(self, t:int):
        """Espera una cantidad de tiempo especificada.

        Args:
            t (int): Tiempo en segundos para esperar.
        """
        self.driver.implicitly_wait(t)

    def navigate(self, Url:str, t:int):
        """Navega a una URL especificada y maximiza la ventana del navegador.

        Args:
            Url (string): URL a la que se va a navegar
            t (int): Tiempo en segundos para esperar después de navegar.
        """
        self.driver.get(Url)
        print(f"Navegando a: {Url}")
        self.driver.maximize_window()
        self.wait(t)

    def validate_element(self, locator_type:str, locator:str) -> WebElement:
        """ Valida la presencia de un elemento en la página usando un selector, 
        lo desplaza a la vista,lo limpia y envía un texto al campo del elemento.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string):  El localizador del elemento
            text (string): Texto a enviar al campo del elemento.
            t (int): Tiempo en segundos para esperar después de interactuar con 
            el elemento.
        """
        locator_dict = {
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "tag": By.TAG_NAME,
            "id": By.ID,
            "class": By.CLASS_NAME,
        }

        try:
            if locator_type in locator_dict:
                by_type = locator_dict[locator_type]
                val = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((by_type, locator)))
                self.driver.execute_script("arguments[0].scrollIntoView();", val)
                return self.driver.find_element(by_type, locator)

            else:
                raise ValueError(f"Tipo de selector no soportado: {locator_type}")
            
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")
            return None

    def validate_and_send_keys(self, locator_type:str, locator:str, 
                                          text:str, t:int):
        """ Valida la presencia de un elemento en la página usando un selector, 
        lo desplaza a la vista,lo limpia y envía un texto al campo del elemento.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string):  El localizador del elemento
            text (string): Texto a enviar al campo del elemento.
            t (int): Tiempo en segundos para esperar después de interactuar con 
            el elemento.
        """
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                element.clear()
                element.send_keys(text)
                self.wait(t)
                print(f"Rellenando campo {locator} con -> {text}")
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")

    def click(self, locator_type:str, locator:str, t:int):
        """Hace click en un elemento de la página usando un selector y desplaza 
            el elemento a la vista.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string): El localizador del elemento.
            t (int): Tiempo en segundos para esperar después de hacer clic en 
            el elemento.
        """
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                element.click()
                print(f"\nDando click en campo: {locator}")
                self.wait(t)
        
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se puede dar click en elemento: {locator}")

    def double_click(self, locator_type:str, locator:str, t:int):
        """Hace doble clic en un elemento de la página usando un selector y 
            desplaza el elemento a la vista.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string): El localizador del elemento.
            t (int): Tiempo en segundos para esperar después de hacer clic en 
            el elemento.
        """
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                ActionChains(self.driver).double_click(element).perform()
                print(f"\nDando doble click en campo: {locator}")
                self.wait(t)
        
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se pudo dar doble click en elemento: {locator}")
    
    def right_click(self, locator_type:str, locator:str, t:int):
        """Hace doble clic en un elemento de la página usando un selector y 
            desplaza el elemento a la vista.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string): El localizador del elemento.
            t (int): Tiempo en segundos para esperar después de hacer clic en 
            el elemento.
        """
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                ActionChains(self.driver).context_click(element).perform()
                print(f"\nDando click derecho en elemento: {locator}")
                self.wait(t)
        
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se pudo dar click derecho en elemento: {locator}")

    def drag_and_drop(self, locator_type:str, locator:str, destino:str, t:int):
        """Hace doble clic en un elemento de la página usando un selector y 
            desplaza el elemento a la vista.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string): El localizador del elemento.
            t (int): Tiempo en segundos para esperar después de hacer clic en 
            el elemento.
        """
        try:
            val = self.validate_element(locator_type, locator)
            dest = self.validate_element(locator_type, destino)
            if val and dest:
                ActionChains(self.driver).drag_and_drop(val, dest).perform()
                print(f"\nSe solto elemento: {locator} en {dest}")
                self.wait(t)
        
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")
    
    def drag_and_drop_xy(self, locator_type:str, locator:str, x:str, y:str, t:int):
        """Hace doble clic en un elemento de la página usando un selector y 
            desplaza el elemento a la vista.

        Args:
            locator_type (string): Tipo de localizador (xpath o css)
            locator (string): El localizador del elemento.
            t (int): Tiempo en segundos para esperar después de hacer clic en 
            el elemento.
        """
        try:
            self.driver.switch_to.frame(0)
            element = self.validate_element(locator_type, locator)
            if element:
                ActionChains(self.driver).drag_and_drop_by_offset(element, x, y).perform()
                print(f"\nSe movie elemento {locator} a las coordenadas {x, y}")
                self.wait(t)
        
        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")

    def select_by_type(self, locator_type:str, locator:str, select_type:str, obj:str, t:int):
        """select_by_xpath_type

        Args:
            locator_type (string): Tipo de selector (xpath o css)
            locator (string): selector del elemento
            type (string): variable de control: index, text, value  
            val (string): elementor del elemento seleccinado
            t (int): tiempo de espera
        """
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                element = Select(element)

            if select_type == "index":
                element.select_by_index(obj)
            elif select_type == "text":
                element.select_by_visible_text(obj)
            elif select_type == "value":
                element.select_by_value(obj)

            print(f"\nEl campo seleccionado es: {obj}")
            self.wait(t)

        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {element}")

    def upload_file(self, locator_type:str, locator:str, file_path:str, t:int):
        """Sube un archivo selecciando desde una ruta
        Args:
            locator_type (string): Tipo de selector (xpath o css)
            locator (string): selector del elemento
            file_path (string): ruta del archivo
            t (int): tiempo de espera 
        """

        try:
            element = self.validate_element(locator_type, locator)
            if element:
                element.send_keys(file_path)
                print(f"\nSubiendo archivo con ruta: {file_path}")
                self.wait(t)

        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")

    def exit_element(self, locator_type:str, locator:str, t:int) -> str:
         """verifica que existe un elemento en la pagina y retorna un mensaje
        Args:
            locator_type (string): Tipo de selector (xpath o css)
            locator (string): selector del elemento
            t (int): tiempo de espera 
        Returns:
            str: Mensaje si existe o no un elmenento
        """
         try:
            element = self.validate_element(locator_type, locator)
            if element:
                print(f"elemento {locator} existe")
                self.wait(t)
                return "Existe"
            
         except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")
            return "No existe"
         
    def copy_paste(self, locator_type:str, locator:str, text:str, t:int):
        try:
            element = self.validate_element(locator_type, locator)
            if element:
                act = ActionChains(self.driver)
                self.validate_and_send_keys(locator_type, locator, text, t)

                # Copiar y Pegar
                act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                self.wait(t)
                act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
                act.send_keys(Keys.TAB)
                act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                print(f"Copiado: {text}")

        except TimeoutException as ex:
            print(ex.msg)
            print(f"\nNo se encontro elemento: {locator}")

    def tearDown(self, t: int):
        """Realiza acciones de limpieza después de la ejecución de los tests.
           Espera un tiempo especificado antes de cerrar el navegador.
        """
        self.wait(t)
        self.driver.close()
