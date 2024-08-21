from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome() 
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text="돼지띠 운세"
search_box=driver.find_element(by=By.ID, value="query")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.ID, value="search-btn")
search_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR, value="#yearFortune > div.infors > div:nth-child(3) > div.detail._togglePanelSelectLink")
print("20104 김건우")
print(temp_div.text)
time.sleep(10)