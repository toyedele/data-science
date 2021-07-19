"""
Created on Tue Jul 6 17:24:13 2021

@author: Taofeek Oyedele

Data set: US medical health insurance cost

Source: Codecademy

Aim of the project: To improve my analytical and visual skills

Hypothesis: 
    Expect that some variables will have a greater impact on the price of insurance
    Smoking, age and bmi should all have a greater effect on the insurance cost
    Insurance cost should increase as one ages
    Insurance cost should also be highest when an individual is obese
    
Conclusion:
    Smoking, age and bmi values have a greater effect on insurance cost compare
    to other variables - with smoking having the highest impact as expected
    The average insurance cost increased as one age with male paying higher than female
    The highest average insurance cost was displayed in the obese group. However,
    it's worth nothing the discrepancy when comparing female and male in the underweight category
    
Room for improvement:
    Look at the average insurance cost grouped by age, bmi and sex
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import iqr

#change the below line to your local address where the insurance file is stored
insurance = pd.read_csv(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\python-portfolio-project-starter-files\insurance.csv')


def scoping_the_data():
    print(insurance.head())
    print(insurance.info())
    print(insurance.describe())
    print(insurance.count().duplicated() )
    print(insurance.count().isnull())
    print(insurance.columns)
    print(" \n The inter-quartile range is " + str(iqr(insurance.charges)))
    
    plt.hist(insurance.charges, edgecolor="black")
    plt.title("Brief overview of the data")
    plt.show() 
    plt.boxplot(insurance.charges, labels= ["insurance charges"])
    plt.show()
       
scoping_the_data()    

insurance_modified = insurance.drop_duplicates()
insurance_modified = insurance_modified.sort_values(
    by=["age","sex","bmi","children","smoker","region"],
    ascending=True).reset_index(drop=True)
print("\n")
print(insurance_modified.tail(60))


# caetgorising gender, smoker and region to numbers in order to perform a correlation
insurance_modified['sex_numbered'] = pd.Categorical(insurance_modified.sex,
                                                  ['male', 'female'], ordered=True)
insurance_modified['sex_numbered'] = insurance_modified['sex_numbered'].cat.codes
insurance_modified['smoker_numbered'] = pd.Categorical(insurance_modified.smoker,
                                                  ['yes', 'no'], ordered=True)
insurance_modified['smoker_numbered'] = insurance_modified['smoker_numbered'].cat.codes
insurance_modified['region_numbered'] = pd.Categorical(insurance_modified.region,
                                                  ['northeast', 'southeast',
                                                   'northwest','southwest'], ordered=True)
insurance_modified['region_numbered'] = insurance_modified['region_numbered'].cat.codes   

# rearranging the columns
column_names = [insurance_modified.columns[6]]

for n in range(len(insurance_modified.columns)):
    name = insurance_modified.columns[n]
    if name not in column_names:    
        column_names.append(name)

insurance_modified = insurance_modified.reindex(columns=column_names)
correlation = abs(insurance_modified.corr())
sns.heatmap(correlation, cmap="GnBu")
plt.show()
print("\n")
print(correlation)


age_group = []
for n in insurance_modified.age:
    if n <= 20:
        age_group.append('20')
    elif n > 20 and n <= 30:
        age_group.append('21 - 30')
    elif n > 30 and n <= 40:
        age_group.append('31 - 40')
    elif n > 40 and n <= 50:
        age_group.append('41 - 50')
    else : age_group.append('50+')


bmi_group = []
for n in insurance_modified.bmi:
    if n < 18.5:
        bmi_group.append('1 - underweight')
    elif n >= 18.5 and n < 25:
        bmi_group.append('2 - healthy')
    elif n >= 25 and n < 30:
        bmi_group.append('3 - overweight')  
    else: bmi_group.append('4 - obese')

insurance_modified['age_group'] = age_group

charges_grouped_by_sex_and_age_group = insurance_modified.charges.groupby(by=[
    insurance_modified.sex,insurance_modified.age_group]).mean()

insurance_modified['bmi_group'] = bmi_group

charges_grouped_by_sex_and_bmi_group = insurance_modified.charges.groupby(by=[
    insurance_modified.sex,insurance_modified.bmi_group]).mean()


def charges_compared_to_smoking_and_region():
    # comparing smoking to charges
    sns.boxplot(data =insurance_modified, x='smoker' , y='charges')
    plt.title('Smoking vs Charges')
    plt.show()
    
    
    # comparing the region to charges
    sns.boxplot(data =insurance_modified, x='region' , y='charges')
    plt.title('Region vs Charges')
    plt.show()
    
charges_compared_to_smoking_and_region()

def chart_by_age_and_sex():
    female = list(charges_grouped_by_sex_and_age_group[:5])
    male = list(charges_grouped_by_sex_and_age_group[5:])
    
    female_error = [x*0.1 for x in female]
    male_error = [x*0.1 for x in male]
    
    n = 1  # This is our first dataset (out of 2)
    t = 2 # Number of datasets
    d = len(female) # Number of sets of bars
    w = 0.8 # Width of each bar
    store1_x = [t*element + w*n for element in range(d)]
    
    
    n = 2  # This is our first dataset (out of 2)
    t = 2 # Number of datasets
    d = len(male) # Number of sets of bars
    w = 0.8 # Width of each bar
    store2_x = [t*element + w*n for element in range(d)]
    
    ax = plt.subplot()
    plt.bar(store1_x, female, yerr=female_error, capsize=5, color="orange")
    plt.bar(store2_x, male, yerr=male_error, capsize=5, color="blue")
    middle_x = [ (a + b) / 2.0 for a, b in zip(store1_x, store2_x)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(['20', '21-30', '31-40', '41-50', '50+'])
    
    plt.legend(["female", "male"])
    plt.xlabel("age group")
    plt.ylabel("average insurance cost")
    plt.title("The average cost of insurance grouped by age and sex")
    plt.show()

chart_by_age_and_sex()

       
def chart_by_bmi_and_sex():
    female = list(charges_grouped_by_sex_and_bmi_group[:4])
    male = list(charges_grouped_by_sex_and_bmi_group[4:])
    
    female_error = [x*0.1 for x in female]
    male_error = [x*0.1 for x in male]
    
    n = 1  # This is our first dataset (out of 2)
    t = 2 # Number of datasets
    d = len(female) # Number of sets of bars
    w = 0.8 # Width of each bar
    store1_x = [t*element + w*n for element in range(d)]
    
    
    n = 2  # This is our first dataset (out of 2)
    t = 2 # Number of datasets
    d = len(male) # Number of sets of bars
    w = 0.8 # Width of each bar
    store2_x = [t*element + w*n for element in range(d)]
    
    ax = plt.subplot()
    plt.bar(store1_x, female, yerr=female_error, capsize=5, color="orange")
    plt.bar(store2_x, male, yerr=male_error, capsize=5, color="blue")
    middle_x = [ (a + b) / 2.0 for a, b in zip(store1_x, store2_x)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(['underweight', 'healthy', 'overweight', 'obese'])
    
    plt.legend(["female", "male"])
    plt.xlabel("bmi group")
    plt.ylabel("average insurance cost")
    plt.title("The average cost of insurance grouped by bmi and sex")
    plt.show()

chart_by_bmi_and_sex()
