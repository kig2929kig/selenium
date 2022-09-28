from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# pip install selenium
# pip install webdriver_manager


option = Options()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver = Service(ChromeDriverManager().install())
#chrome_driver = Service(ChromeDriverManager(path="경로명").install())
driver = webdriver.Chrome(service = chrome_driver , options=option)
driver.get('https://naver.com')
