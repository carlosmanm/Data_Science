import pandas as pd
import numpy as np
import seaborn as sn
import mysql.connector as sql
from sqlalchemy import create_engine
import sqlalchemy as sqla
import matplotlib.pyplot as plt

# BBDD

# Conexion


mydb = sql.connect(host="localhost", user="root", password="radio.1495", database="course")

query = "Select * from clientes;"
query2 = "Select * from pedidos;"
query3 = "Select * from productos;"

data = pd.read_sql(query,mydb)
data2 = pd.read_sql(query2,mydb)
data3 = pd.read_sql(query3,mydb)

data.head()
data2.head()
data3.head()

plt.hist(data3["SECCION"], facecolor='blue', alpha=0.5)
plt.show()

data3['SECCION'].value_counts()

