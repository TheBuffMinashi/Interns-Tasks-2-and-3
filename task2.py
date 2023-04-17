from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def scrape(link: str):
    outdir = Path(__file__).parent / 'out'
    outdir.mkdir(exist_ok=True)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    page = 1
    driver.get(link.format(page))
    all_pages = int(driver.find_elements(By.XPATH, '//span[contains(@class, "s-pagination-disabled")]')[-1].text)

    while True:
        elems = driver.find_elements(By.XPATH, '//div[contains(@data-component-type, "s-search-result")]')

        for elem in elems:
            filename = elem.get_attribute('data-asin')
            elem_link = elem.find_element(By.XPATH, './/h2/a').get_attribute('href')
            elem_driver = webdriver.Chrome()
            elem_driver.get(elem_link)
            title = elem_driver.find_element(By.XPATH, '//span[@id="productTitle"]').text
            price = elem_driver.find_element(By.XPATH, '//span[@class="a-price-whole"]').text
            about = elem_driver.find_element(By.XPATH, '//div[@id="feature-bullets"]/ul').text

            with open(outdir / f'{filename}.txt', 'w') as f:
                f.write(f'title: {title}\n')
                f.write(f'price: {price}\n')
                f.write(f'url: {elem_link}\n')
                f.write(f'about: {about}\n')

        page += 1
        if page > all_pages:
            break
        driver = webdriver.Chrome()
        driver.get(link.format(page))


if __name__ == '__main__':
    asus_link = "https://www.amazon.com/s?k=gaming+laptops&i=electronics&rh=n%3A172282%2Cp_89%3AASUS&dc&pf_rd_i" \
                "=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r" \
                "=Z3TJSQZRFZ4ECSEJK9BR&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1681722140&rnid=2528832011&ref" \
                "=sr_pg_{}"
    scrape(asus_link)
