import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://land.naver.com/')

driver.find_element_by_css_selector('queryInputHeader').send_keys('압구정 현대')