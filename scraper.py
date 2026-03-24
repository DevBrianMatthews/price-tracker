# Archivo de código de prueba

import requests # Descarga el HTML
from bs4 import BeautifulSoup # Limpia el HTML

import sqlite3


# URL del sitio a busar el precio
url = 'https://www.alkosto.com/macbook-pro-14-pulgadas-chip-m5-cpu-10-nucleos-gpu-10/p/195950488876?algEvent=eyJvYmplY3RJZCI6IjE5NTk1MDQ4ODg3NiIsImluZGV4IjoiYWxrb3N0b0luZGV4QWxnb2xpYVBSRCIsImFjdGlvbiI6InZpZXciLCJxdWVyeUlEIjoiOTU0MzhkYzUyMTUzZWUwOTk5MzljMGUxMTQ3NzdlNzQifQ=='

# Traer el HTML completo del sitio web
request = requests.get(url)
html    = request.text

# Buscar dentro de ese HTML la etiqueta donde está el precio
soup    = BeautifulSoup(html, 'html.parser')
element = soup.find('span', id="js-original_price")


# Traer el precio y limpiarlo
gross_price = element.text
price       = gross_price.strip().split(" ")[0]
price       = price.replace("$", "").replace(".", "")
price       = float(price)

# Traer el Nombre del producto
element_name = soup.find('h1', class_="js-main-title")
name         = element_name.text

# print(name)

# ----------- DATA BASE ----------

# Abrimos la conexion a la base de datos que crea un archivo .db
conection = sqlite3.connect('prices.db')

# Cursor se encarga de ser intermediario entre la conexion para poder escribir las queries
cursor = conection.cursor()

# Ejecuta la instruccion de SQL en forma de texto y crea la tabla con sus filas
cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, url TEXT UNIQUE)')

# Se insetan los datos en las columnas de la tabla
cursor.execute('INSERT OR IGNORE INTO products (name, url) VALUES (?, ?)', (name, url))

#Selecciona el product_id
cursor.execute("SELECT id FROM products WHERE url = ?", (url,)) # IMPORTANTE la coma (,) para que se sepa que es una Tupla y no una variable.
product_id = cursor.fetchone()[0] # Muestra en una sola linea el primer elemento de la tubla

# Crea tabla de precios historicos
cursor.execute('CREATE TABLE IF NOT EXISTS price_history (id INTEGER PRIMARY KEY, product_id INTEGER, price REAL, date TEXT DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (product_id) REFERENCES products(id))')


# Traer el precio anterior y el nuevo precio
# ...
cursor.execute(
    "SELECT price FROM price_history WHERE product_id = ? ORDER BY date DESC LIMIT 1",
    (product_id,)
)

last_price = cursor.fetchone()

# Comparar si el precio anterior y el nuevo cambio
if last_price is None:
    print(f'Aun no hay precios a comparar, el precio actual es: {price}')
elif price < last_price[0]:
    print(f'El precio disminuyó, ahora es: {price}')


# Agregar producto y precio a la tabla de histórico.
cursor.execute(
    "INSERT INTO price_history (product_id, price) VALUES (?, ?)",
    (product_id, price)
)


# Confirma las instrucciones
conection.commit()

# Cierra la conexion
conection.close()

