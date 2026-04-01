from database.models import get_connection, create_tables, insert_product, get_product_id, get_last_price, insert_price
from notifiers.telegram_notifier import send_notification
from scrapers.alkosto import AlkostoScraper
import asyncio

url = 'https://www.alkosto.com/macbook-pro-14-pulgadas-chip-m5-cpu-10-nucleos-gpu-10/p/195950488876?algEvent=eyJvYmplY3RJZCI6IjE5NTk1MDQ4ODg3NiIsImluZGV4IjoiYWxrb3N0b0luZGV4QWxnb2xpYVBSRCIsImFjdGlvbiI6InZpZXciLCJxdWVyeUlEIjoiOTU0MzhkYzUyMTUzZWUwOTk5MzljMGUxMTQ3NzdlNzQifQ=='

def check_prices():
    # Base de datos
    conection, cursor = get_connection('prices.db')
    create_tables(cursor)

    # Scraping
    scraper = AlkostoScraper()
    html    = scraper.fetch_page(url)
    price   = scraper.get_price(html)
    name    = scraper.get_name(html)

    # Guardar producto y obtener su id
    insert_product(cursor, name, url)
    product_id = get_product_id(cursor, url)

    # Comparar precios
    last_price = get_last_price(cursor, product_id)

    if last_price is None:
        print(f'Primer registro, precio actual: {price}')
    elif price < last_price[0]:
        message = f'El precio de {name} bajó, ahora está en: ${price:,.0f}\n{url}'
        asyncio.run(send_notification(message))

    # Siempre guardar el precio actual
    insert_price(cursor, product_id, price)
    conection.commit()
    conection.close()


check_prices()