from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://google.co.kr"
driver.get(url)

# from selenium.webdriver.common.by import By
# By.CSS_SELECTOR - CSS 선택자를 이용
# By.NAME - name 속성 이용
#driver.find_element(By.CSS_SELECTOR, ".gLFyf.gsfi").send_keys("뽀로로")
driver.find_element(By.NAME, "q").send_keys("뽀로로")

# Python Key class - https://github.com/SeleniumHQ/selenium/blob/selenium-4.2.0/py/selenium/webdriver/common/keys.py#L23
#from selenium.webdriver.common.keys import Keys
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)

#driver.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md").click()
driver.find_elements(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md")[1].click()

#driver.quit()
