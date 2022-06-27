def warn(*args, **kwargs):
    pass
from re import I
import warnings
warnings.warn = warn

from dataScraper import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

from model_settings import lasso_settings

#stock_ticker = input('Enter Ticker To Scrape: ').upper()
prediction_list = []
typed_ticker = [] 

def predictor(stock_ticker):
    global prediction_list
    global ticker
    global lasso_settings
    
    prediction_list = []
    ticker = stock_ticker
    typed_ticker.append(ticker)
    stock_data = dataScraper(stock_ticker)

    alpha = float(lasso_settings['alpha'])
    tol = float(lasso_settings['tol'])
    max_iter = int(lasso_settings['default_iter'])
    lasso = Lasso(alpha=alpha, max_iter=max_iter, tol=tol)

    test_size = 0.1

    print('\nModel = ' + str(lasso))
    #print('R2 = ' + str(r2_score_lasso))
    #print('\n~ ' + stock_ticker.upper() + ' Next Day Price Predictions ~\n')

    X = stock_data.iloc[:-1 , :]
    y = {
        'High' : stock_data.iloc[1: , :]['High'], 
        'Low' : stock_data.iloc[1: , :]['Low'], 
        'Close (Adjusted)': stock_data.iloc[1: , :]['Adj Close']
    }
    sample = stock_data.iloc[-1:, :]

    for i in y:
        X_train, X_test, y_train, y_test = train_test_split(X, y[i], test_size=test_size)

        y_pred_lasso = lasso.fit(np.array(X_train), np.array(y_train))
        r2_score_lasso = r2_score(np.array(y_test), y_pred_lasso.predict(np.array(X_test)))
        prediction = y_pred_lasso.predict(np.array(sample))
        prediction_list.append(prediction)
        #print(i + ' - ' + str(prediction) + '\n')