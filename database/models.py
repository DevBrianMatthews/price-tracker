import sqlite3

def get_connection(name_db):
    conection = sqlite3.connect(name_db)
    cursor    = conection.cursor()

    return conection, cursor


def create_tables(cursor):
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, url TEXT UNIQUE)'
    )

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS price_history (id INTEGER PRIMARY KEY, product_id INTEGER, price REAL, date TEXT DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (product_id) REFERENCES products(id))'
    )


def insert_product(cursor, name, url):
    cursor.execute(
        'INSERT OR IGNORE INTO products (name, url) VALUES (?, ?)', (name, url)
    )

def get_product_id(cursor, url):
    cursor.execute(
        'SELECT id FROM products WHERE url = ?', (url,)
    )
    result = cursor.fetchone()
    return result[0] if result else None


def insert_price(cursor, product_id, price):
    cursor.execute(
        "INSERT INTO price_history (product_id, price) VALUES (?, ?)", (product_id, price)
    )


def get_last_price(cursor, product_id):
    cursor.execute(
        'SELECT price FROM price_history WHERE product_id = ? ORDER BY date DESC LIMIT 1', (product_id,)
    )

    return cursor.fetchone()