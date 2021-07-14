# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:14:11 2021

@author: Taofeek Oyedele

Data: Apple share price over the last 10 years

Aim: 
    To find the 50 day moving avarage 
    To categorise the data from daily prices in to monthly and display the result
    To find any seasonality and give potentail investment recommendation
    
Conclusion:
    In conclusion, there is a pattern in the data after a seasonality test was carried out. 
    Most of the data lie within a range of +/- 0.5. 
    Looking further into the data, it’s clear that a strong selling pattern is seen in Q4 of a given calendar year,which is followed by a buy signal in Q1 of the following year. 
    A recommended investment strategy will be long Apple shares at the beginning of the year with the aim to close and enter a short position by the end of Q1. 
    This short position can be held for most of the year but will advise taking profit around November as liquidity typically erodes drastically in December,
    and the cost of getting out of the trade could have a severe impact on the trade’s overall profit.
"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose as sd

# importing and viewing the data
apple_df = pd.read_csv(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\AAPL.csv')

print(apple_df.head())

# 50 day moving average

apple_df['fifty_close_dma'] = apple_df.iloc[:,5].rolling(window=50).mean()
print('\nBelow includes the 50 dma\n')
print(apple_df.head(60))

# getting the data to plot
date = apple_df.Date.values
adj_close_price = apple_df['Adj Close'].values
fifty_dma_close = apple_df.fifty_close_dma.values

# plotting the data
axes = plt.subplot()
plt.plot(date, adj_close_price, c='green')
plt.plot(date, fifty_dma_close, c='blue')
plt.legend(['Adjusted close price', '50 dma'])
axes.set_xticks(range(0,len(date),500))
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('The 50 daily moving average and the adjusted close price vs date')
plt.show()

#converting daily data to monthly data
apple_df['Date'] = apple_df.loc[:'Date'].astype('datetime64[ns]')
data_df = apple_df[['Date', 'Adj Close']]
data_df.set_index('Date',inplace=True)
monthly_data_df = data_df.resample('M').mean()
print('\nBelow is the monthly dataset\n')
print(monthly_data_df.head(12))
plt.plot(monthly_data_df)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('The monthly adjusted closing price')
plt.show()

# decomposing the monthly data and plotting the seasonality of the data
decompose = sd(monthly_data_df, model='additive')
# decompose.plot() # shows the trend, seasonality and noise in the data
decompose.seasonal.plot()
