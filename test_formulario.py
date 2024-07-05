from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait, Select 
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from time import sleep

from datetime import datetime

driver = webdriver.Edge()
t = 2
date = datetime.today().strftime("%d-%m-%Y")

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
sleep(t)

try:
    driver.execute_script("arguments[0].scrollIntoView();",
                          WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable(
                            (By.XPATH, "//*[@id='post-body-3077692503353518311']"
                                "/div[1]/div/div/h2[2]/div[1]/div/div[2]/input"))))

    buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='post-body-3077692503353518311']"
         "/div[1]/div/div/h2[2]/div[1]/div/div[2]/input")))
    
    buscar.find_element(By.XPATH, "//*[@id='post-body-3077692503353518311']"
                        "/div[1]/div/div/h2[2]/div[1]/div/div[2]/input") \
                        .send_keys("Jonathan" + Keys.TAB + "Flores")
    
    driver.find_element(By.XPATH, "//*[@id='sex-0']").click()
    driver.find_element(By.XPATH, "//*[@id='exp-1']").click()
    driver.find_element(By.XPATH, "//*[@id='datepicker']") \
    .send_keys(date)

    driver.find_element(By.XPATH, "//*[@id='profession-1']").click()

    sleep(t)

    driver.execute_script("arguments[0].scrollIntoView();",
                          WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable(
                            (By.XPATH, "//*[@id='tool-0']"))))
    
    driver.find_element(By.XPATH, "//*[@id='tool-0']").click()
    driver.find_element(By.XPATH, "//*[@id='tool-2']").click()

    continent = Select(driver.find_element(By.XPATH, "//*[@id='continents']"))
    continent.select_by_visible_text("North America")
    
    commands = Select(driver.find_element(By.XPATH, "//*[@id='selenium_commands']"))
    commands.select_by_index(1)

    sleep(t)

    driver.find_element(By.XPATH, "//*[@id='photo']") \
    .send_keys("C://Users//sasum//Documents//Python//Selenium//venv//images//gato.jpg")

    sleep(t)

    driver.execute_script("arguments[0].scrollIntoView();",
                          WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable(
                            (By.XPATH, "//*[@id='PageList2']/div/div[1]/div[1]"
                             "/div/ul/li[2]/div/a"))))
    
    menu = driver.find_element(By.XPATH, "//*[@id='PageList2']/div/div[1]/div[1]/div/ul/li[2]/div/a")
    hidden_menu = driver.find_element(By.XPATH, "//*[@id='PageList2']/div/div[1]/div[1]/div/ul/li[2]/div/div/a[2]")
    ActionChains(driver).move_to_element(menu).click(hidden_menu).perform()

except TimeoutException as ex:
    print(ex)
    print("Element not found")

sleep(t)
driver.close()