from pandas_datareader import data
from datetime import date, datetime
import numpy as np
import sqlite3, os.path

startdate = '2012-01-01'
today = date.today().strftime("%Y-%m-%d") 
enddate = today

def connectDB():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "history.db")
    conn = sqlite3.connect(db_path)
    return conn

def createDB():
    conn = connectDB()
    cursor = conn.cursor()
    print('Creating Database Tables')
    cursor.execute("""CREATE TABLE RESULTS (
    Date   DATE,
    Time   TIME,
    Ticker VARCHAR,
    High   REAL,
    Low    REAL,
    Close  REAL,
    Model  VARCHAR,
    R2     REAL)""")
    conn.commit()
    cursor.execute("""CREATE TABLE MODEL_SETTINGS (
    Model    VARCHAR,
    max_iter INTEGER,
    alpha    REAL,
    tol      REAL,
    l1_ratio REAL)""")
    conn.commit()

def addDatatoDB(date, time, ticker, predictions):
    conn = connectDB()
    cursor = conn.cursor()
    query = """INSERT INTO RESULTS (Date, Time, Ticker, High, Low, Close, Model, R2) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    data_tuple = (date, time, str(ticker).upper(), float(predictions[0]), float(predictions[1]), float(predictions[2]), str(predictions[3]), float(predictions[4]))
    try:
        cursor.execute(query, data_tuple)
    except:
        createDB()
        cursor.execute(query, data_tuple)

    conn.commit()
    cursor.close()

def dateArrange(data):
    dates = data['Date'].to_list()
    epochDates = []
    for i in dates:
        date_time = np.datetime64(i).astype(datetime)
        splitDate = date_time.strftime("%Y-%#m-%d").split('-')
        epochDate = datetime(int(splitDate[0]),int(splitDate[1]),int(splitDate[2]),0,0).timestamp()
        epochDates.append(epochDate)
    data['Date'] = epochDates

def dataScraper(ticker):
    try:
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
    except:
        print('Failed to Scrape Stock Data, Check Internet Connection.')
        return
