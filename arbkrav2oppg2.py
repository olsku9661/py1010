# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:31:20 2024

Program to calculate how many pizzas we need for a party
Request information of participants

Resources used: 
    https://www.geeksforgeeks.org/floor-ceil-function-python/

@author: ole.skurdal
olsku9661@usn.no
"""

#%% Import packages

import numpy as np

#%% Declaring the variables & values used in the program

elever_per_pizza = 4

#%% Calculate what is needed

print("Hei, til klassefesten regner vi med at hver elev spiser 1/4 pizza")
print("For finne ut hvor mange pizzaer vi skal kjøpe må du:\n")
antall_elever = int(input('Skrive inn antall elever som skal være med på festen: '))

pizza_deler = antall_elever / elever_per_pizza
pizza_hele = np.ceil(pizza_deler)

print(f'Det må handles inn {pizza_hele:.0f} pizzaer til festen, lykke til!')


