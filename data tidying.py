# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:15:16 2021

@author: Taofeek Oyedele
"""

import pandas as pd
# import glob

students = pd.read_excel(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\restaurants.xlsx', sheet_name='students')

# transforming the data by converting the fractions and probabilty scores to one col

print(students.head(10))

students = pd.melt(frame=students, id_vars=["full_name","gender_age","grade"],
                   value_vars=["Fractions","Probability"],value_name="score",
                   var_name="exam")


print(students.head())

print(students.exam.value_counts())

students = students.dropna()

students = students.drop_duplicates(subset=['full_name']).reset_index()
print(students.exam.value_counts())

students['gender'] = students.gender_age.str[0]
students['age'] = students.gender_age.str[1:]
students.score = pd.to_numeric(students.score)
students.score = students.score*100
print(students.head(10))

students['raw_grade'] = students.grade.str.split('(\d+)', expand=True)[1]

students.raw_grade = pd.to_numeric(students.raw_grade)

avg_grade = students.raw_grade.mean()
print("The average year grade is " + str(int(avg_grade)))





