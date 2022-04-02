# Get the real price stock

from yahoo_fin.stock_info import *

get_live_price('FB')

# get the last price


# How to know if this company is in the S&P500?

print(tickers_sp500())

stock = input("Please entender a ticker symbol ")

if stock in tickers_sp500():
    print("The stock is in the S&P 500")
else:
    print("Not in S&P 500")


# ------------------ Get historical data: Script for Power BI

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin

yfin.pdr_override()

df = pdr.get_data_yahoo("BTC-USD", start="2019-01-01", end="2022-01-15")

df['Company'] = "BTC-USD"

dates =[]

for x in range(len(df)):
    newdate = str(df.index[x])
    newdate = newdate[0:10]
    dates.append(newdate)

df['Date'] = dates

df = df.reindex(columns=['Company', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

# df.head()

# ------------- Benchmarking

import datetime

start_sp = datetime.datetime(2013, 1, 1)
end_sp = datetime.datetime(2018, 3, 9)

sp500 = pdr.get_data_yahoo('^GSPC', 
                           start_sp,
                             end_sp)
    
sp500.head()

# --------------------- Portfolio Analysis: Code for Power BI

from pandas_datareader import data as web
from datetime import datetime
import numpy as np

assets = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']

stockStartDate = '2013-01-01'

today = datetime.today().strftime('%Y-%m-%d')

df = pd.DataFrame()

for stock in assets: 
    df[stock] = web.DataReader(stock, data_source='yahoo', start = stockStartDate, end = today)['Adj Close']

dates =[]

for x in range(len(df)):
    newdate = str(df.index[x])
    newdate = newdate[0:10]
    dates.append(newdate)

df['Date'] = dates

df = pd.melt(df, id_vars=['Date'], var_name='Company', value_name='value')

df = df.rename(columns = {'value': 'Adj Close'}, inplace = False)

df = df.reindex(columns=['Company', 'Date', 'Adj Close'])
