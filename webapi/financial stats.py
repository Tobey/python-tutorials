import codecademylib3_seaborn
import pandas as pd
from datetime import datetime
import pandas_datareader.data as web
import pandas_datareader.wb as wb
import numpy as np


gold_prices = pd.read_csv('gold_prices.csv')

crude_oil_prices = pd.read_csv('crude_oil_prices.csv')

start= datetime(1999, 1, 1)
end= datetime(2019, 1, 1)

nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)

sap_data = web.DataReader('SP500', 'fred', start, end)

gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)

export_data = wb.download(indicator='NE.EXP.GNFS.CN.', country=['US'], start=start, end=end)

print(export_data)
print(gold_prices)
print(crude_oil_prices)

def log_return(prices):
  return np.log(prices / prices.shift(1))

gold_returns =log_return(gold_prices['Gold_Price'])
crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN.'])
gdp_data_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
sap_data_returns = log_return(sap_data['SP500'])
nasdaq_data_returns = log_return(nasdaq_data['NASDAQ100'])

print('gold:', gold_returns.var())
print('crude oil:', crude_oil_returns.var())
print('export:', export_returns.var())
print('gdp data:', gdp_data_returns.var())
print('sap_data:', sap_data_returns.var())
print('nasdaq data:', nasdaq_data_returns.var())