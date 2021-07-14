# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:22:47 2021

@author: Taofeek Oyedele
"""

my_age = 24
half_my_age = my_age / 2
greeting = "hello"
name = "Sam"
greeting_with_name = greeting + name
display(name)


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
# INTRODUCTION TO FUNCTIONS
# Why Functions?
# Let’s come back to the trip planning application we just discussed in the previous exercise. The steps we talked about for our program were:
# 
#  1. Establish an origin and destination
#  2. Calculate the distance/route
#  3. Return the best route 
# =============================================================================


def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

directions_to_timesSq()

def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

trip_welcome("Times Square")

def calculate_taxi_price(miles_to_travel, rate, discount=5):
  print(miles_to_travel * rate - discount )

calculate_taxi_price(100, 10 ) # position arguments
calculate_taxi_price(rate=10, discount=10, miles_to_travel=100) #keyword arguments
# discount = 5 in the function parameter = default argument
# the above functions are user defined functions but we have built-in functions
# such as the "print" function

#variable access in functions, any variable defined outside a function can be
#accessed both in and out of a function like the below

favorite_locations = "Paris, Norway, Iceland"
def print_count_locations():
    #favorite_locations = "Paris, Norway, Iceland"
    print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()


#using return
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 

def deduct_expense(budget, expense):
  a = budget - expense
  return  a
  

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)


print_remaining_budget(new_budget_after_shirt)


# =============================================================================
# CONTROL FLOW
# Boolean Expressions
# In order to build control flow into our program, we want to be able to check 
# if something is true or not. A boolean expression is a statement that can
#  either be True or False.

# Boolean expressions are statements that can be either True or False
# A boolean variable is a variable that is set to either True or False.
# We can create boolean expressions using relational operators:
# ==: Equals
# !=: Not equals
# >: Greater than
# >=: Greater than or equal to
# <: Less than
# <=: Less than or equal to
# if statements can be used to create control flow in your code.
# else statements can be used to execute code when the conditions of an if statement are not met.
# elif statements can be used to build additional checks into your if statements
# =============================================================================
# Write a space.py program that helps him keep track of his target weight by:
# 
# Checks which number planet is equal to.
# It should then compute his weight on the destination planet.
# =============================================================================

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 2

# Write an if statement below:

def which_planet(planet):
  if planet == 1 or planet == 2 or planet == 3 or planet == 4 or planet == 5 or planet == 6:
    place = ["Venus","Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    relative_gravity = [0.91, 0.38, 2.34, 1.06, 0.92, 1.19]
  return "on " + str(place[int(planet-1)]) + " your corresponding weight is " + str(weight*relative_gravity[int(planet-1)])

print(which_planet(planet))

# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
  if (num1 + num2 != 10):
     if not(num1 + num2 == 10):
         return True
  else : return False


  
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

# =============================================================================
# What is a List?
# In programming, it is common to want to work with collections of data. 
# In Python, a list is one of the many built-in data structures that allows us to
# work with a collection of data in sequential order.
#  e.g of a list, broken_heights = [65, 71, 59, 62]
# A list begins and ends with square brackets ([ and ]).
# Each item (i.e., 67 or 70) is separated by a comma (,)
# It’s considered good practice to insert a space () after each comma, 
# but your code will run just fine if you forget the space.
# 
# Lists can contain any data type in Python! For example, 
# this list contains a string, integer, boolean, and float.
# =============================================================================

sam_height_and_testscore = ["Sam", 67, 85.5, True]

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here and appending lists:
new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders 
orders_combined_another_Way = orders + ["lilac", "iris"] #can also use .append()

print(orders_combined)

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]

order_list.remove("Flatbread")
order_list.append("bread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
new_store_order_list.remove("Mango")
#new_store_order_list.remove("Onions") # should get an error cos onions isn't there
print(new_store_order_list)

#2D Lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]

heights.append(["Vik", 68])

print(heights)

# accessing and ammending 2D list
incoming_class = [["Kenny", "American", 9], 
  ["Tanya","Russian", 9], ["Madison", "Indian", 7]]

incoming_class[2][2] = 8
incoming_class[-3][-3] = "Ken" #using negative index
print(incoming_class)
print(len(incoming_class))



names = ["Jamie", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 65]

combined = zip(names, heights)

print(list(combined))

# using list methods

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]

front_display_list.insert(0, "Apple")
print(front_display_list)
front_display_list.pop(2) # .pop is used for removing in the list
print(front_display_list)
print(front_display_list.count("Mango"))
front_display_list.sort(reverse=True)
print(front_display_list)

# =============================================================================
# The sorted() function is different from the .sort() method in two ways:
# 
# It comes before a list, instead of after as all built-in functions do.
# It generates a new list rather than modifying the one that already exists.
# =============================================================================

print(str(sorted(front_display_list)) + " this is via sorted built in function" )
front_display_list.sort()
print(str(front_display_list) +" via sort method")


# going through a list, adding the last two digits and appending it to the list 
# repeat 2 more times
# this was also done via for and while loop after learning about loops
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

print(append_sum([1, 1, 2]))

def append_sum(lst):
    for a in range(3):
        a = lst[-1] + lst[-2]
        lst = lst + [a]   
    return lst
    
print(append_sum([1, 1, 2]))

def append_sum(lst):
    count = 0
    while count <= 2:
        a = lst[-1] + lst[-2]
        lst = lst + [a]
        count +=1
    return lst
    
print(append_sum([1, 1, 2]))    


def double_index(lst, index):
  if index >= 0 :
    double = 2 * lst[index-1]
    lst[index-1] = double
    print(double)
    return lst
  else : return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

def middle_element(lst):
  if len(lst) % 2 == 0 :
    locate = len(lst) / 2
    a = int(locate)
    print(type(a))
    print(type(locate))
    print(lst[a]+lst[a-1])
    avg = (lst[a]+lst[a-1]) * 0.5
    return avg
  else : return lst[int(len(lst) / 2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5, 2]))


# =============================================================================
# loops introduction including for, while, infinite and nested
# for <temporary variable> in <collection>:
#  <action>
# while <conditional statement>:
#  <action>
# =============================================================================

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for i in ingredients:
    print(i)


big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
    
for i in big_number_list:
    if i > 0:
        print(i)
    else : continue


project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for team in project_teams:
  for name in team:
      print(name)

        
# =============================================================================
# List Comprehensions
# Let’s break down our example in a more general way:
# 
# new_list = [<expression> for <element> in <collection>]
# In our doubled example, our list comprehension:
# 
# Takes an element in the list numbers
# Assigns that element to a variable called num (our <element>)
# Applies the <expression> on the element stored in num and adds the result to a
# new list called doubled
# Repeats steps 1-3 for every other element in the numbers list (our <collection>)
# =============================================================================


numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [score + 10 for score in grades ]
print(scaled_grades)

scaled = []

for n in grades:
  n += 10
  scaled.append(n)

print(scaled)


numbers = [2, -1, 79, 33, -45]

only_negative_doubled = []

for n in numbers:
    if n < 0:
        only_negative_doubled.append(n *2)
    else : continue
print(only_negative_doubled)

# another method will be 

negative_doubled = [num * 2 for num in numbers if num < 0 ]
print(negative_doubled)

if_else_method = [num * 2 if num < 0 else num *3 for num in numbers]
print(if_else_method)

# creating a len() function

name = "Timothy"
def get_length(name):
  for n in range(len(name)):
    n +=1
  return n

print(get_length(name))

# using while loop

char = "Timo"
def length(char):
  get = 0
  while get < len(char):
    get += 1
  return get
print(length(char))

a = "alpjaba"

a.find("a")
b = a.replace("a","b")
print(b)


# =============================================================================
# 
# Introduction to Dictionary
# A dictionary is an unordered set of key: value pairs.
# 
# It provides us with a way to map pieces of data to each other so that we can 
# quickly find values that are associated with one another.
# 
# Suppose we want to store the prices of various items sold at a cafe:
# 
# Avocado Toast is 6 dollars
# Carrot Juice is 5 dollars
# Blueberry Muffin is 2 dollars
# In Python, we can create a dictionary called menu to store this data:
# 
# menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Notice that:
# 
# A dictionary begins and ends with curly braces { and }.
# Each item consists of a key ("avocado toast") and a value (6).
# Each key: value pair is separated by a comma.
# It’s considered good practice to insert a space () after each comma, but our 
# code will still run without the space.
# 
# However, the keys can be numbers as well but can't be a list
# 
# Values can be of any type. We can use a string, a number, a list, or 
# even another dictionary as the value associated with a key!
# 
# We can also mix and match key and value types. For example:
# 
# person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
# =============================================================================

children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] ,
            "Corleone": ["Sonny", "Fredo", "Michael"] }

print(children)

my_empty_dictionary = {} # can also have an empth dictionary

# adding things to the dictionary

my_empty_dictionary = {1:"hello", 2:"to the dictionary", 
                       3:"This is a dictionary", 
                       4:["Now", "it's", "no more", "empty"],
                       5: "the number of empty dictionary is", 6: "the val is 2"}

print(my_empty_dictionary)

#adding more stuff

my_empty_dictionary.update({7:"just adding things", "a": "nothing more to add"})
print(my_empty_dictionary)

# creating a dictionary from 2 lists

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]


drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}

print("this is a dictionary: " + str(drinks_to_caffeine))


print(my_empty_dictionary[6]) # getting a value or
print(my_empty_dictionary.get(6, "no value")) #returns "no value if key != exist

# key error handling methods

# 1 using the if method

key_check = "tea"

if key_check in drinks_to_caffeine:
    print(drinks_to_caffeine[key_check])
    
# 2 using the try except error handling
try:
    print(drinks_to_caffeine[key_check])
except KeyError:
    print("this key doesn't exist")
    
# to see all the keysm, there are two methods

print(list(drinks_to_caffeine))

for key in drinks_to_caffeine.keys():
    print(key)

# getting values 
print(my_empty_dictionary.values())

#getting both the key and value via .items() method

for key, value in drinks_to_caffeine.items():
    print("The amount of caffeine in {drink} is {caffeine}"
          .format(drink = key, caffeine = value))

A class is a template for a data type. It describes the kinds of information 
that class will hold and how a programmer will interact with that data. 
Define a class using the class keyword. 

for example
class CoolClass:
  pass
# =============================================================================
# In the above example we created a class and named it CoolClass. 
# We used the pass keyword in Python to indicate that the body of the class 
# was intentionally left blank so we don’t cause an IndentationError.
# 
# A class doesn’t accomplish anything simply by being defined. 
# A class must be instantiated. In other words, we must create an instance 
# of the class, in order to breathe life into the schematic.
# 
# Instantiating a class looks a lot like calling a function. 
# We would be able to create an instance of our defined CoolClass as follows:
# 
# cool_instance = CoolClass()
# Above, we created an object by adding parentheses to the name of the class. 
# We then assigned that new instance to the variable cool_instance for 
# safe-keeping so we can access our instance of CoolClass at a later time.
# 
# Instantiation takes a class and turns it into an object
# =============================================================================

class Facade:
  test = "this is class tutorial"
  number = 1
  
  # in a class, a method is known as function with self passed in as 
  # one of the arguments if there're multiple arguments
  # if multipl arguments are passed in, they have to be defined later 
  def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."

facade_1 = Facade() #instantiating the class, facade_1 is now an object

sub = facade_1.test
num = facade_1.number

print(sub + " number " +str(num))
  

rule = Facade()
print(rule.washing_brushes())


# =============================================================================
# working with files
# =============================================================================

with open("script.py") as new_file:
    file = new_file.read()
    
print(file)

# writing to a file

with open('new.py', 'w') as new_name: # this will erase contents of existing files
    new_name.write("This is a new file") 

with open('new.py', 'r') as read_content: # 'r' is the default for reading files
    content = read_content.read()    
print(content)

with open("new.py", 'a') as new_file: #append mode
    new_file.write("wohooo, we're doing something")
    file = new_file.read()
print(file)


# a method to write to a file as well as read it
# DictReader method can alos be used to read the csv as well
import csv


access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'},
              {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'},
              {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'},
              {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'},
              {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'},
              {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'},
              {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'},
              {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'},
              {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'},
              {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

with open('logger.csv', 'w') as logger_csv:
  #fields = []
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()

  for log in access_log:
    log_writer.writerow(log)

with open('logger.csv') as logger:
  read_log = logger.read()

print(read_log)


# example on how to work with json files
import json

with open('message.json') as message_json:
  message = json.load(message_json)

print(message['text'])

# message = {'text': "Now that's JSON!", 'secret text': "Now that's some _serious_ JSON!"}


# saving python data as a json file example

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
  json.dump(data_payload,data_json)

with open('data.json') as data:
  data_11 = data.read()

print(data_11)



