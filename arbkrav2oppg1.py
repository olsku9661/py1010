# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:00:52 2024

Program to calculate the age of a person
Request information of birthyear

Resourses used:
    https://www.w3schools.com/python/python_datetime.asp
    https://www.datacamp.com/tutorial/python-datetime?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=157156376311&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=s&utm_adpostion=&utm_creative=720362650453&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9218816&utm_content=&utm_campaign=230119_1-sea%7Edsa%7Etofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-bfcm24&gad_source=5&gclid=EAIaIQobChMI1PuUhciRigMV2VCRBR3bAxwdEAAYASAAEgIcHPD_BwE&dc_referrer=https%3A%2F%2Fsyndicatedsearch.goog%2F
  
@author: ole.skurdal
olsku9661@usn.no
"""

#%% Import packages

import datetime

#%% Declaring the variables & values used in the program

local_time = datetime.datetime.now()
#print(local_time)
this_year = local_time.year
#print(this_year)

#%% Input section

print("Vil du vite hvor gammel du er, må jeg spørre:")
birth_year = int(input('Hvilket år er du født [YYYY]? '))
your_age = this_year - birth_year


#%% Output 

print("I år som er", this_year, "vil du være", your_age, "år gammel :-)")

# Siden vi er i 2025...
print("I fjor som var", this_year - 1, "var du", your_age - 1, "år gammel :-)")

# The End
