from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

SLEEP_TIME = 3
NEXT_PAGE_CLASS_NAME = "s-pagination-next"


class AmazonScraper:
    def __init__(self):
        self.last_url = ""

        options, chrome_options = self._disable_styling()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, chrome_options=chrome_options)

    def _disable_styling(self) -> tuple:
        options = Options()
        options.headless = True

        chrome_options = webdriver.ChromeOptions()
        # this will disable image loading
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        # or alternatively we can set direct preference:
        chrome_options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2,
                      'profile.managed_default_content_settings.javascript': 2}
        )

        return options, chrome_options

    def _save_product_links(self, file_name="product_links.txt") -> None:
        try:
            with open(file_name, "w") as file:
                while self.driver.find_element(By.CLASS_NAME, NEXT_PAGE_CLASS_NAME):
                    # checking if it's the last page of search results
                    if self.last_url == self.driver.current_url:
                        break

                    search_results = self.driver.find_element(By.CLASS_NAME, "s-search-results")
                    for item in search_results.find_elements(By.CLASS_NAME, "s-no-outline"):
                        print(item.get_attribute("href"), file=file)

                    # Going to next page
                    self.last_url = self.driver.current_url
                    self.driver.find_element(By.CLASS_NAME, NEXT_PAGE_CLASS_NAME).click()
                    sleep(SLEEP_TIME)
        except (EOFError, IOError) as err:
            print(err)

    def _get_product_information(self):
        index_folder = self._get_or_create_index_folder()
        i = 1

        with open("product_links.txt", "r") as file:
            for line in file.readlines():
                if line == "None\n":
                    continue

                self.driver.get(line)
                sleep(SLEEP_TIME)

                laptop_model = self.driver.find_element(By.XPATH, """// *[ @ id = "productTitle"]""").text
                laptop_description = self.driver.find_element(By.XPATH, """//*[@id="feature-bullets"]""").text
                try:
                    laptop_price = self.driver.find_element(By.XPATH,
                                                            """//*[@id="corePrice_feature_div"]/div/span[1]/span[2]/span[2]""").text
                except:
                    laptop_price = "Not available!"

                file_path = os.path.join(index_folder, f"file_{i}.txt")
                with open(file_path, "w") as laptop_info:
                    print(laptop_model, file=laptop_info)
                    print(self.driver.current_url, file=laptop_info)
                    print(laptop_price, file=laptop_info)
                    print(laptop_description, file=laptop_info)
                i += 1

    def _get_or_create_index_folder(self) -> str:
        index_folder = os.path.join(os.getcwd(), "index")

        if not os.path.exists(index_folder):
            os.makedirs(index_folder)

        return index_folder

    def start(self, url) -> None:
        self.driver.get(url)
        sleep(SLEEP_TIME)
        self._save_product_links()
        self._get_product_information()


if __name__ == "__main__":
    scraper = AmazonScraper()
    scraper.start(url="https://www.amazon.com/s?k=gaming+laptop&ref=nb_sb_noss")
