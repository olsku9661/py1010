# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:31:20 2024

Program to calculate radians from degrees

Resources used: 

@author: ole.skurdal
olsku9661@usn.no
"""

#%% Import packages

import numpy as np

#%% Declaring the variables & values used in the program

# Formelen er: Radianer = Grader * (π/180)

#%% Get input and calculate what is needed

print("Vi regner om fra grader til radianer")
v_grad = float(input('Skriv inn gradtallet: ' ))

v_rad = v_grad*(np.pi/180)

# print(v_rad)

print(f'{v_grad} grader tilsvarer {v_rad:.2f} radianer')

