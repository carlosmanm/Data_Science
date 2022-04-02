# Data Science Tasks

import pandas as pd
import os

# The interview can be sepate in 3 categories of questions (Facebook example):
# ---- Statistic (about multiple regression)
# Example: explain the beta coefficients in a multiple regression | if your target variable
# have zeros in the dataset (actual values) how would you build your model? using a probit and tobit
# models that can handle target variables that are like that. | Can you explain how to interpret
# the confidence interval of the logit regression model? if we have 95% of confidence interval, 
# the actual beta coefficient will fall into the confidence interval that we estimated. Also represents
# the uncertainty around this variable. | presence of 0s in your confidence interval.

# ---- SQL
# ----- Case Problem

# Task 1: Merge the 12 months of sales data into a singles CVS file.

df = pd.read_csv("./Sales_Data/Sales_April_2019.csv")

files = [file for file in os.listdir("./Sales_Data")]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv", index=False)

all_data = pd.read_csv("all_data.csv")
all_data.head()

# Task 2: Clean up the data

# drop nan rows

nan_df = all_data[all_data.isna().any(axis=1)]
nan_df

all_data = all_data.dropna(how='all')

# Delete some error in our column

all_data = all_data[all_data["Order Date"].str[0:2] != 'Or']

# Let's convert columns to the correct type

all_data["Quantity Order"] = pd.to_numeric(all_data["Quantity Order"])
all_data["Price Each"] = pd.to_numeric(all_data["Price Each"])


# Task 3: Add Month Column

all_data["Month"] = all_data["Order Date"].str[0:2]
all_data["Month"] = all_data["Month"].astype("int32")
all_data.head()

# Task 4: What was the best month for sales? How much was earned that month?

# Add a Sales Column

all_data["Sales"] = all_data["Quantity Order"] * all_data["Price Each"]

all_data.groupby("Month").sum()

# all_data.groupby("Month").sum()["Sales"]
 
import matplotlib.pyplot as plt

plt.bar(all_data["Months"], all_data["Sales"])
plt.ylabel("Sales")
plt.xlabel("Months")
plt.show()

# Task: What city sold the most product?



# Task: Export to SQL Server or CSV and After that use 
# in Tableau (in case of not using Matplotlib of Seaborn)

# SQL: pandas.DataFrame.to_sql

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})

df.to_sql('users', con=engine)
engine.execute("SELECT * FROM users").fetchall()

# Or 

with engine.begin() as connection:
    df1 = pd.DataFrame({'name' : ['User 4', 'User 5']})
    df1.to_sql('users', con=connection, if_exists='append')


# CSV: pandas.DataFrame.to_csv


df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})
df.to_csv(index=False)