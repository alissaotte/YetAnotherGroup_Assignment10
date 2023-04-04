##################################################################################################################
# Names: Brant Kightlinger, Alissa Otte, Erik Sibri
# Emails: kightlbc@mail.uc.edu, otteal@mail.uc.edu, sibriee@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010 002
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that we are able to collaborate as a group to request and receive
#   (cont.) data from an API, create a dictionary with the API's data, and call and format data we select
#   (cont.) This module shows how we call the API and call the function to create a dictionary with key/pair values
# Citations: N/A
# Anything else that's relevant: N/A
##################################################################################################################

# main.py

import json
import requests
from iterateDictionaryPackage.iterateDictionary import *

# Requesting website and specifically information about cheddar cheese
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=Kfrk8cf6cgEAzUwuLY6YdA6eE2H4SdFggDW3607K&query=Cheddar%20Cheese')
json_string = response.content

parsed_json = json.loads(json_string) # Now we have a Python dictionary

# Running function to create dictionary with key/value pairs
iterate_dictionary(parsed_json)
# print(parsed_json) # Test step, printing out entire dictionary


# Weis Markets, Inc. (Alissa)
print(" ")
print("General information About Cheese 1: ")
print("Brand Name: " + (parsed_json['foods'][1]['brandName']))
print("Ingredients: " + (parsed_json['foods'][1]['ingredients']))
# 1st cheese brand nutritional information
print("Nutritional information About Cheese 1: ")
# Protein information
print((parsed_json['foods'][1]['foodNutrients'][0]['nutrientName']) + ": " + (parsed_json['foods'][1]['foodNutrients'][0]['nutrientNumber']) + " " + (parsed_json['foods'][1]['foodNutrients'][0]['unitName']))
# Carbs information
print((parsed_json['foods'][1]['foodNutrients'][2]['nutrientName']) + ": " + (parsed_json['foods'][1]['foodNutrients'][2]['nutrientNumber']) + " " + (parsed_json['foods'][1]['foodNutrients'][2]['unitName']))


# Tillamook County Creamery Association (Erick)
print(" ")
print("General information About Cheese 30: ")
print("Brand Name: " + (parsed_json['foods'][30]['brandName']))
print("Ingredients: " + (parsed_json['foods'][30]['ingredients']))
# 30th cheese brand nutritional information
print("Nutritional information About Cheese 30: ")
# Protein information
print((parsed_json['foods'][30]['foodNutrients'][0]['nutrientName']) + ": " + (parsed_json['foods'][30]['foodNutrients'][0]['nutrientNumber']) + " " + (parsed_json['foods'][30]['foodNutrients'][0]['unitName']))
# Carbs information
print((parsed_json['foods'][30]['foodNutrients'][2]['nutrientName']) + ": " + (parsed_json['foods'][30]['foodNutrients'][2]['nutrientNumber']) + " " + (parsed_json['foods'][30]['foodNutrients'][2]['unitName']))

# Tillamook County Creamery Association (Erick)
print(" ")
print("General information About Cheese 25: ")
print("Brand Name: " + (parsed_json['foods'][25]['brandName']))
print("Ingredients: " + (parsed_json['foods'][25]['ingredients']))
# 25th cheese brand nutritional information
print("Nutritional information About Cheese 25: ")
# Protein information
print((parsed_json['foods'][25]['foodNutrients'][0]['nutrientName']) + ": " + (parsed_json['foods'][25]['foodNutrients'][0]['nutrientNumber']) + " " + (parsed_json['foods'][25]['foodNutrients'][0]['unitName']))
# Carbs information
print((parsed_json['foods'][25]['foodNutrients'][2]['nutrientName']) + ": " + (parsed_json['foods'][25]['foodNutrients'][2]['nutrientNumber']) + " " + (parsed_json['foods'][25]['foodNutrients'][2]['unitName']))
