# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:31:14 2021

@author: Taofeek Oyedele

aim is to improve data visualisation using matplotlib and seaborn
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\test_scores.xlsx')

print(dataset.head())

# reformatting the data

dataset1 = dataset.melt(id_vars='StudentName', var_name='Year', value_name='Score')

print(dataset1.tail())

# sns.barplot(x='StudentName', y='Score', hue='Year', data=dataset, palette='CMRmap_r')


sns.barplot(x='Year', y='Score', hue='StudentName', data=dataset1, palette='CMRmap_r')

plt.show()

# convering a subset to a dictionary which can then be used if needed
dic = {}

dic[dataset.columns[1]] = dataset[['StudentName',2007,2008]]

print(dic)

# task is to plot it as a line graph where x is name and y = score for each year

# use plt.plot, plt.legend and plt.show

# =============================================================================
# Number Code	String for placing the legend
# 0	best
# 1	upper right
# 2	upper left
# 3	lower left
# 4	lower right
# 5	right
# 6	center left
# 7	center right
# 8	lower center
# 9	upper center
# 10	center
# Note: If you decide not to set a value for loc, it will default to choosing the “best” location.
# 
# For, example, we can call plt.legend() and set loc to 6:
# 
# plt.legend([.....], loc=6)
# =============================================================================

x = [1, 1, 2, 3, 5, 8, 7, 10]
y1 = [2,1,2,1,2,5,7,10]
y2 = [5,8,9,4,3,7,10,2]

plt.close('all')
plt.plot(x,y1 ,color='pink', marker='o')
plt.plot(x,y2,color='gray', marker='o')
plt.title("Two Lines on One Graph")
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.legend(["y1", "y2"], loc= 4)
plt.show()

# another example where multiple graphs are plotted as a subplot

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

plt.figure(figsize=(12,8))
ax1= plt.subplot(1,2,1)
x_values = range(len(months))
plt.plot(x_values, visits_per_month, marker='o')
plt.xlabel('month')
plt.ylabel('visits per month')
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Visits per month')
plt.savefig('Visits per month.png')



ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month, color='g')
plt.plot(x_values, persian_limes_per_month, color='black')
plt.plot(x_values, blood_limes_per_month, color='orange')
plt.legend(['key limes per month', 'persian limes per month','blood limes per month' ], loc=9)
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.title('Limes sold per month')
plt.savefig('Limes sold per month.png')

plt.show()

# barchat
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]

plt.bar(store1_x , sales1)

n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element in range(d)]

plt.bar(store2_x , sales2)

plt.show()

# stacked bars
plt.bar(range(len(sales1)),sales1)
plt.bar(range(len(sales1)), sales2, bottom=sales1)
plt.legend(['Location 1', 'Location 2'])

plt.show()

# error bar
error = [0.1*x for x in sales1]
error_2 = [0.1*y for y in sales2]

plt.bar(store1_x, sales1, yerr = error, capsize=5)
plt.bar(store2_x, sales2, yerr = error_2, capsize=5)
ax3 = plt.subplot()
middle_x = [ (a + b) / 2.0 for a, b in zip(store1_x, store2_x)]
ax3.set_xticks(middle_x)
ax3.set_xticklabels(drinks)


plt.show()

# error fill between
ax = plt.subplot()
plt.plot(range(len(sales1)), sales1)
plt.plot(range(len(sales1)), sales2)
ax.set_xticks(range(len(sales1)))
ax.set_xticklabels(drinks)

y_lower = [x - 0.1*x for x in sales1]

y_upper = [x + 0.1*x for x in sales1]

plt.fill_between(range(len(sales1)), y_lower, y_upper, alpha=0.2)

y_lower2 = [x - 0.1*x for x in sales2]

y_upper2 = [x + 0.1*x for x in sales2]

plt.fill_between(range(len(sales1)), y_lower2, y_upper2, alpha=0.2)

plt.show()

# via piet chart
plt.pie(sales1, labels=drinks, autopct='%d%%')
plt.title("The first set of sales")
plt.show()

# # histogram
# plt.hist(sales1, alpha=0.5)
# plt.hist(sales2, alpha=0.5)

# plt.show()


# data
# x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
# y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
# z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

plt.close('all')

#creating a 2d visualisation
fig = plt.figure()
constellation_2d = fig.add_subplot()
constellation_2d.scatter(x,y1, c='r')
plt.show()


#creating a 3d visualisation
fig_3d = plt.figure()

constellation3d = fig_3d.add_subplot(projection='3d')
constellation3d.scatter(x,y1,y2, c='green',marker='o')  
plt.show()




