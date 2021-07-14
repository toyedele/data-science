# -*- coding: utf-8 -*-
"""
This section is focused on data manipulation with panda and numpy

Created on Thu Jun 17 15:46:13 2021

@author: Taofeek Oyedele
"""

# data manipulation with panda

# lambda is similar to a normal function except it's a one liner,
# simple function and can't be resued

add_two = lambda add: add + 2

print(add_two(2))

is_string = lambda string : string in 'This is a string'

print(is_string('this'))
print(is_string('is'))

if_else = lambda output : 'it works' if output in 'This is a string' else 'wrong'

print(if_else('is'))

contains_a = lambda check : True if 'a' in check else False

print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))


long_string = lambda str : len(str) > 12 # will return True or False 

print(long_string("short"))
print(long_string("photosynthesis"))

# =============================================================================
# 
# Numpy
# 
# Is an open source python library used for scientific computing due to its 
# efficient data analysis capabilities.
# 
# It has a powerful array called ndarray which can have any number of dimensions
# 
# Panda is a library built on top of Numpy and frequently used alongside numpy
# =============================================================================

# to read a csv file as a df do pd.read_csv('name.csv')

import numpy as np
import pandas as pd

# using ndarray

list = [1,2,3,4]
list_2 = [list, [5,6,7,8]]

np_array = np.array(list)
np_array_2 = np.array(list_2) # converts to a 2D array

print(np_array_2)
print(list_2)

# ndarray are much easier to deal with than python list e.g subtrating 2

toyPrices = np.array([5,8,3,6])
print(toyPrices - 2)

# VS

toyPrices1 = [5,8,3,6]
for i in range(len(toyPrices1)):
    toyPrices1[i] -= 2
print(toyPrices1)

# panda series takes a ndarray and allows you to name each index 

toy_label = pd.Series(toyPrices,index=['shrek', 'lala', 'po','panda'])
print(toy_label)

dataf = pd.DataFrame([
    ['James Corden','13 Upper St',34],
    ['Jane White', '56 Apple Ave',28],
    ['Joey Badox', '89 Broadway',51],
    ['Steve Best','125 Main Road', 25]
    ],
    columns=['name','address','age'])

data_df = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo','James Okay'],
    'address' : ['123 Main St', '456 Maple Avenue', '789 Broadway','125 Main Road'],
    'age': [34,28,51,25]})


print(dataf)
print(data_df)
print(data_df.iloc[-2:])

# selecting few rows and adjusting the index
print("""
      reseting the index
      """)

data1 = data_df.iloc[[0, 2, 1]]
print(data1)

reset = data1.reset_index()
print(reset)

proper_reset = data1.reset_index(drop=True)
print(proper_reset)

# adding a new column

data_df['vaccinated'] = ['yes','no','no','yes']
data_df['double_age'] = data_df.age * 2

print(data_df)

# integrating lambda function to df

get_last_name = data_df.name.apply(lambda last_name : last_name.split()[-1])

data_df['last name'] = get_last_name

print(get_last_name)

# if vaccinated, half their age

half_age = data_df.apply(lambda half : half.age * 0.5
                                 if half['vaccinated'] == 'yes'
                                 else half.age, axis=1)
data_df['half age'] = half_age

print(data_df)

# renaming columns

# data_df.columns = ['Name', 'Address', 'Age', 'Vaccine', 'Double Age', 'Surname'
#                    , 'Half Age']

# or method 2, here i've only changed last name to surname and vaccinated to vaccine

data_df.rename(columns={'last name':'Surname', 'vaccinated':'vaccine'},inplace=True)

print(data_df)

print(data_df.nunique()) # nunique counts the number of unique items

# aggregate function by grouping, can then use reset_index to make it into a DF
data_group = data_df.groupby(['name','vaccine']).age.count().reset_index() 

print(data_group)                   
data_pivot = data_group.pivot(columns='vaccine',index='name',values='age').reset_index()

print(data_pivot)

# merging some col from data_df with dataf

data_col_split = data_df.iloc[:,[2,3,4]] # picks the right cols

df_merge = pd.merge(dataf, data_col_split)

# another way to merge is. This method is better as multiple df can be merged
# at once by doing another .merge("name_df")

df_merge = dataf.merge(data_col_split)

print(df_merge)

"""
however there are multiple ways to merge,
another method is using left_on and right_on
an example is 

orders_products = pd.merge(
  orders, products, left_on = 'product_id',right_on='id', suffixes=['_orders','_products']
)

where orders and products are df and suffixes allow renaming the cols instead 
of id_x and id_y

another method of merging is renaming the col of another df to match
one in the first df

example

orders_products = pd.merge(orders, products.rename(columns={'id':'product_id'}))

these methods can also be use

pd.merge(dataf,data_col_split, how='right') 

where right can change to left, inner or outer
left & right keeps everything from the 1st and 2nd df respectively

inner merges things that are have a common id and outer merges everything
"""

dataf['age'] = [1,2,23,25]
























