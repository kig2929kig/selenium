# pip install selenium
# pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver = Service(ChromeDriverManager().install())
#chrome_driver = Service(ChromeDriverManager(path="경로명").install())
driver = webdriver.Chrome(service = chrome_driver , options=option)

def open_url(url) :
    driver.get(url)

def my_find_element_send_keys(element, send_text) :
    driver.find_element(By.NAME, element).send_keys(send_text)

def my_find_element_enter(element) :
    driver.find_element(By.NAME, element).send_keys(Keys.ENTER)

def my_find_element_click(element) :
    driver.find_element(By.CSS_SELECTOR, element).click()

def my_find_elements_item(element) :
    my_List = []
    my_list = driver.find_elements(By.CSS_SELECTOR, element)
    return my_list

def my_src_get(element) :
    src = driver.find_element(By.CSS_SELECTOR, element).get_attribute("src")
    return src



