from os import remove
import pandas as pd
import numpy as np

# C:\Users\carlvazquez\AppData\Local\Programs\Python\Python39

# ------------------------------------ Manipulación Basica
sr = pd.Series([10, 9, 8, 7, 6])
sr
sr.values
sr.index

sr = pd.Series([10, 9, 8, 7, 6], index =['a', 'b', 'c', 'd', 'e'])

sr

sr.isnull().any()

# diccionario

dict_data = {'CO':100, 'MX':200, 'AR':300}
dict_data

dict_data.keys()

dict_data['AR']

pd.Series(dict_data)

pd.Series(dict_data, index=['CO', 'MX', 'AR'])

np.nan + 10

sr.isnull()


# Panel Data

dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}

data = pd.DataFrame(dict_data)

data.head()

data.columns

data['Q1'].isnull().any()

data['Q1'] = data['Q1'].fillna(data['Q1'].mean())

df = pd.DataFrame(dict_data, index=['ana', 'benito', 'camilo', 'daniel', 'erika', 'fabian', 'gabriela'])
df

df.index

df[['edad', 'Q1']]

df.loc[['ana', 'erika'],['edad', 'Q1']]

df.iloc[2,1]

# loc permite seleccionar a traves de index y columnas y iloc 
# por su posición dentro de df

df.iloc[2, [1,3]]

df.iloc[:, [1,3]]

df[(df['edad']>=12) & (df['pais']=='mx')]

df.query('edad>12')

df[df['Q2'] > df['Q1']]

# ------------------------------------------- Conexion a BD SQL

# Pandas cuenta con una funcionalidad que facilita el acceso a tus bases de datos tipo SQL, para ello te mostrare algunos ejemplos:

# ------------------------------ PostgreSQL:

# Valida que tengas la librería psycopg2 usando el comando import. Si no está instalada en tu ambiente, usa el comando !pip install psycopg2 en la terminal de python para instalarlo.

# Comenzamos cargando las librerías:

import pandas as pd
import psycopg2

# Luego creamos el elemento de conexión con el siguieente código:

sql_conn = psycopg2.connect(user = "user_name",
                            password = "password",
                            host = "xxx.xxx.xxx.xxx",
                            port = "5432",
                            database = "postgres_db_name")

# Seguido simplemente definimos nuestra query en SQL:

query_sql = '''
select *
from table_name
limit 10
'''

# Y creamos nuestro dataframe:

df = pd.read_sql(query_sql, sql_conn)
df.head(5)

# After work update or create

data.to_sql(con=sql_conn, name='student2', if_exists='append', index=False)
# append sirve para crear y para actualizar
# replace solo sirve para actualizar

# ----------------------------------- SQL Server:
# Valida que tengas la librería pyodbc usando el comando import, si no está instalada en tu ambiente, usa el comando !pip install pyodbc en la terminal python para instalarlo.

# Comenzamos cargando las librerías:
import pandas as pd
import pyodbc

# Luego creamos el elemento de conexión con el siguiente código:

driver = '{SQL Server}'
server_name = 'server_name'
db_name = 'database_name'
user = 'user'
password = 'password'

sql_conn = pyodbc.connect('''
DRIVER={};SERVER={};DATABASE={};UID={};PWD={};
Trusted_Connection=yes
'''.format(driver, server_name, db_name, user, password))

# O si tienes el DSN:

dsn = 'odbc_datasource_name'
sql_conn = pyodbc.connect('''
DSN={};UID={};PWD={};Trusted_Connection=yes;
'''.format(dsn, user, password))

# Seguido simplemente definimos nuestra query en SQL:	

query_sql = 'select * from table_name limit 10'

# Y creamos nuestro dataframe con:

df = pd.read_sql(query_sql, sql_conn)
df.head(5)

# ------------------------------------ Python to SQL

# from sqlalchemy import create_engine
# my_conn = create_engine('mysql+mysqldb://root:test@localhost/my_tutorial')

data = {
    'class':['M', 'N', 'R'],
    'NO':[1,2,3]}

