#교육을 목적으로 만든 이메일입니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = "https://mail.google.com/mail/&ogbl"
driver.get(url)
#action = ActionChains(driver)

driver.find_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf").send_keys("ansanths.computer@gmail.com")
#action.send_keys("ansanths.computer").perform()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf").send_keys("password")
driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".T-I.T-I-KE.L3").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".agP.aFw").send_keys("ansanths.computer@gmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".agP.aFw").send_keys(Keys.TAB)
driver.find_element(By.CSS_SELECTOR, ".aoT").send_keys("테스트 메일입니다.")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".aoT").send_keys(Keys.TAB)
driver.find_element(By.CSS_SELECTOR, ".Am.Al.editable.LW-avf.tS-tW").send_keys("안녕")
driver.find_element(By.CSS_SELECTOR, ".Am.Al.editable.LW-avf.tS-tW").send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, ".Am.Al.editable.LW-avf.tS-tW").send_keys("좋은 하루 보내세요.")
driver.find_element(By.CSS_SELECTOR, ".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()
#driver.quit()
