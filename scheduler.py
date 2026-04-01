from database.models import get_connection, create_tables, insert_product, get_product_id, get_last_price, insert_price
from notifiers.telegram_notifier import send_notification
from scrapers.alkosto import AlkostoScraper
import asyncio

from apscheduler.schedulers.blocking import BlockingScheduler

url = 'https://www.alkosto.com/macbook-pro-14-pulgadas-chip-m5-cpu-10-nucleos-gpu-10/p/195950488876?algEvent=eyJvYmplY3RJZCI6IjE5NTk1MDQ4ODg3NiIsImluZGV4IjoiYWxrb3N0b0luZGV4QWxnb2xpYVBSRCIsImFjdGlvbiI6InZpZXciLCJxdWVyeUlEIjoiOTU0MzhkYzUyMTUzZWUwOTk5MzljMGUxMTQ3NzdlNzQifQ=='

def check_prices():
    # Database
    conection, cursor = get_connection('prices.db')
    create_tables(cursor)

    # Scraping
    scraper = AlkostoScraper()
    html    = scraper.fetch_page(url)
    price   = scraper.get_price(html)
    name    = scraper.get_name(html)

    # Save the product and retrieve its ID
    insert_product(cursor, name, url)
    product_id = get_product_id(cursor, url)

    # Compare prices
    last_price = get_last_price(cursor, product_id)

    if last_price is None:
        print(f'Primer registro, precio actual: {price}')
    elif price < last_price[0]:
        message = f'El precio de {name} bajó, ahora está en: ${price:,.0f}\n{url}'
        asyncio.run(send_notification(message))

    # Always save the current price
    insert_price(cursor, product_id, price)
    conection.commit()
    conection.close()

scheduler = BlockingScheduler()
scheduler.add_job(check_prices, 'interval', seconds=10)
scheduler.start()