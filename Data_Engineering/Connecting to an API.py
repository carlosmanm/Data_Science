import requests

response = requests.get('https://randomfox.ca/floof')

print(response.status_code)

# 200 means that everything worked ok

print(response.text)

# Nos brindara información que podemos utilizar en nuestros programas

# Esto viene en formato JSON y SPOILER practicamente todas las APIs vienen
# en formato JSON. Es un estandar para comunicación e información de APIs

# {"image":"https:\/\/randomfox.ca\/images\/40.jpg","link":"https:\/\/randomfox.ca\/?i=40"}

print(response.json())

# Nos enseñara en este nuevo formato:

# {'image': 'https://randomfox.ca/images/40.jpg', 'link': 'https://randomfox.ca/?i=40'}

# En formato diccionario de Python que ya podemos utilizar.

fox = response.json()

print(fox['image'])

# nuestra respuesta: https://randomfox.ca/images/40.jpg

# --------- Working with APIs in Python for your Data Science Project

# Using YouTube API

# api --------> json -----> pandas

