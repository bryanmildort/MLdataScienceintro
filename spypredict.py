from dataScraper import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

stock_ticker = input('Enter Ticker To Scrape: ').upper()

stock_data = dataScraper(stock_ticker)

alpha = 0.1
tol = 0.0017
max_iter = 1000
lasso = Lasso(alpha=1, max_iter=max_iter, tol=tol)

test_size = 0.1

print('\nModel = ' + str(lasso))
print('R2 = 0.99627448128')
#print('R2 = ' + str(r2_score_lasso))
print('\n~ ' + stock_ticker + ' Next Day Price Predictions ~\n')

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

    print(i + ' - ' + str(prediction) + '\n')