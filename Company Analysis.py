# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 09:02:05 2021

@author: Taofeek Oyedele

Data source: Codecademy

Aim: to improve a company's operations after a global pandemic by answering the below questions:
    - Is the company in good financial health?
    - Does the company need to let go of any employees?
    - Should the company allow employees to work from home permanently?

Conclusion:
    
"""

from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# load in financial data
financial_data = pd.read_excel(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\company.xlsx', sheet_name='financial_data')

# code goes here
print(financial_data.head(10))
# print(financial_data.shape)

month = financial_data.Month.values
revenue = financial_data.Revenue.values
expenses = financial_data.Expenses.values

plt.subplot(1,1,1)
# plt.figure(figsize=(10,10))
plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

plt.subplot(2,1,1)
plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.tight_layout()
plt.show()


#looking at the expenses
expense_overview = pd.read_excel(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\company.xlsx', sheet_name='Expenses')
print(expense_overview)

expense_categories = expense_overview.Expense.values
proportions = expense_overview.Proportion

plt.clf()
plt.pie(proportions, labels=expense_categories)
plt.title('Expenses')
plt.axis('equal')
plt.tight_layout()
plt.show()

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()

#looking at the employees
employees = pd.read_excel(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\company.xlsx', sheet_name='Employees')
print(employees.head)


sorted_productivity = employees.sort_values(by='Productivity').reset_index(drop=True)
employees_cut = sorted_productivity.iloc[:100]
print(employees_cut.Name)

#exploring the relationship between Income and Productivity
#due to the different scales, the data needs to be standardised
data = employees[['Salary','Productivity']].iloc[100:]

scaler = preprocessing.StandardScaler()
standardised_data = scaler.fit_transform(data)
print(standardised_data)
plt.clf()
plt.hist(standardised_data, density=True)
plt.show()

# investigating commute times
commute_times  = employees['Commute Time']
# print(commute_times.describe())

plt.clf()
plt.hist(commute_times)
plt.title("Employee Commute Times")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()

# transforming the data
commute_times_log = np.log(commute_times)
plt.clf()
plt.hist(commute_times_log)
plt.title("Employee Commute Times")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()

