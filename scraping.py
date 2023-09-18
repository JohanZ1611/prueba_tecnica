'''
Web Scraping

1.Ejercicio 1

Requisito: Escribe un programa en Python que haga web scraping de la página principal de ScrapePark.org y
 extraiga las patinetas que cuestan menos de $68. Expectativa: El programa debe hacer web scraping de la página principal de ScrapePark.org y 
 extraer los nombres y precios de todas las patinetas que cuestan menos de $68.

2.Ejercicio 2

Requisito: Modifica el programa anterior para que también extraiga las patinetas cuyo nombre contenga un número mayor a 3.
 Expectativa: El programa modificado debe hacer lo mismo que el programa original, pero también debe extraer los nombres y
 precios de todas las patinetas cuyo nombre contenga un número mayor a 3.

3.Ejercicio 3
 
Requisito: Modifica el programa anterior para que guarde los nombres de los clientes y sus testimonios en un archivo CSV. 
Expectativa: El programa modificado debe hacer lo mismo que el programa anterior, pero también debe guardar los nombres de los clientes y 
sus testimonios en un archivo CSV.

'''

from bs4 import BeautifulSoup
import requests



URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, "html.parser")


#* Ejercicio 1

# divs = soup.find_all('div', class_='detail-box')
# productos = []
# precios = []

# for div in divs:
#   if (div.h6 is not None) and ('Patineta' in div.h5.text):
#     producto = div.h5.get_text(strip=True)
#     precio = div.h6.get_text(strip=True).replace('$', '')
#     if (int(precio ) < 68):
#         print(f'{producto:<18} | precio: {precio}')
#         productos.append(producto)
#         precios.append(precio)

#* Ejercicio 2

# divs = soup.find_all('div', class_='detail-box')
# productos = []
# precios = []

# for div in divs:
#   if (div.h6 is not None) and ('Patineta' in div.h5.text):
#     producto = div.h5.get_text(strip=True)
#     precio = div.h6.get_text(strip=True).replace('$', '')

#     if any(char.isdigit() and int(char) > 3 for char in producto.split() if char.isdigit()): 
#             #* se divide la cadena, luego se evalua que almenos contenga un digito y a esta misma se le hace la comparacion de que sea mayor a tres
#             print(f'{producto:<18} | precio: {precio}')
#             productos.append(producto)
#             precios.append(precio)

#* Ejercicio 3

divs = soup.find_all('div', class_='detail-box')
clientes = []
testimonios = []


for div in divs:
    if (div.h5 is not None) and ('Cliente' in div.h5.text):
        cliente = div.h5.get_text(strip=True)
        testimonio = div.p.get_text(strip=True)

        clientes.append(cliente)
        testimonios.append(testimonio)


clientes.insert(0,'Clientes')
testimonios.insert(0,'Testimonios')


Archivo = dict(zip(clientes,testimonios))

Archivo.items()

import csv

with open('Archio.csv','w') as A : 
    w = csv.writer(A)
    w.writerows(Archivo.items())
