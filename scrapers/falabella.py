from scrapers.base_scraper import BaseScraper
from bs4                   import BeautifulSoup


class FalabellaScraper(BaseScraper):
    def get_price(self, html):
        soup    = BeautifulSoup(html, 'html.parser')
        element = soup.find('span', class_="copy12")

        gross_price = element.text
        price       = float(gross_price.strip().replace('$', '').replace('.', '').strip())

        return price

    def get_name(self, html):
        soup         = BeautifulSoup(html, 'html.parser')
        element_name = soup.find('h1', class_="pdp-basic-info__product-name")
        name         = element_name.text
        return name