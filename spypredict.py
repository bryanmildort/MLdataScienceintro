from dataScraper import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

print('Enter Ticker To Scrape: ')
stock_ticker = input()

stock_data = dataScraper(stock_ticker)

X = stock_data.iloc[:-1 , :]
y = stock_data.iloc[1: , :]['Adj Close']

test_size = 0.1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

alpha = 0.1
tol = 0.0017
max_iter = 1000
lasso = Lasso(alpha=1, max_iter=max_iter, tol=tol)

y_pred_lasso = lasso.fit(np.array(X_train), np.array(y_train))
r2_score_lasso = r2_score(np.array(y_test), y_pred_lasso.predict(np.array(X_test)))

print(lasso)
print(r2_score_lasso)