import pandas as pd
import numpy as np
import seaborn as sn
import mysql.connector as sql
from sqlalchemy import create_engine
import sqlalchemy as sqla


# engine = create_engine('mysql://name:password@hostname/database')

db_connection = sqla.create_engine('mysql+mysqlconnector://root:radio.1495@localhost/books')

df = pd.read_sql_table("authors", db_connection)

df.head()

df.describe

df.shape

# Queries

with db_connection.connect() as connection:
    result = connection.execute("SELECT * from books")
    for row in result:
        print(row)

#-----------------------------

mydb = sql.connect(host="localhost", user="root", password="radio.1495", database="books")

query = "Select * from clients;"

result_dataFrame = pd.read_sql(query,mydb)

result_dataFrame.head()

result_dataFrame.shape


