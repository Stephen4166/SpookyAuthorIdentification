# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:22:34 2017

@author: lc416
"""
# This is a practice
# -------String------------------------------
name = "ask somebody"
#print (name.title ())
#print (name.upper ())
id = 10
information = name + " " + str (id)
#print (information)
name.rstrip ()
#print (name)
lang = " python "
#print (lang.strip ())

# --------List-----------------------------------
numbers = [1,2,5,3,6]
#print (numbers) 
#print (numbers [1])
#print (numbers [-1])

# modify elements
numbers [-1] = 0
#print (numbers)

# add an element
numbers.append (100)
#print (numbers)  
numbers.insert (-2, 999) # insert stores the value at the location, shifts every other value one position to the right
#print (numbers)

# remove elements
#print (numbers)
del numbers [0]
#print (numbers)
poped_number = numbers.pop () # pop out the last one
#print (poped_number)
#print (numbers)
poped_number = numbers.pop (-2) # pop out pointed one
#print (poped_number)
numbers.remove (5) # remove the specified value (This method only removes the first occurrence of the value)
#print (numbers)
a = 3
numbers.remove (a) # remove 是按照值来删除
#print (numbers)

# sort the list
cars = ['bmw', 'audi', 'hyundai', 'toyota']
cars.sort ()
#print (cars)
cars.sort (reverse = True)
#print (cars)
cars = ['bmw', 'audi', 'hyundai', 'toyota']
#print (sorted (cars)) # this is temporarily sorted
cars.reverse () # reverse the original order of a list
#print (cars)
cars = ['bmw', 'audi', 'hyundai', 'toyota']
#print (len (cars)) # the length of a list

# ---working with lists--------------------------------------------------------------------------
# loop through the entire list
#for car in cars:
#    print (car + "\n")
#    
#    print ("abcdef!!!")

# numerical list
#==============================================================================
# for value in range (1, 5): # from 1 to 4, not include 5
#     print (value)
#==============================================================================

# use range to make lists
#==============================================================================
# numbers = list (range (1, 6))
# print (numbers)
#==============================================================================

#==============================================================================
# even_numbers = list (range (2, 11, 2)) # start from two, end before 11, and add 2 each time
# print (even_numbers)
#==============================================================================

#==============================================================================
# squares = []
# for value in range (1, 11):
#     squares.append (value ** 2)
# print (squares)
#==============================================================================

# Simple statistics
#==============================================================================
# digits = list (range (1, 11))
# print (str(min (digits)) + " " + str(sum (digits)))
# 
#==============================================================================

# list comprehensions
#==============================================================================
# squares = [value ** 2 for value in range (1, 11)]
# print (squares)
#==============================================================================

# slicing a list 
cars = ['bmw', 'audi', 'hyundai', 'toyota']
#==============================================================================
# print (cars [0:3])
# print (cars [:4])
# print (cars [2:])
# print (cars [-2:])
#==============================================================================

# copy lists
#==============================================================================
# cats = cars # point to the same item which is not correct
# print (cats)
# print (cars)
# cars.pop ()
# print (cats)
#==============================================================================
#==============================================================================
# cats = cars [:]
# cars.pop ()
# print (cats)
#==============================================================================

# tuple -- immutable list, use parentheses instead of square brackets
dimensions = (200, 50)
# write over a tuple
dimensions = (400, 100)



# ---if statement--------------------------------------------------------------
#==============================================================================
# car = "Audi"
# if car == "audi":
#     print ("This works")
# else:
#     print ("This doesn't work")
#==============================================================================
#==============================================================================
# car = "Audi"
# if car.lower () == "audi":
#     print ("This works")
# else:
#     print ("This doesn't work")    
#==============================================================================
#==============================================================================
# if (car == "audi") or (car != "xxx"):
#     print ("This works")
#==============================================================================
#==============================================================================
# if "audi" in cars:
#     print ("There is a audi")
#==============================================================================
#==============================================================================
# if "audi" not in cars:
#     print ("XXXXXX")
#==============================================================================
#==============================================================================
# age = 25
# if age < 18:
#     print ("You still have time")
# elif age < 22:
#     print ("You need to hurry up")
# else:
#     print ("You deserve better, far better")
#==============================================================================
#==============================================================================
# age = 25
# if age < 18:
#     print ("You still have time")
# elif age < 22:
#     print ("You need to hurry up") # omiting the else statment, you cannot write else: and leave nothing following it 
#==============================================================================

# if statement with lists
#==============================================================================
# for car in cars:
#     if car == "audi":
#         print ("xxxxx")
#     else:
#         print ("yyyyy")
#==============================================================================

# checking that a list is not empty
#==============================================================================
# dogs = []
# if dogs:
#     print ("There are some dogs")
# else:
#     print ("There are no dogs")
#==============================================================================

# -----Dictionary--------------------------------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
#print (alien_0 ['color'])

# add a key-value pair
alien_0 ['x_position'] = 0
#print (alien_0)

# modify values in a dictionary
alien_1 = {}
alien_1 ['color'] = "green"
alien_1 ["hp"] = 200
alien_1 ["hp"] = 19

# remove a pair
#==============================================================================
# print (alien_1)
# del alien_1 ["hp"]
# print (alien_1)
#==============================================================================

# loop through all K-V pairs    (for k, v in exampleD.items())
user_0 = {
        'hp': 1,
        'mp': 12,
        'speed': 2,
        }
#==============================================================================
# for key, value in user_0.items ():
#     print (key + " " + str (value))  # they won't be printed in the order which they were stored
#==============================================================================
    

# loop through all keys
#==============================================================================
# for key in user_0.keys ():     # or for key in user_0
#     print (key.title())
#==============================================================================


# loop in order
#==============================================================================
# for key in sorted (user_0.keys ()):
#     print (key)
#==============================================================================


# loop through all values
#==============================================================================
# for value in user_0.values ():
#     print (value)
#==============================================================================
    
user_0 ['height'] = 12
#==============================================================================
# for value in set(user_0.values ()):   # use a set to avoid repetition
#     print (value)
#==============================================================================
    


# --------Nesting--------------------------------------------------------------
# lists in dict
#==============================================================================
# pizza = {
#         'crust': 'thick',
#         'topping': ['mushrooms', 'extra cheese'],
#         }
# print (pizza['topping'])
#==============================================================================

# dicts in dicts
users = {
        'small a': {
                'age': 12,
                'height': 23,
                },
        'big c': {
                'age': 14,
                'height': 54,
                },
        }
#==============================================================================
# for username, userinfo in users.items ():
#     print (username + " " + str(userinfo['age']) + ' ' + str(userinfo['height']))
#==============================================================================



# ================input--------------------------------------------------------
#==============================================================================
# message = input ("Tell me something: ")
# print (message)
#==============================================================================


#==============================================================================
# prompt = "If you tell us who you are, we can personalie the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print (name)
#==============================================================================


#height = input("How tall are you? ")
#height = int(height)
#==============================================================================
# if height > 2:
#     print("You are tall.")
#==============================================================================


# ------While Loop-------------------------------------------------------------
#==============================================================================
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#==============================================================================


#==============================================================================
# message = ''
# while message != 'quit':
#     message = input("If you want to quit, just type 'quit': ")
#     print(message)
#==============================================================================


#==============================================================================
# while True:
#     city = input("What's your favorite city? ")
#     
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")
#==============================================================================


#==============================================================================
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     
#     print(current_number)
#==============================================================================


# ---------------Functions-----------------------------------------------------
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

#greet_user("Ashley")


# default values
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("The name is: " + pet_name + ".")

#==============================================================================
# describe_pet("yoyo")  # positional arguments
# describe_pet(pet_name = 'yoyo')     # keyword arguments
#==============================================================================


