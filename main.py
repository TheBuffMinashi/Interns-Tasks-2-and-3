from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
        self._get_product_urls()

    def _close_driver(self):
        self.driver.close()

    def _get_product_urls(self):
        products_table = self.driver.find_element(By.CLASS_NAME, "ProductGrid__grid__f5oba")
        products = products_table.find_elements(By.CLASS_NAME, "ProductGridItem__itemOuter__KUtvv")
        for product in products:
            product = product.find_element(By.CLASS_NAME, "ProductGridItem__itemInfo__wl2YN")
            product_desc = product.find_element(By.CLASS_NAME, "Title__title__z5HRm")
            product_title = product_desc.text
            product_url = product_desc.get_attribute('href')
            product_price = product.find_element(By.CLASS_NAME, "price")
            product_price_text = product_price.find_element(
                By.CLASS_NAME,
                "Price__whole__mQGs5"
            ).text.replace(',', '') + product_price.find_element(
                By.CLASS_NAME,
                "Price__decimalSeparator__vydon"
            ).text + product_price.find_element(
                By.CLASS_NAME,
                "Price__fractional__wJiJp"
            ).text
            product_full_price = float(product_price_text)
            self.products.append({"title": product_title, "price": product_full_price, "url": product_url})
            self.product_urls.append(product_url)
        self._write_product_into_files()

    def _write_product_into_files(self):
        # TODO: write these products into txt files
        self._close_driver()


if __name__ == '__main__':
    link = input("Please insert the link: ")
    # https://www.amazon.com/stores/page/9FE6FA16-F70F-4905-88E3-63344313BFA9?ingress=2&visitId=7aaafd95-46f1-45f7-b5bf-f3e7bc2cf7c9&ref_=ast_bln
    AmazonLaptopScraper(listing_url=link)
