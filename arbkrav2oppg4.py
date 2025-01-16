# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:30:29 2025
Velger å levere alle underoppgavene til oppgave 4 i en fil

4.a
Create a dictionary with different countries as keys

4.b
Ask the user to input a country and give output about the capitol and inhabitants
That is the values the dictionary holds for this key

4.c
Append another country to the dictionary with capitol and inhabitants

Resources used:
    https://www.w3schools.com/python/python_dictionaries.asp

@author: ole.skurdal
olsku9661@usn.no
"""

#%% Import packages

# import numpy as np

#%% Declaring the variables & values used in the program

# Litt om noen metoder som brukes på dictionaries (data er her vår dictionary)
# data.keys()  # Kun "nøklene"
# data.items()  # Har får vi alt
# data.values()  # Her det bare verdiene til nøklene vi får
# len(data)  # Lengden av dictionaryen

#%% Create the dictionary
# Oppgave 4.a

data = {}  # Oppretter en tom dictionary
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

# print("Her alle data vi har i vår dictionary:", data)


#%% Request input
# Oppgave 4.b

Land = input('\nSkriv inn navnet på et land du vil vite mer om: ' )

if Land in data.keys():
    print("\nVi vet følgende om", Land)
    By = data[Land][0]
    Innbyggere = data[Land][1]
    print(By, "er hovedstaden i", Land, "og det er", Innbyggere, "mill. innbyggere i", By)
else:
    print("Beklager, fant ikke", Land, "i listen vår")
    

#%% Expand the dictionary
# Oppgave 4.c

print("\nVi har lite data i vår dictionary og ønsker at du utvider den med et nytt land\n")

nyttLand = input('Skriv inn navnet på et land vi ikke har: ' )

if nyttLand not in data:
    print("Om du er fornøyd med å legge inn", nyttLand, "så trenger vi navnet på hovedstad og innbyggere")
    nyBy = input("Hva er navnet på hovedstaden: " )
    nyInnbygger = input("Hvor mange innbyggere er det i hovedstaden: " )
    data[nyttLand] = [nyBy, nyInnbygger]
    # print(nyBy, nyInnbygger)
else:
    print("Vi har allerede", nyttLand, "i listen vår!")

print("\nVår dictionary inneholder nå følgende data:\n", data)

print("\nHer er en litt penere oversikt :-)")
for land in data:
     print("I", land, "er hovedstaden", data[land][0], "og den har", data[land][1], "mill. innbyggere")
    
# The End
