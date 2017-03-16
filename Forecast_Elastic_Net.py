import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read in the data
df = pd.read_csv('Forex.csv')

# Have a look at the Data(structure)
df.head()
# Convert the Month Field to an integer or double
# Code ***

# A sample implementation with integer
df['FloatDate'] = 1 ,2 , 3 , 4 , 5 , 6 , 7 , 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27

from sklearn.linear_model import LinearRegression
slr = LinearRegression()

X = df[['FloatDate']].values
y = df[['#Price']].values


slr.fit(X, y)
print('Slope: %.3f' % slr.coef_[0])
print('Intercept: %.3f' % slr.intercept_)

def lin_regplot(X, y, model):
    plt.scatter(X, y, c='red')
    plt.plot(X, model.predict(X), color='blue')
    return None

lin_regplot(X, y, slr)
plt.xlabel('# Float Date')
plt.ylabel('Price')
plt.show()

# Linear Regression equation is
# y = mx + c

# c -- y intercept
# m -- slope
# x -- input values
# y -- is our expectations
Date_MM_YYYY = 35
price_ksh = slr.predict(Date_MM_YYYY)

print("The Kenya shilling in Date 35 is %.3f" % price_ksh)

# Implementation in ElasticNetCv
from sklearn.linear_model import ElasticNet
alpha = 0.001

EnetCv = ElasticNet(alpha=alpha)

price_predict = EnetCv.fit(X,y).predict(35)

print("The Kenya shilling in Date 35 is(Using ElsticNet) %.3f" % price_predict)