# data.to_sql(con=my_conn, name='student2', if_exists='append', index=False)

# Ya podemos verificar que en SQL ya se encuentre con:

# USE my_tutorial;
# SELECT * FROM student2;
# Y listo, ya podremos visualizarlo.

# Queries desde Python

# query = "SELECT * FROM student WHERE class='Five"
# df.pd.read_sql(query, my_conn)
# print(df)

# df.to_sql(con=my_conn, name='student2, if_exists='apppend', index=False)
# con es de connection
# if exists tmbn puede ser 'replace'


# ----------------- de CSV a Python y de Python a SQL y de SQL a Tableau

# student3 = pd.read_csv('Student.csv')
# df = pd.DataFrame(data=student3)
# df.to_sql(con=my_conn, name='student3', if_exists='append', index= False)
# Abrir Tableau, solo es poner el nombre del server, si
# se requiere user and password, colocar  y elegir la base de datos que se quiere ver
# Trabajar con la base de datos trabajada en Python y especificamente la tabla que se creo 
# y crear visualizaciones

# --------------- Acceso AWS RDS con Python

# ------- Como leer CSV desde AWS S3 directo usando Python boto3

# import boto3

# import boto3
# client = boto3.client('s3')
# path = 's3://carlosman1995bucket/Us_housing.csv'
# df = pd.read_csv(path)
# df

# -------- Como leer un Parquet desde AWS S3 

# import boto3
# import pandas as pd
# import io


# filename = 'my.parquet'
# bucketname = 'carlosmanmz1995bucket'
# buffer = io.BytesIO()
# client = boto3.resource('s3')
# object = client.Object(buckeName, filename)
# object.download_fileobj(buffer)

# df = pd.read_parquet(buffer)
# df

# ----------------------------------- Usando MySQL Cloud database con Python

# import mysql.connector

# mydb = mysql.connector.connect(
#    host= 'bnm3yabltgd51jaxjwli-mysql.services.clever-cloud.com',
#    user = 'carlosmanmz1995',
#    passwd = 'CM81194.42428VM',
#    database = 'sales')

# mycursor = mydb.cursor()

# mycursor.execute('DROP TABLE IF EXISTS customers')
# mycursor.execute('CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))')

# sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
# val = ('John', 'Highway 21')
# mycursor.execute(sql, val)
# mydb.commit()


# sql = " UPDATE customers SET address = 'Canyon 12' WHERE adress = 'Highway 21'"
# mycursor.execute(sql)
# mydb.commit()

# sql = " DELETE FROM customers WHERE name = 'John'"
# mycursor.execute(sql)
# mydb.commit()


# --------------- de Python a AWS S3 Bucket

# import boto3
# import pandas as pd
# import io
# from io import StringIO

# filename = 'MyData.xls'
# bucketName = 'cmv1995bucket'

# csv_buffer = StringIO()
# df.to_csv(csv_buffer)
# client = boto3.client('s3')

# response = client.put_object(
# ACL='private', 
# Body=csv_buffer.getvalue(),
# Bucket=bucketName, 
# Key=filename)

# Verificar en AWS que se encuentre el df


# ------------------------------- Otros formatos:

# CSV - Es muy versatil ya que solo tiene comas y saltos de linea | df.to_csv | pd.read_csv(filename, sep='|', index=False)
# JSON - Tiene un formato muy similar al de un diccionario de Python | df.to_json(dir_pandas.format(test.json)) 
# | pd.read_json(dir_pandas.format(test.json))
# Excel - Permite guardar el archivo en formato .xls para trabajar con el en MS| df.to_excel(dir_pandas.format(test.xlsx)) 
# | pd.read_excel(dir_pandas.format(test.xlsx))
# Pickle - Permite comprimir la información, es util cuando se tienen tablas grandes | df.to_pickle(dir_pandas.format(test.pkl)) 
# | pd.read_pickle(dir_pandas.format(test.pkl))
# Parquet - Permite darle un formato que puede usarse en ambientes Big Data como Hadoop | df.to_parquet(dir_pandas.format(test.parquet)) 
# | pd.read_parquet(dir_pandas.format(test.parquet))
# HDF | df.to_hdf | pd.read_hdr

