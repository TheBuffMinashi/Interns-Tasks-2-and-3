from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pickle

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.get('https://www.amazon.com/')
time.sleep(5)
if os.path.exists('cookies.pkl'):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
    time.sleep(6)
else:
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
    time.sleep(6)

# //*[@id="nav-global-location-popover-link"]
# element_l = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="glow-ingress-block"]')))
# element_l.click()
element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'nav-hamburger-menu')))
element.click()
time.sleep(4)

element = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Computers")]/parent::a')))
element.click()
time.sleep(4)
element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Computers & Tablets")]')))
element.click()
element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="n/565108"]/span')))
element.click()
time.sleep(3)
element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//li[@aria-label="ASUS"]/span/a')))
element.click()
time.sleep(4)
element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//li[@aria-label="Gaming"]/span/a')))
element.click()
time.sleep(3)
# search_result = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div [@data-component-type="s-search-result"]')))
# # search_result = 'a','b','c','d','e','f','g'
data = []
n=0
# f = open("result_1.txt", "a")
while True:
    try:
        search_result = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div [@data-component-type="s-search-result"]')))
        for item in search_result:
            name= item.find_element(By.XPATH, './/h2/a/span').text
            n = n+1
            laptop = str(n) + "-" + name
            data.append(laptop)
            time.sleep(3)
            # f.write(laptop)
        next_page = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//a[starts-with(@class, "s-pagination-item s-pagination-next")]')))
        next_page.click()
        time.sleep(2)
    except:
        break
f = open("result.txt", "a", encoding="utf-8")
for laptop in data:
    f.write(laptop + "\n\n")
    time.sleep(1)
f.close()
print(data)

input("quit?")
browser.quit()