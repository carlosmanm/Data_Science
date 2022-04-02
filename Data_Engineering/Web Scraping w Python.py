# Web scraping o raspado web, es una técnica utilizada mediante programas de software para extraer información de sitios web.1​ Usualmente, 
# estos programas simulan la navegación de un humano en la World Wide Web ya sea utilizando el protocolo HTTP manualmente, o incrustando un 
# navegador en una aplicación.

# El web scraping está muy relacionado con la indexación de la web, la cual indexa la información de la web utilizando un robot y es una 
# técnica universal adoptada por la mayoría de los motores de búsqueda. Sin embargo, el web scraping se enfoca más en la transformación de datos 
# sin estructura en la web (como el formato HTML) en datos estructurados que pueden ser almacenados y analizados en una base de datos central,
# en una hoja de cálculo o en alguna otra fuente de almacenamiento. Alguno de los usos del web scraping son la comparación de precios en tiendas, 
# la monitorización de datos relacionados con el clima de cierta región, la detección de cambios en sitios webs y la integración de datos en sitios 
# webs. También es utilizado para obtener información relevante de un sitio a través de los rich snippets.


# Las herramientas de web scraping son software, es decir, bots programados para examinar bases de datos y extraer información. 
# Se utiliza una gran variedad de tipos de bot, muchos de ellos totalmente personalizables para:

# Reconocer estructuras de sitios HTML únicos.
# Extraer y transformar contenidos.
# Almacenar datos.
# Extraer datos de las API.
# Dado que todos los bots utilizan el mismo sistema para acceder a los datos del sitio, a veces puede resultar difícil distinguir 
# entre bots legítimos y bots maliciosos.

# Diferencias clave entre bots legítimos y maliciosos
# Existen algunas diferencias clave que te ayudarán a distinguir entre los dos:

# Los robots legítimos se identifican con la organización para la que lo hacen. Por ejemplo, Googlebot se identifica en su 
# encabezado HTTP como perteneciente a Google. Los robots maliciosos, a la inversa, se hacen pasar por tráfico legítimo al crear 
# un usuario HTTP falso.

# Los robots legítimos respetan el archivo robot.txt de un sitio, que enumera las páginas a las que puede acceder un robot y las que no. 
# Los maliciosos, por otro lado, rastrean el sitio web independientemente de lo que el operador del sitio haya permitido.

# El web scraping se considera malicioso cuando los datos se extraen sin el permiso de los propietarios de sitios web

import pandas
import bs4
from pandas.core.algorithms import rank
import requests

url = 'https://mexico.as.com/resultados/futbol/mexico_clausura/clasificacion/'

page = requests.get(url)

soup = bs4.BeautifulSoup(page.content, 'html.parser')

# Equipos

# Para obtener estos datos de Span y nombre-equipo debemos irnos a Inspeccionar (dando clic en los datos que queremos obtener) e identificar
# esta información  

eq = soup.find_all('span', class_='nombre-equipo')

print(eq)

equipos = list()

count = 0

for i in eq:
    if count < 20:
        equipos.append(i.text)
    else:

        break
    count +=1
print(equipos)

# Puntos

pts = soup.find_all('td', class_='destacado')

print(pts)

puntos = list()

count = 0

for i in pts:
    if count < 20:
        puntos.append(i.text)
    else:

        break
    count +=1
print(puntos)

# Crear dataframe



df = pandas.DataFrame({'Nombre': equipos, 'Puntos':puntos}, index=list(range(1, 21)))

df.head()