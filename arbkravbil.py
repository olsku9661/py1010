# -*- coding: utf-8 -*-
"""
Created on Wed Nov 06 22:25:09 2024

@author: ole.skurdal
This is the first arbeidskrav in PY1010-1 @ USN
Case is to compare the cost of owning an eletric car vs. an petrol fuled car

"""

#%%
#  Declaring the variables & values used in the program

KmY = 15000  # Km. per year 
FsEl = 5000  # Insurance per year El car
FsBen = 7500  # Insurance per year Gasoline car
TrInsFee = 8.38  # Traffic insurance fee per day el & gas
FuelEl = 0.2  # Power consumption 0.2 kWh/km El car 
ElPowPrice = 2.00  # Kr. 2.00 per kWh
FuelCon = 1.0  # Fuel consumption petrol per km
RoadTaxEl = 0.1  # Bomavgift kr. 0.1 per km El
RoadTaxBen = 0.3  # Bomavgift kr. 0.3 per km Bensin

#%%
#  Computing the intermediate results

InsFeeYear = TrInsFee*365  # Årlig trafikkforsikring
# print(format(InsFeeYear, '.2f'))
#print(f'Årlig trafikkforsikringsavgift for begge: {InsFeeYear:.2f}')

PetFuelCar = KmY*FuelCon  # Årlig drivstofforbruk bensin
ElFuelCar = KmY*FuelEl*ElPowPrice  # Årlig drivstofforbruk el
#print(PetFuelCar, ElFuelCar)

RTaxYBen = RoadTaxBen*KmY  # Årlig bomavgift bensinbilk
RTaxYEl = RoadTaxEl*KmY  # Årlig bomavgift elbil
#print(RTaxYBen, RTaxYEl)

#%% 
#  Present the final results with insurance

# Electric car:
FinalEl = InsFeeYear + ElFuelCar + RTaxYEl

# Petrol fuel car
FinalBen = InsFeeYear + PetFuelCar + RTaxYBen
#print(FinalBen, FinalEl)

print("Oversikt over årlige kostnader for elbil og bensinbil.")
print("Med årlig kjørelengde på 15.000 km.:\n")
print(f'Total årlig kostnad for elbil er kr: {FinalEl:.1f}')
print(f"Total årlig kostnad for besinbil er kr: {FinalBen:.1f}")
print("Kostnadsdifferanse per år [Bensin - Elbil] er kr:", FinalBen - FinalEl)

#Ans = str(input("\nØnsker du å oppgi dine egne antall kjørte kilometer? "))



#kuer = int(input(’Hvor mange kuer har du ?’))
