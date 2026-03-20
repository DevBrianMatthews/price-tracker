
# Archivo de código de prueba
import requests
from bs4 import BeautifulSoup

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
price       = gross_price.strip().split(" ")

# Mostrar el precio limpio en consola
print(price[0])


soup_name    = BeautifulSoup(html, 'html.parser')
element_name = soup_name.find('h1', class_="js-main-title")
name         = element_name.text

print(name)

# ----------- DATA BASE ----------

# conection = sqlite3.connect('prices.db')

# cursor = conection.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, url TEXT)')