# ---------------- Formatos de lectura para cargar y guardar DataFrames

# CSV, Excel, Json y demás formatos String : Son simples, requieren alto costo computacional y algo lentos.
# HDF : Gran soporte, adecuado para grandes cantidades de datos, rápido a costo de alto costo computacional.
# Parquet : Puede igualar a hdf e inclusive trabajar por chunks y en paralelo.
# Pickle : Es práctico pero lento con grandes cantidades de datos.

# Tiempos de carga: JSON y CVS al no ser binarios tardaran más, HDF es un formato optimizado
# para trabajar en Big data, de ahi los mas rapidos son Parquet, Pickle y Feather seran los 
# más rapidos.

# Consumo de Memoria RAM: Mas JSON, parquet, feather y pickle son los que menos cuesta leer.


# ---------- Tipos de Variables que componen un data frame

# Buscar BD de Dataset Search de Google

# df.head()
# df.tail()
# df.sample(n)
# df.shape
# df.describe()

pd.options.display.float_format = '{:,.1f}'.format
# ver floats con menos 0's despues del punto.
data.describe()

#incluir string's

data.describe(include='all') 

# Tipo de variables

data.dtypes

# Nueva caracteristica de pandas que permite transformar los datos y agilizarlos

data.convert_dtypes().dtypes

# en lugar de ser objects ahora son strings

# saber el numero de categorias que tiene una variable.

data.nunique() 

data['genero'].unique()

data['genero'].value_counts()

# para codificar rapidamente

code = pd.get_dummies(data['genero'])

# Otra forma (mejor)

np.where(data['genero'] == 'M', 1, 0)


# data['genero'].replace('MASCULINO','M',inplace=True)

# Crear nueva variable

# Numbers = [1,2,3,4,5,6,7]
# data['Number'] = Numbers

# crear una columna que solo tenga 1's

data['ones'] = 1
data

data['code'] = np.where(data['genero'] == 'M', 1, 0)

# cambiar variables de tiempo:
# pd.to_datetime(data['year'], errors = 'coerce', format ='%m/%d/%Y %H:%M:%S %p')

# Renombrar variables

data.rename(columns={'genero':'Genero'}, inplace=True)

list(data)

# Borrar filas, columnas y copiar información

data = data.drop(['ones', 'code', 'Number'], axis=1)

# filas especificas

data.drop([0,2,4,6].head(10))

# borrar variables más filas especificas

data.drop(columns=['edad', 'pais'], index=[0,2,4,6])

df_test = data.copy(deep=True)
# es importante poner copy, porque sino, los cambios
# se se hagan sobre una aplicaran sobre la otra y NO queremos eso, por eso
# es una base de prueba

# ------ Funciones matematicas en DF

data['Q2']**2

np.sin(data['Q2']**2)+10

data['Q2'] - data['Q1']

data['Q2'].iloc[::2]

data['Q2'].iloc[::3].sub(data['Q1'], fill_value=1)

data['Q2']/data['Q1']

data['Q2'].dot(data['Q2'])

# ------- Lamba y funciones más complejas

def fun_1(x):
    y = x**2+1
    return y

fun_1(10)

np.arange(-5, 6).shape

fun_1(np.arange(-5, 6))

# Aplicado en DF

data['Q2'].apply(fun_1)


# Además de apply, también se pueden usar las funciones applymap y map, dependiendo de la necesidad.

# apply() se utiliza para aplicar una función a lo largo de un eje (columna o fila).
# applymap() se usa para aplicar una función a todos los elementos del DataFrame
# map() se usa para sustituir cada valor de una fila por otro valor.

def fun_1(x, a=1, b=0):
    y=x**2+a*x+b
    return y

fun_1(10, a=20, b=-100)

data['Q2'].apply(fun_1, args=(20, -100))

# data['Q2'].apply(fun_1, a=20, b=-100)

# Lambda es una forma de definir una funcion en una sola linea

data['Q2'].apply(lambda x: x+273)

