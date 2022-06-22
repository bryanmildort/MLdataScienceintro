from datetime import datetime
import pandas as pd

spyData = pd.read_csv('spyData.csv')

def dateArrange(data):
    dates = data['Date'].to_list()
    epochDates = []
    for i in dates:
        splitDate = i.split('/')
        newDate = splitDate[2] + ',' + splitDate[0] + ',' + splitDate[1] + ',0,0'
        epochDate = datetime(int(splitDate[2]),int(splitDate[0]),int(splitDate[1]),0,0).timestamp()
        epochDates.append(epochDate)
    data['epochDates'] = epochDates

dateArrange(spyData)