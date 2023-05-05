from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


brands = [
    'ASUS',
    'MSI',
    'HP',
    'Lenovo',
    'Dell',
    'Acer',
    'SAMSUNG',
    'Gigabyte',
    'Apple',
    'LG'
]
for i in brands:
    print(i)
brand = input('enter brand: ')


PATH = './chromedriver.exe'


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.maximize_window()
driver.get('https://www.amazon.com/')

search = driver.find_element(By.NAME, "field-keywords")
search.send_keys('gaming laptop')
search.send_keys(Keys.RETURN)

driver.find_element(By.LINK_TEXT, 'ASUS').click()

product_links = driver.find_elements(
    By.XPATH,
    '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]',
)

links = []
for link in product_links:
    links.append(link.get_attribute('href'))

products = []
for link in links:
    driver.execute_script("window.open('%s', '_blank')" % link)
    driver.switch_to.window(driver.window_handles[-1])
    try:
        product_title = driver.find_element(By.ID, 'titleSection').text.encode('utf-8')
        products.append(product_title)
    except:
        product_title = None

    try:
        product_price = driver.find_element(By.CLASS_NAME, "a-price").text.encode('utf-8')
        products.append(product_price)
    except:
        product_price = None


    products.append(link)

with open('Links.txt', 'w') as f:
    for product in products:
        f.write(str(product) + '\n')

driver.quit()