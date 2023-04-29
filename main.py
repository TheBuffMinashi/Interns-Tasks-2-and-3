import time
from selenium import webdriver
from selenium.webdriver.common.by import By

brand = "dell"
with open("./products/asus_laptops.txt", 'w') as file:
    for page_num in range(10):
        url = f"https://www.amazon.com/s?k={brand}+laptop&page={page_num}"
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        for product in products:
            title = product.find_element(By.XPATH, './/h2/a').text.encode('utf-8')
            link = product.find_element(By.XPATH, './/h2/a').get_attribute('href').encode('utf-8')
            try:
                price = product.find_element( By.CLASS_NAME,"a-price").text.encode('utf-8')

            except:
                price = "N/A"

            laptops = []

            laptops.append({
                'title': title,
                'link': link,
                'price': price
            })

            file.write(f" {laptops}\n")
