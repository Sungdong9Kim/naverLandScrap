import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)
#
# driver.get('https://land.naver.com/')
#
# driver.find_element_by_css_selector('.search_input sta_search_text sta_text_ovr').send_keys('압구정 현대')

driver.get('https://land.naver.com/')
#
driver.find_element_by_css_selector('input#queryInputHeader').send_keys('압구정 현대')
driver.find_element_by_css_selector('a.search_button').click()

driver.find_element_by_css_selector('div.title').click()

driver.find_element_by_css_selector('button.list_filter_btn').click()