data.columns

# Borramos strings

data = data.drop(['pais', 'genero'], axis=1) 

# Calculamos media a todo el df

data.apply(lambda x: x.mean())

data.applymap(lambda x: x/100)

# ------------------------ Multiples indices

import easygui
easygui.egdemo()

data = pd.read_excel(r'C:\Users\carlvazquez\Documents\Learning\Python\Econometric_DB.xlsx')

data.columns

# idx_filtro = data['Country'].isin(['Aruba', 'Colombia'])
# idx_filtro

# data = data[idx_filtro]
# data - ya solo tenemos esos 2 paises y ahora a crearlo indice.

# data = data.set_index(['Country', 'year'])
# data

# seleccionar por indices:

# data.loc['Colombia',:]

# data.loc['Colombia',:].loc['2016',:]

# data.xs(['Aruba'])

# data.xs(['Arucba', '2018'])

# data.xs('2018', level='year')

data.head()

data = data.set_index(['Year']).sort_index(ascending=True)
data

# ids = pd.IndexSlicedata
# data.loc[ids['Aruba', '2015':'2017'],:].sort_index()

# Obtener datos de un primer nivel, si tuvieramos más indices nos daria los demas en 
# los siguients niveles.

data.index.get_level_values(0)

# Multiples instrucciones a indices segun el nivel

# data['pop']['Colombia']['2018']

# Aplicaciones matematicas en indices

data.sum(level='Year')

# data.unstack('year') cambia el icono de year en columnas donde son los años las colunnas.
# Es el data frame traspuesto.

# Indice: Artificio que en pandas nos da la coordenadas. Esto permite aplicar funciones matematicas en varios niveles.

# ------------------------ STRINGS con Pandas

# Pandas cuenta con una gran funcionalidad a la hora de interactuar con texto, es super versatil si estas interesado en crear modelos de análisis de lenguaje natural.

# Comencemos cargando nuestra librería y creando un diccionario con nombres de personas.

import pandas as pd

data = {'names':['Sara Moreno 34',
                 'jUAn GOMez 23',
                 'CArlos mArtinez 89',
                 'Alfredo VelaZques 3',
                 'luis Mora 56',
                 '@freddier #platzi 10',pd.NA]}

# Usemos los datos del diccionario para crear nuestro DataFrame. Nuestro DataFrame contiene una columna tipo texto, con variedades de caracteres especiales, números, 
# mayúsculas e inclusive variables nulas.

df = pd.DataFrame(data)

# Para usar las funciones asociadas a texto usamos str en nuestro DataFrame, por ejemplo, si se quiere colocar el texto en minúscula, basta con escribir:

df['names'].str.lower()

# Para mayúsculas igualmente:

df['names'].str.upper()

# O si queremos solo la primera letra en mayúscula:

df['names'].str.capitalize()

# Para contar la longitud de nuestro texto usamos:

df['names'].str.len()

# Para dividir el texto por espacios usamos split y definimos el carácter por
# el que queremos dividir, en este caso, un espacio vacío ' ' o '#':

df['names'].str.split(' ')

df['names'].str.split('#')

# Para seleccionar los primeros o últimos 5 caracteres usamos:

df['names'].str[:5]

df['names'].str[-5:]

# Podemos reemplazar una secuencia de caracteres por otra mediante:

df['names'].str.replace('Alfredo','Antonio')

# También podemos buscar una secuencia de texto en específico, en este caso, 'ara':

df['names'].str.findall('ara')


# También podemos crear un filtro basándonos en una secuencia de texto en
# específico, en este caso, las filas que tengan 'or':

df['names'].str.contains('or')

# Así mismo, podemos contar el número de ocurrencias de un caracter en específico,
# por ejemplo, cuántas veces aparece la letra 'a':

df['names'].str.lower().str.count('a')

# Existen comandos más avanzados usando Regex, por ejemplo, si quiero extraer los
# caracteres numéricos:

df['names'].str.extract('([0-9]+)', expand=False)

# O, por ejemplo, si quiero extraer las menciones '@xxxx' del texto:

