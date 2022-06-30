#def warn(*args, **kwargs):
#    pass
#from re import I
#import warnings
#warnings.warn = warn

from dataScraper import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from model_settings import *

prediction_list = []
typed_ticker = [] 

def predictor(stock_ticker):
    global prediction_list, ticker, lasso_settings, elastic_settings
    
    prediction_list = []
    ticker = stock_ticker
    typed_ticker.append(ticker)
    stock_data = dataScraper(stock_ticker)
    
    if model_selection[0] == 'Lasso':
        from sklearn.linear_model import Lasso
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
            'Close (Adjusted)': stock_data.iloc[1: , :]['Close']
        }
        sample = stock_data.iloc[-1:, :]

        for i in y:
            X_train, X_test, y_train, y_test = train_test_split(X, y[i], test_size=test_size)

            y_pred_lasso = lasso.fit(np.array(X_train), np.array(y_train))
            r2_score_lasso = r2_score(np.array(y_test), y_pred_lasso.predict(np.array(X_test)))
            prediction = y_pred_lasso.predict(np.array(sample))
            prediction_list.append(prediction)
            #print(i + ' - ' + str(prediction) + '\n')
        prediction_list.append(lasso)
        prediction_list.append(r2_score_lasso)
    if model_selection[0] == 'ElasticNet':
        from sklearn.linear_model import ElasticNet
        alpha = float(elastic_settings['alpha'])
        tol = float(elastic_settings['tol'])
        max_iter = int(elastic_settings['default_iter'])
        l1_ratio = float(elastic_settings['l1_ratio'])
        enet = ElasticNet(alpha=alpha, tol=tol, max_iter=max_iter, l1_ratio=l1_ratio)

        test_size = 0.1

        print('\nModel = ' + str(enet))
        #print('R2 = ' + str(r2_score_lasso))
        #print('\n~ ' + stock_ticker.upper() + ' Next Day Price Predictions ~\n')

        X = stock_data.iloc[:-1 , :]
        y = {
            'High' : stock_data.iloc[1: , :]['High'], 
            'Low' : stock_data.iloc[1: , :]['Low'], 
            'Close (Adjusted)': stock_data.iloc[1: , :]['Close']
        }
        sample = stock_data.iloc[-1:, :]

        for i in y:
            X_train, X_test, y_train, y_test = train_test_split(X, y[i], test_size=test_size)

            y_pred_enet = enet.fit(np.array(X_train), np.array(y_train))
            r2_score_enet = r2_score(np.array(y_test), y_pred_enet.predict(np.array(X_test)))
            prediction = y_pred_enet.predict(np.array(sample))
            prediction_list.append(prediction)
            #print(i + ' - ' + str(prediction) + '\n')
        prediction_list.append(enet)
        prediction_list.append(r2_score_enet)
    
    today = date.today().strftime("%Y-%m-%d") 
    current_time = datetime.now().strftime("%H:%M:%S")
    addDatatoDB(today, current_time, ticker, prediction_list)
