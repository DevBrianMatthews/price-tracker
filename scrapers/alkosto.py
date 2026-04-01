from scrapers.base_scraper import BaseScraper
from bs4 import BeautifulSoup
class AlkostoScraper(BaseScraper):
    def get_price(self, html):
        soup    = BeautifulSoup(html, 'html.parser')
        element = soup.find('span', id="js-original_price")

        gross_price = element.text
        price       = gross_price.strip().split(" ")[0]
        price       = price.replace("$", "").replace(".", "")
        price       = float(price)

        return price

    def get_name(self, html):
        soup         = BeautifulSoup(html, 'html.parser')
        element_name = soup.find('h1', class_="js-main-title")
        name         = element_name.text
        return name
