import requests # Descarga el HTML

class BaseScraper:
    def fetch_page(self, url):
        request = requests.get(url)
        html    = request.text
        return html

    def get_price(self, html):
        raise NotImplementedError

    def get_name(self, html):
        raise NotImplementedError
