from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# pip install selenium
# pip install webdriver_manager


option = Options()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver = Service(ChromeDriverManager().install())
#chrome_driver = Service(ChromeDriverManager(path="경로명").install())
driver = webdriver.Chrome(service = chrome_driver , options=option)
driver.get('https://google.co.kr')

driver.find_element(By.CSS_SELECTOR, ".gLFyf.gsfi").send_keys("뽀로로")
driver.find_element(By.CSS_SELECTOR, ".gLFyf.gsfi").send_keys(Keys.ENTER)
#gLFyf gsfi
#q
