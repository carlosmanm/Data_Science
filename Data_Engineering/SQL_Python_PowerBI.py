# Import the packages

import pandas as pd
import mysql.connector as sql

# Create the connections 

mydb = sql.connect(host="localhost", user="root", password="Radio.1495", database="marven_cycles")

query = "SELECT * FROM sales19 WHERE Quantity_Sold > 0;"

# Create the dataframe

data = pd.read_sql(query,mydb)

# Let's copy this script and put it on Power BI connections to read this fixed and clean DB!