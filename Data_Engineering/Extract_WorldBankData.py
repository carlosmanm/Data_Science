# import wbgapi as wb

# wb.series.info('NY.GDP.PCAP.CD')           # GDP
# wb.economy.info(['CAN', 'USA', 'MEX'])     # Countries in North America

# wb.series.info(q='women')
# wb.economy.info(q='congo')


# ------------- Accessing data

# for row in wb.data.fetch('SP.POP.TOTL', 'USA'): # all years
#    print(row)

# ---------------- Creating data frame: also Code for Power BI

import wbgapi as wb
import pandas as pd

data = wb.data.DataFrame(['NY.GDP.PCAP.CD', 'SP.POP.TOTL'], 'USA', mrv=50)

data["Country"] = "USA"

data = pd.melt(data, id_vars=['Country'], var_name='years', value_name='value')

data['Year'] = data['years'].str[-4:]

data = data.filter(['Country', 'value', 'Year'])

data = data.reindex(columns=['Country', 'Year', 'value'])

# mrv = most recent 50 years 

# ----------- Case 2

data2 = wb.data.DataFrame('SP.POP.TOTL', wb.region.members('AFR'), range(2010, 2020, 2))

data2.head()
data2.shape

# ----------- Case 3
data3 = wb.data.DataFrame(['SP.POP.TOTL', 'EN.ATM.CO2E.KT'], time=range(2000, 2020), skipBlanks=True, columns='series')
data3




