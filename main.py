import time
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome()
driver.implicitly_wait(3)

wb = Workbook(write_only=True)
ws = wb.create_sheet('부동산 정보')
ws.append(['평형', '매매/전세', "가격"])
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

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height