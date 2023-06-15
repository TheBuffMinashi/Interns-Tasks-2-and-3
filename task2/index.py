from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pickle
import csv

# #////////////////// Step 1: Configuration //////////////////#

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(chrome_options=chrome_options)


# browser.get('https://www.amazon.com/')
# time.sleep(5)
# if os.path.exists('cookies.pkl'):
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         browser.add_cookie(cookie)
#     browser.refresh()
#     time.sleep(6)
# else:
#     pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
#     time.sleep(6)

# #////////////////// Step 2: Extract information //////////////////#

# element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'nav-hamburger-menu')))
# element.click()
# time.sleep(4)

# element = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Computers")]/parent::a')))
# element.click()
# time.sleep(4)
# element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Computers & Tablets")]')))
# element.click()
# element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="n/565108"]/span')))
# element.click()
# time.sleep(3)
# element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//li[@aria-label="ASUS"]/span/a')))
# element.click()
# time.sleep(4)
# element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//li[@aria-label="Gaming"]/span/a')))
# element.click()
# time.sleep(3)
# n=0
# links = []

# while True:
#     try:
#         search_result = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div [@data-component-type="s-search-result"]')))
#         for item in search_result:
#             link_page = item.find_element(By.XPATH, './/h2/a').get_attribute('href')
#             links.append(link_page)

#         next_page = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//a[starts-with(@class, "s-pagination-item s-pagination-next")]')))
#         next_page.click()
#         time.sleep(2)
#     except:
#         break

# for link in links:
#     n= n+1
#     browser.get(link)
#     try:
#         Brand_Laptop = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//tr[contains(@class, "po-brand")]/td[2]/span'))).text
#     except:
#         Brand_Laptop = "NaN"
#     try:
#         Series_Laptop = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//tr[contains(@class, "po-model_name")]/td[2]/span'))).text
#     except:
#         Series_Laptop = "NaN"
#     try:
#         Price_Laptop = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "priceToPay")]/span/span [@class="a-price-whole"]'))).text
#     except:
#         Price_Laptop = "NaN"
#     try:
#         Description_Laptop = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'productTitle'))).text
#     except:
#         Description_Laptop = "NaN"
#     try:
#         Link_Laptop = link
#     except:
#         Link_Laptop = "NaN"
#     try:
#         About_items = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@id="feature-bullets"]/ul/li')))
#     except:
#         About_items = ["NaN",]
#     time.sleep(4)

# #////////////////// Step 3: Save the information in text format //////////////////#

#     file = open("./Data/Text/" + str(n) + ".txt", "a", encoding="utf-8")
#     file.write("Brand => "+ Brand_Laptop + "\n\n" + "Series => "+ Series_Laptop + "\n\n" + "Price => "+ Price_Laptop + "\n\n" + "Description => "+ Description_Laptop + "\n\n" + "Link => "+ Link_Laptop + "\n\n")
#     for About_item in About_items:
#         try:
#             about = About_item.find_element(By.XPATH, './/span').text
#             file.write(about + "\n")
#         except:
#             file.write("NaN")
#             break
#     file.close()
#     time.sleep(15)
# browser.quit()
#////////////////// Step 4: Data is cleared and saved in .CSV format. //////////////////#
# Counts the number of extracted files.
Dir_len = len(os.listdir('./Data/Text/'))

List= []
n=1
for x in range(Dir_len):
    f=open("./Data/Text/" + str(n) + ".txt", "r", encoding="utf-8")
    Text_file =f.read()
    Text_file_CLR = Text_file.replace('Brand => ', '').replace('Series => ', '').replace('Price => ', '').replace('Description => ', '').replace('Link => ', '').replace('"', 'inch').replace('”', 'inch')
    Str_ascii = Text_file_CLR
    Str_encoding = Str_ascii.encode("ascii", "ignore")
    Str_decoding = Str_encoding.decode()
    contents= Str_decoding.split('\n\n')
    List.append(contents)
    n= n+1
    f.close()


file_csv = open("./Data/Result.csv", "w", newline="")
writer_csv = csv.writer(file_csv)
writer_csv.writerow( ['Brand', 'Series', 'Price', 'Description', 'link', 'About'] )
writer_csv.writerows( List )
file_csv.close()