df['names'].str.replace('@[^\s]+','')

# Analisis de Texto - next step --- Procesamiento de Lenguaje Natural con Python y NLTK.

# --------- Concatenación de DataFrames: concat y append

np.set_printoptions(precision=1)

x1 = np.random.rand(2,5)*100

x2 = np.random.rand(2,5)*-100

np.concatenate([x1, x2])

np.concatenate([x1, x2], axis=1).shape

s1 = pd.Series(x1[0], index=['a', 'b', 'c', 'd', 'e'])
# [0] eligo la primera fila

s2 = pd.Series(x2[0], index=['c', 'd', 'e', 'f', 'g'])

pd.concat([s1, s2])

pd.concat([s1, s2], axis=1)

# eliminar indices

s1.reset_index(drop=True)

pd.concat([s1.reset_index(drop=True), s2.reset_index(drop=True)], axis=1)

df1 = pd.DataFrame(np.random.rand(3,2)*-1, columns=['a', 'b'], index=[2,3,4])

df2 = pd.DataFrame(np.random.rand(3,2)*10, columns=['a', 'b'])

# indices se comparten 

pd.concat([df1, df2])

# indices no se comparten

pd.concat([df1, df2], axis=1)

# encontrar valores donde se compartan indicen unicamente, sin NA's

pd.concat([df1, df2], axis=1, join='inner')

# sin indices establecidos

pd.concat([
    df1.reset_index(drop=True),
    df2.reset_index(drop=True)
], axis=1)

# append pega la segunda matrix debajo de la primera.

df1.append(df2)

# Y puedes continuar pegando valores

df1.append(df2).append(df2)

# Traspuesta

df1.T

df1.T.append(df2.T).T

# Normalmente tenemos distintas fuentes de datos y tenemos que unificar.

# -------------- Merge de DataFrames

df_left = pd.DataFrame(
    {'X':['x0','x1','x2','x3'],
    'W':['w0','w1','w2','w3'],
    'Y':['y0','y1','y2','y3'],
    'Mix':['y2','y3','a2','a3']},
    index = ['y2','y3','a2','a3'])

df_right = pd.DataFrame(
    {'Z':['z2','z3','z4','z5'],
     'A':['a2','a3','a4','a5'],
     'Y':['y2','y3','y4','y5']},
    index = [2,3,4,5])

# por default la union es inner

# siempre se deben tener llaves clave para hacer los joins:

# inner
# outer (todo)
# left 
# right

pd.merge(df_left, df_right)

pd.merge(df_left, df_right, how='inner', on='Y')

pd.merge(df_left, df_right, how='inner', left_on='Mix', right_on='Y')

pd.merge(df_left, df_right, how='inner', left_on='Mix', right_on='A')

# left 

pd.merge(df_left, df_right, how='left', on='Y')

# right
pd.merge(df_left, df_right, how='right', on='Y')

# outer
pd.merge(df_left, df_right, how='outer', on='Y')

pd.merge(df_left, df_right, how ='outer', on = 'Y', suffixes=['_left','_right'])

# Unificar DF's a traves de un parametro en comun (llaves primarias y secundarias)

# --------------- ¿Cómo lidiar con datos faltantes en tus DataFrames?

# Es muy común que nuestros DataFrames presenten datos faltantes, antes de empezar a procesar nuestros DataFrames veamos un poco en qué consisten los objetos NaN (Not a Number).

# Importemos las librerias Pandas y Numpy para esto:

import numpy as np
import pandas as pd

# Un número que no está definido usualmente se representa con el siguiente objeto:

np.nan

# ¡Este objeto tiene propiedades matemáticas! Al sumar un número, obtenemos como
# respuesta el mismo NaN.

np.nan + 0

# La versión 1.0 de pandas incluye un nuevo objeto NA, que es mucho más
# general pues, ademas de interactuar con números, tambien puede hacerlo con
# cadenas de texto u otras varaibles como las de tipo booleano. Si quieres que
# esta nueva definición este incluida entre tus cálculos usa:

pd.options.mode.use_inf_as_na = True

