from pandas_datareader import data
from datetime import date

from dateArrange import *

startdate = '2017-01-01'
today = date.today().strftime("%Y-%m-%d") 
enddate = today

def dataScraper(ticker):
    panel_data = data.DataReader(ticker, 'yahoo', startdate, enddate).reset_index()
    price_close = panel_data['Adj Close']
    price_20dma = price_close.rolling(window=20).mean().to_list()[100:] # 20 Day Moving Average
    price_50dma = price_close.rolling(window=50).mean().to_list()[100:] # 50 day
    price_100dma = price_close.rolling(window=100).mean().to_list()[100:] # 100 day
    panel_data = panel_data.iloc[100: , :]
    panel_data['20dma'] = price_20dma
    panel_data['50dma'] = price_50dma
    panel_data['100dma'] = price_100dma
    dateArrange(panel_data)
    return panel_data