# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:27:31 2021

@author: Taofeek Oyedele
"""

# =============================================================================
# Python Syntax: Medical Insurance Project
# Suppose you are a medical professional curious
# about how certain factors contribute to medical insurance costs. 
# Using a formula that estimates a person’s yearly insurance costs, 
# you will investigate how different factors such as age, sex, BMI, etc. affect the prediction.
# =============================================================================

# create the initial variables below
age = 28
sex = 0 # 0 for female, 1 for male*
bmi = 26.2
num_of_children = 3
smoker = 0 # 0 for a non-smoker, 1 for a smoker

# Add insurance estimate formula below
insurance_cost = 250 * age - 128  * sex + 370 * bmi + 425 * num_of_children + 2400 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age +=4

new_insurance_cost = 250 * age - 128  * sex + 370 * bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) +" dollars.")

# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250 * age - 128  * sex + 370 * bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing the BMI by 3.1 is " + str(change_in_insurance_cost) +" dollars.")

# Male vs. Female Factor

bmi = 26.2
sex = 1

new_insurance_cost = 250 * age - 128  * sex + 370 * bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for being male instead of female is " + str(change_in_insurance_cost) +" dollars.")
# Extra Practice

#experiment of a smoker vs non- non-smoker
smoker = 0
if smoker == 0:
  new_insurance_cost = 250 * age - 128  * sex + 370 * bmi + 425 * num_of_children + 2400 * smoker - 12500
  change_in_insurance_cost = new_insurance_cost - insurance_cost
  print("The change in estimated insurance cost for being a non-smoker is " + str(change_in_insurance_cost) +" dollars.")
elif smoker == 1:
  new_insurance_cost = 250 * age - 128  * sex + 370 * bmi + 425 * num_of_children + 2400 * smoker - 12500
  change_in_insurance_cost = new_insurance_cost - insurance_cost
  print("The change in estimated insurance cost for being a smoker is " + str(change_in_insurance_cost) +" dollars.")


#what happens when the number of children changes
num_of_children = 1
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost due to kids cost is " + str(change_in_insurance_cost) +" dollars.")


# =============================================================================
# # using functions to make things easier and conditional functions
# # Create calculate_insurance_cost() function below: 
# =============================================================================
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for "+ name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost


# Initial variables for Maria 
#age = 28
#sex = 0 
#bmi = 26.2
#num_of_children = 3
#smoker = 0  

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("maria",28,0,26.2,3,0)
omar_insurance_cost = calculate_insurance_cost("omar",35,1,22.2,0,1)

# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    return "To lower your cost, you should consider quitting smoking."
  else : return "Smoking is not an issue for you."

def analyze_bmi(bmi_value):
  if bmi_value > 30 :
    return "Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI."
  elif 25 <= bmi_value <= 30  :
    return "Your BMI is in the overweight range. To lower your cost, you should lower your BMI."
  elif 18.5 <= bmi_value < 25  :
    return "Your BMI is in a healthy range."
  else : return "Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health."
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  print(analyze_smoker(smoker))
  print(analyze_bmi(bmi))
  return estimated_cost
 #analyze_smoker(smoker)
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)



mine = estimate_insurance_cost("moi",28,0,20.2,2,0)

# adding list to the project

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here

names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0,5320.0,35210.0]
insurance_data = zip(names, insurance_costs)
print("Here is the actual insurance cost data: " + str(list(insurance_data)))

estimated_insurance_data = []

estimated_insurance_data.append(["Maria", maria_insurance_cost])
estimated_insurance_data.append(["Rohan", rohan_insurance_cost])
estimated_insurance_data.append(["Valentina", valentina_insurance_cost])
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

insurance_cost_difference = []
insurance_cost_difference.append(["Maria", maria_insurance_cost - insurance_costs[0]])
insurance_cost_difference.append(["Rohan", rohan_insurance_cost - insurance_costs[1]])
insurance_cost_difference.append(["Valentina", valentina_insurance_cost-insurance_costs[2]])

print("The difference for each individual is: " + str(insurance_cost_difference))


# list challenge continuation

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = zip(insurance_costs, names)
record = list(medical_records)
print(record)

num_medical_records = len(list(names))

print("There are " + str(num_medical_records) + " medical records.")

first_medical_record = record[0]

print("Here is the first medical record: " + str(first_medical_record))

sorte = sorted(record)

cheapest_three = sorte[:3]

print("Here are the three cheapest insurance costs in our medical records:" + str(cheapest_three))

priciest_three = sorte[-3:]
print("Here are the three most expensive insurance costs in our medical records: "+ str(priciest_three))

occurrences_paul = names.count("Paul")

print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records. ")

#sort it out via names, then pick the records for index 3 and 7
alpha_record = list(zip(names, insurance_costs))
alpha_record.sort()

print("The records for index 3 to 7 are: " + str(alpha_record[3:8]))

# adding loops

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0

for cost in actual_insurance_costs:
  total_cost += cost
print(total_cost)


average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) )


for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs [i]
  #print("The insurance cost for "+ name + " is " + str(insurance_cost) +" dollars.")
  if insurance_cost > actual_insurance_costs[i] :
    print("The insurance cost for "+name +" is above average.")
  elif insurance_cost < actual_insurance_costs[i]:
     print("The insurance cost for "+name +" is below average.") 
  else : print("The insurance cost for "+ name + " is equal to the average.")

updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

print(updated_estimated_costs)


# practising with strings
medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
#print(medical_data)

updated_medical_data = medical_data.replace("#","$")
#print(updated_medical_data)

num_records = 0
for n in updated_medical_data:
   if n == "$":
    num_records +=1
#print("There are {num_records} medical records in the data.".format(num_records=num_records))

#Splitting Strings

medical_data_split = updated_medical_data.split(";")

#print(medical_data_split)

medical_records = []
for n in medical_data_split:
  medical_records.append(n.split(","))

#rint(medical_records)

#cleaning the ddata
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

#print(medical_records_clean)

#analyse

for name in medical_records_clean:
  print(name[0].upper())

names = []
ages = []
bmis = []
insurance_costs = []

for info in medical_records_clean:
  names.append(info[0])
  ages.append(info[1])
  bmis.append(info[2])
  insurance_costs.append(info[3])

print(names)

total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
average_bmi = total_bmi / len(bmis)
print("Average BMI: {average_bmi}".format(average_bmi= str(average_bmi)))  

#extra, calculating the avg insurance cost but the $ needs to be removed first
insurance = 0

for i in insurance_costs:
  ins = []
  ins.append(i[1:])
  #print(ins)
  for a in ins:
    #ins.append(i[1:])
    insurance += float(a) 
#print(insurance)
avg_cost = insurance / len(insurance_costs)

print("avg insurance cost is : $" + str(avg_cost))


#using dictionaries

medical_costs = {}

medical_costs["Marina"] = 6607.0
medical_costs.update({"Vinay":3225.0, "Connie":8886.0, "Isaac":16444.0,"Valentina":6420.0})

medical_costs.update({"Vinay": 3325.0})

total_cost = 0

for value in medical_costs.values():
  total_cost += value

#print("Average Insurance Cost: {average_cost}".format(average_cost = total_cost/len(medical_costs)))

#print(medical_costs)


names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27,24,43,35,52]

names_to_ages = {key:value for key, value in zip(names, ages)}

#print(names_to_ages)

marina_age = names_to_ages.get("Marina", "None")

#print("Marina's age is {marina_age}".format(marina_age = marina_age))

medical_records = {}

medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records)

connie = medical_records.get("Connie").get("Insurance_cost")
print("Connie's insurance cost is {X} dollars.".format(X=connie))

medical_records.pop("Vinay","doesn't exist")

for key, item in medical_records.items():
  print("{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}".format(Name=key,Age=item["Age"],Sex = item["Sex"], Smoker=item["Smoker"],BMI=item["BMI"],Insurance_cost=item["Insurance_cost"]))

# updating the record

def update_medical_records(name,age,sex,bmi,children,smoker,insurance_cost):
  values = {}
  values.update({"Age":age,"Sex":sex,"BMI":bmi,"Children":children,"Smoker":smoker,"Insurance_cost":insurance_cost})
  medical_records[name] = values
  print(medical_records)

name = "Thomas"
age = 27
sex = "Male"
bmi = 22.0      
children = 5
smoker = "Smoker"
insurance_cost = 2600.0

update_medical_records(name,age,sex,bmi,children,smoker,insurance_cost)