# Al sumar NA a una cadena de texto, obtengo el mismo NA:

pd.NA +'Hola mundo'

# A continuación, vamos a crear un DataFrame

df = pd.DataFrame(np.arange(0, 15).reshape(5, 3), columns=['a', 'b', 'c'])
df


# Y vamos a añadir algunas variables no definidas:

df['d'] = np.nan
df['e'] = np.arange(15, 20)
df.loc[5,:] = pd.NA
df.loc[4,'a'] = pd.NA
df.loc[0,'d'] = 1
df.loc[5,'d'] = 10
df

# Para reconocer cuando un objeto es nulo simplmente usamos:

df.isnull()

# En dónde todas nuestras variables no definidas fueron marcadas con TRUE,
# df.isna() tambien cumple esta función.

# Conocer el número de variables nulas por columna puede hacerse juntando el
# comando anterior con la funcion de suma:

df.isnull().sum()

# Si lo que nos interesa es conocer el número de filas con elementos nulos, basta con usar axis=1:
df.notnull().sum(axis=1)

# O todos los elementos nulos de nuestro DataFrame:

df.size-df.isnull().sum().sum()

# Reconocer estos elementos nos puede ayudar a filtrar en nuestro DataFrame, en este caso, me gustaría 
# filtrar por las variables no nulas de la columna ‘a’:

df[df['a'].notnull()]

# dropna es perfecto para elimnar rapidamente las filas con registros faltantes:

df.dropna()

df[['a']].dropna()

# Ya que hemos visto cómo funcionan las variable nulas, veamos cómo lidiar con
# ellas. Usando la función fillna podremos reemplazarlas por el valor que
# querramos, en este caso 0.

df.fillna(0)

# Si quisieramos remplazar con el valor siguiente usamos method="ffill":

df.fillna(method="ffill")

# Si quisieramos remplazar con el valor previo usamos method="bfill":

df.fillna(method="bfill")

# El mismo ejercicio anterior se puede aplicar con las filas usando axis=1:

df.fillna(method="bfill",axis=1)

# Podemos usar también una serie para reemplazar los valores de una columna en especifico, 
# es importante que haya emparejamiento entre los índices:

fill = pd.Series([100, 101, 102])
fill

df['d'] = df['d'].fillna(fill)
df['d'] 

df

# Una de las formas más usadas para reemplazar datos es usar el promedio de las columnas, 
# esto se hace con la función mean. O si se quiere un mejor estimador, usamos median.

df.fillna(df.median())

# Por último, Pandas también puede interporlar los valores faltanes calculando el valor que puede haber existido en el medio.

df_d = pd.concat([df[['d']], df[['d']].interpolate()],axis=1)
df_d.columns = ['d_antes','d_interpolado']
df_d

# ----------- Group By

dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}

data = pd.DataFrame(dict_data)

data.groupby('pais').mean()

data.groupby('genero').median()

data.groupby('genero')['cm'].count()

for i in[0,1,2,3, 'Hola']:
    print(i)

for key_group, group in data.groupby('pais'):
    grouped_edad = group['Q2'].mean()
print('pais: {}, Q2{}\n'.format(key_group, grouped_edad))

# Excelentes agrupaciones

data.groupby(['pais', 'genero'])['Q2'].mean().to_frame()

data.groupby(['pais', 'genero'])['Q2'].aggregate(['min', np.mean, max])

# Añadir funciones en agrupaciones

def mean_group(x):
    return np.mean(x)/100

data.groupby(['pais', 'genero'])['Q2'].aggregate(['min', np.mean, mean_group, max])

# Agregar diccionario de funciones que nos gusta ocupar

dict_agg = {'cm':[min, max], 'edad':[np.mean, mean_group]}

data.groupby(['pais', 'genero']).aggregate(dict_agg)

# Crear filtros

def f_filter(x):
    return mean_group(x['edad'])>1

data.groupby('pais').filter(f_filter)


# -------------------- Cómo lidiar con datos duplicados en Pandas

