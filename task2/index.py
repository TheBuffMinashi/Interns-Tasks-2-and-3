from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get('https://www.amazon.com/')
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'nav-hamburger-menu')))
element.click()
time.sleep(1)
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[8]')))
element.click()
time.sleep(1) 
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hmenu-content"]/ul[6]/li[5]/a')))
element.click()
time.sleep(2)
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="n/565108"]/span')))
element.click()
time.sleep(2)
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="p_89/ASUS"]/span/a/span')))
element.click()
time.sleep(2)
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="p_n_feature_twenty-seven_browse-bin/23710032011"]/span/a/span')))
element.click()
time.sleep(3)
search_result = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div [@data-component-type="s-search-result"]')))
data = []
for item in search_result:
    name= item.find_element(By.XPATH, './/h2/a/span').text
    time.sleep(0.5)
    data.append(name)
print(data)

input("quit?")
browser.quit()