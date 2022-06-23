from datetime import datetime
import numpy as np

def dateArrange(data):
    dates = data['Date'].to_list()
    epochDates = []
    for i in dates:
        date_time = np.datetime64(i).astype(datetime)
        splitDate = date_time.strftime("%Y-%#m-%d").split('-')
        epochDate = datetime(int(splitDate[0]),int(splitDate[1]),int(splitDate[2]),0,0).timestamp()
        epochDates.append(epochDate)
    data['Date'] = epochDates
    #print(data)