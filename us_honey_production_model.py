# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:39:13 2021

@author: Taofeek Oyedele

Data set: Honey Production in the USA (1998-2012)
Data Source: Kaggle

Aim: 
    what is the relationship between honey produced and time
    predict how much honey will be produced in 2050

Hypothesis:
    Null: There's no relationship between honey produced and years
    Alternative: There's a relationship between honey produced and years

Method: 
    Linear Regression model

Conclusion: 
    Looking at the R^2, we have 0.58. Therefore, about 60% of the variability of honey produced is explained by the time
    The p-value for year is very low and less than 0.05, therefore I reject the null hypothesis as the time when the honey is produced is statistically significant
    Trend wise, the amount of honey produced decreases over time with a correlation of -0.76
    Finally in 2050, on average 186,545 honey will be produced
        
Room for improvement: split the data into train and test datasets
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression as lregr
from sklearn import metrics
import statsmodels.formula.api as smf

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



print('\n The correlation between honey produced and time is',\
      round(prod_per_year.year.corr(prod_per_year.totalprod),3))
    
    
# reshaping the format of years
years = prod_per_year.year.values.reshape(-1,1) 

honey_produced = prod_per_year.totalprod

# regression
model = lregr()
model.fit(years,honey_produced)
print('\nThe coefficient and y_intercept are {} & {} respectively'.format(int(model.coef_[0]),int(model.intercept_)))

honey_predict = model.predict(years)

#display results
sns.scatterplot(data=prod_per_year, x='year', y='totalprod')
plt.plot(years,honey_predict, c='r')
plt.title('Linear regression of honey produced vs years')
plt.show()

# evaluation
print('\nMean Squared Error: ',int(metrics.mean_squared_error(honey_produced, honey_predict)))
print('Root Mean Squared Error: ',int(np.sqrt(metrics.mean_squared_error(honey_produced, honey_predict))))
r_squared = round(model.score(years, honey_produced, sample_weight=None),2)
print('The R^2 is: ', r_squared)


# model validation and prediction
def validation():
    formula = "totalprod ~ year"
    model_validation = smf.ols(formula = formula, data = prod_per_year).fit()
    
    if r_squared == round(model_validation.rsquared,2):
        print('\nThe model created is successful and the p-values for time is :',round(model_validation.pvalues[-1],3))
        
        if model_validation.pvalues[-1] < 0.05:
            print("Therefore, reject the null")
            
            # prediction
            future_years = np.array(range(2013,2051))
            future_years = future_years.reshape(-1,1)
            
            future_honey_production = model.predict(future_years)
            print('\nIn conclusion, on average {} honey will be produced in 2050 \n'.format(int(future_honey_production[-1])))
        
        else: print("Therefore, fail to reject the null")
            
    else:
        print("\nSomething is wrong with the model and can't be used for prediction")
        
validation()        

