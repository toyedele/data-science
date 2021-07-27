# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:39:13 2021

@author: Taofeek Oyedele

Data set: Honey Production in the USA (1998-2012)
Data Source: Kaggle

Aim: 
    what is the relationship between honey produced and time
    predict how much honey will be produced in 2050

Method: Linear Regression model

Conclusion: 
    honey produced decreases over time with a correlation of -0.76
    186,545 honey are expected in 2050
    
    

Room for improvement: split the data into train and test datasets
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression as lregr

df = pd.read_csv(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\us_honey_production.csv')


def scoping_the_data():
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.count().duplicated() )
    print(df.count().isnull())
    print(df.columns)
    
    missing_data = df.isnull().sum().to_frame()
    missing_data = missing_data.rename(columns={0:'Empty Cells'})
    print(missing_data)
    

    plt.title("Brief overview of the data")   
    sns.scatterplot(data=df, x='year', y='totalprod')
    plt.show()
       
scoping_the_data() 

prod_per_year = df.totalprod.groupby(df.year).mean().reset_index()
print(prod_per_year.head())



print('\n The correlation between honey produced and time is {}\n'\
      .format(prod_per_year.year.corr(prod_per_year.totalprod)))
    
    
# reshaping the format of years
years = prod_per_year.year.values.reshape(-1,1) 

honey_produced = prod_per_year.totalprod

# regression
model = lregr()
model.fit(years,honey_produced)
print('The coefficient and y_intercept are {} & {} respectively'.format(int(model.coef_[0]),int(model.intercept_)))

honey_predict = model.predict(years)

#display results
sns.scatterplot(data=prod_per_year, x='year', y='totalprod')
plt.plot(years,honey_predict, c='r')
plt.title('Linear regression of honey produced vs years')
plt.show()

# prediction
future_years = np.array(range(2013,2051))
future_years = future_years.reshape(-1,1)

future_honey_production = model.predict(future_years)
print('\n{} honey are expected in 2050'.format(int(future_honey_production[-1])))