# Es muy usual que los registros de una base de datos aparezcan más de una vez, así que veamos cómo pandas puede ayudarnos a 
# lidiar con estos casos. Para comenzar, importemos pandas y creemos un DataFrame con dos columnas y algunos datos repetidos.

import pandas as pd

df = pd.DataFrame({'a': ['w'] * 4 + ['x'] * 3 + ['y'] * 2 + ['z']+['v'], 
                   'b': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4,5]})
df

# Para encontrar los registros duplicados usamos duplicated , que marca con True aquellos casos de filas duplicadas:

df.duplicated()

# Podemos usar keep='first' para marcar solo la primera ocurrencia o keep='last' para marcar la última:

df.duplicated(keep='first')

df.duplicated(keep='last')

# Identificados los casos duplicados, podemos usar este resultado para filtrar y seleccionar aquellos que no tienen un registro duplicado:

df[~ df.duplicated()]

# Si quisieras dejar el primer registro de los duplicados o el último, recuerda usar keep='first' o keep='last'. 
# Remarco el hecho de que usé negación '~' para ver los registros no duplicados.

# Y si me interesara ver cuáles son los registros duplicados, podemos usar keep=False:

df.duplicated(keep=False)

df[df.duplicated(keep=False)]

# Por último, puedes usar el comando 'drop_duplicates' para eliminar los duplicados. 
# Por defecto, la función guarda el primer resultado keep='first':

df.drop_duplicates()

# Y si quieres solo borrar duplicados teniendo en cuenta una sola columna, lo puedes hacer mediante una 
# lista nombrando las columnas donde vas a eliminar los duplicados, en este caso, ['a']:

df.drop_duplicates(['a'],keep='last')

# ------------------------ Aggregation y groupby

# % del total

data['genero'].value_counts() / data['genero'].value_counts().sum()*100

data.groupby('genero').mean()

data.groupby('genero')[['cm', 'Q2']].describe()

# Agrupar con funciones matematicas

def mean_transform(x):
    return np.mean(x)*1.12

data.groupby('genero')[['cm', 'Q2']].apply(mean_transform)

data.groupby('genero')[['cm', 'Q2']].apply(lambda x: np.mean(x)*1.12)

# sI queremos ocupar más de una funcion

data.groupby('genero')[['cm', 'Q2']].aggregate([np.mean, np.max])


# ------------- Group By: extraer valor con variables categóricas

# Truco con Ones

data['ones'] = 1

df_g = data.groupby(['genero', 'pais'])[['ones']].sum()
df_g


df_g.groupby(level=0).apply(

    lambda x:
    x/x.sum()*100
)

# Crear grupos y categorias

data.head()

pd.cut(data['cm'], bins=3).value_counts()

# definir el ancho de nuestras categorias

pd.cut(data['cm'], bins=[110, 120, 155]).value_counts()

data['cut'] = pd.cut(data['cm'], bins=[110, 120, 155])

data.head()

# --------------------- Tablas dinámicas con Pivot Table

df = data.groupby(['genero', 'pais'])[['Q2']].mean().reset_index()

df

# Por default te da mean

df.pivot_table(values='Q2', index='genero', columns='pais')

# Probemos con otras funciones

df.pivot_table(values='Q2', index='genero', columns='pais', aggfunc=[np.median, np.std])

# -------------- Series de tiempo

# df_time = df.groupby('ObservationDate').sum()
# df_time.head(5)

# df1 = df_time['Confirmed'].iloc[10:15]
# df1

# df2 = df_time['Deaths'].iloc[12:17]
# df2

# df1 - df2

# df_time.diff().mean()

# df_diff = df_time.diff()
# df_diff

# df_time.head(1).to_dict()

# df_diff = df_diff.fillna({'Confirmed': 555.0,
# 'Deaths': 17.0,
# 'Recovered': 28.0})

# df_diff.cumsum()

#  df_diff.resample('M').sum()

#  df_diff.resample('M').count()

#  df_diff.resample('M').mean()

#  df_cum = df_time.resample('12h').sum(min_count=1)
# df_cum

# df_cum = df_cum.interpolate()
# df_cum

