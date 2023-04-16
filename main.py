from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


class AmazonLaptopScraper:
    def __init__(self, listing_url):
        self.listing_url = listing_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product_urls = []
        self.products: list[dict] = []

        self._get_brand_listing()

    def _get_brand_listing(self):
        self.driver.get(url=self.listing_url)
        self._get_products()

    def _close_driver(self):
        self.driver.close()

    def _get_products(self):
        try:
            products_table = WebDriverWait(self.driver, 30).until(
                ec.presence_of_element_located((By.CLASS_NAME, "ProductGrid__grid__f5oba"))
            )
            products = products_table.find_elements(By.CLASS_NAME, "ProductGridItem__itemOuter__KUtvv")
            for product in products:
                product = product.find_element(By.CLASS_NAME, "ProductGridItem__itemInfo__wl2YN")
                product_url = product.find_element(By.CLASS_NAME, "Title__title__z5HRm").get_attribute('href')
                self.product_urls.append(product_url)

            self._get_product_details()
        except TimeoutException:
            self._close_driver()

    def _get_product_details(self):
        for url in self.product_urls:
            self.driver.get(url)
            product_title = self.driver.find_element(By.ID, "productTitle").text
            product_price = self.driver.find_element(
                By.CLASS_NAME,
                "a-price-symbol"
            ).text + self.driver.find_element(
                By.CLASS_NAME,
                "a-price-whole"
            ).text + '.' + self.driver.find_element(
                By.CLASS_NAME,
                "a-price-fraction"
            ).text
            self.products.append({"title": product_title, "price": product_price, "url": url})
        self._write_product_into_files()

    def _write_product_into_files(self):
        for i in range(len(self.products)):
            with open(f'products/product_{i}.txt', 'w') as file:
                product = self.products[i]
                for field, value in product.items():
                    file.write(f"{field}: {value} \n")

        self._close_driver()


if __name__ == '__main__':
    link = "https://www.amazon.com/stores/page/9FE6FA16-F70F-4905-88E3-63344313BFA9?ingress=2&visitId=7aaafd95-46f1-45f7-b5bf-f3e7bc2cf7c9&ref_=ast_bln"
    AmazonLaptopScraper(listing_url=link)
