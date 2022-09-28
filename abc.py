from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# pip install selenium
# pip install webdriver_manager


option = Options()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver = Service(ChromeDriverManager().install())
#chrome_driver = Service(ChromeDriverManager(path="경로명").install())
driver = webdriver.Chrome(service = chrome_driver , options=option)
driver.get('https://mail.google.com/mail/&ogbl')

driver.find_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf").send_keys("ansanths.computer@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf").send_keys("ansan8955")
driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b").click()