# df_cum['rate'] = 1 - df_cum['Deaths']/df_cum['Confirmed']

# df_cum = df_cum.reset_index()
# df_cum

# -----------------------------------------  Visualizacion

# df_cum.groupby(pd.Grouper(key='ObservationDate', freq = 'M'))[['rate']].mean()

# rolling permite hacer promedios con ventanas de frecuencias
# sr = series

# sr = df_cum.groupby(pd.Grouper(key='ObservationDate', freq = '1D'))['rate'].mean()
# sr.plot()

# sr.plot()
# sr.rolling(window=7).mean().plot()
# sr.rolling(window=14).mean().plot()

# sr.rolling(window=14).apply(lambda x: np.std(x)).plot()

# df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False)

# df_time = df.groupby(['Country/Region',
#             pd.Grouper(key='ObservationDate',freq='1D')]).sum()
# df_time

# df_china = df_time.loc['Mainland China',:]

# df_china.plot(figsize = (10,7), title = 'CODV-19')
# plt.xlabel('Date')
# plt.ylabel('People')
# plt.show()

# ax = df_china.plot(figsize = (10,7), title = 'CODV-19',
#               legend = False,
#               style = ['r-','g--','b:*'])
# ax.legend(['1','dos','3'])
# plt.xlabel('Date')
# plt.ylabel('People')
# plt.show()

# df_monthly = df_china.resample('M').max()
# df_monthly

# df_monthly['Traitment'] = df_monthly['Confirmed'] - df_monthly['Deaths']- df_monthly['Recovered']
# df_monthly

# df_china['rate'] = 1- df_china['Deaths']/df_china['Confirmed']
# df_china['rate'].hist(figsize = (10,7), bins = 10)

# df_china['rate'].plot(kind = 'kde', figsize = (10,7))


# -------------------- EXAMEN 

data['Q1'].astype('category')

np.array([10, 8, 5,0])*np.array([0,1,6,12])

pd.Series([10,8,5,0])-pd.Series([0,1,6,12])

[10,8,5,0] + [0,1,6,12]

data.columns

data = data.drop(columns=['cut'])

pd.NA | False

df = pd.DataFrame({
    'edad' :     [ 10, 9, 13, 14, 12, 11, 12],
    'cm' : [ 115, 110, 130, 155, 125, 120, 125],
    'pais' :    [ 'co', 'mx', 'co', 'mx', 'mx', 'ch', 'ch'],
    'genero' :  [ 'F', 'M', 'M', 'M', 'F', 'F', 'F'],
    'Q1' : [ 5, 10, 8, np.nan, 7, 8, 3],
    'Q2' : [ 7, 9, 9, 8, 8, 8, 9.]
}, index = ['Ana','Benito','Camilo','Daniel','Erika','Paola','Gabriela'])

print(df['edad'] >= 12)

df.convert_dtypes()

df.groupby(['genero'])['cm'].agg([np.mean, np.std])

df.describe()

print(df.iloc[[4],[2]])

df.dtypes

df[(df['edad']>12) & (df['pais']=='mx')]

df.groupby(['genero'])[['edad']].mean()

df1 = pd.DataFrame({
    'edad' :     [ 10, 9, 13, 14, 12, 11, 12],
    'cm' : [ 115, 110, 130, 155, 125, 120, 125],
    'pais' :    [ 'co', 'mx', 'co', 'mx', 'mx', 'ch', 'ch'],
    'genero' :  [ 'F', 'M', 'M', 'M', 'F', 'F', 'F'],
    'Q1' : [ 5, 10, 8, np.nan, 7, 8, 3],
    'Q2' : [ 7, 9, 9, 8, 8, 8, 9.]
}, index = ['Ana','Benito','Camilo','Daniel','Erika','Paola','Gabriela'])

print(df.loc[['Ana'],['cm']])

pd.concat([df, df1])

[df1]+[df]

print(df.query("(edad >= 12) & (cm < 130) & (Q1 > 5)")['Q2'])

df.shape

df.set_index(['genero', 'pais']).sort_index()