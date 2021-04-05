import time
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome()
driver.implicitly_wait(3)

wb = Workbook(write_only=True)
ws = wb.create_sheet('부동산 정보')
ws.append(['이름', '평형', '매매/전세', "가격"])
#
# driver.get('https://land.naver.com/')
#
# driver.find_element_by_css_selector('.search_input sta_search_text sta_text_ovr').send_keys('압구정 현대')

driver.get('https://land.naver.com/')
#
driver.find_element_by_css_selector('input#queryInputHeader').send_keys('압구정 현대')
driver.find_element_by_css_selector('a.search_button').click()

driver.find_element_by_css_selector('div.title').click()

# Want to find '매매' only but i don't know how to click '매매' checkbox now
# driver.find_element_by_css_selector('button.list_filter_btn').click()

last_height = driver.execute_script("return document.body.scrollHeight")

scroll_location = driver.find_element_by_css_selector('div.item_list.item_list--article')

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", scroll_location)

    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight", scroll_location)
    if new_height == last_height:
        break
    last_height = new_height

for land_info in driver.find_elements_by_css_selector('div.item_inner'):
    name = land_info.find_element_by_css_selector('span.text').text
    square_feet = land_info.find_element_by_css_selector('span.spec').text
    type = land_info.find_element_by_css_selector('span.type').text
    price = land_info.find_element_by_css_selector('span.price').text
    ws.append([name, square_feet, type, price])

driver.quit()
wb.save('압구정_신현대_가격정보.xlsx')
