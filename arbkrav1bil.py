# -*- coding: utf-8 -*-
"""
Created on Tue Nov 05 19:25:00 2024

@author: ole.skurdal
This is the first work requirement in PY1010-1 @ USN
Case is to compare the cost of owning an eletric car vs. an petrol fuled car

"""

#%%
#  Declaring the variables & values used in the program

KmY = 15000  # Using 15000 km. per year 
FsEl = 5000  # Insurance per year El car
FsBen = 7500  # Insurance per year petrol car
TrInsFee = 8.38  # Traffic insurance fee per day el & gas
FuelEl = 0.2  # Power consumption 0.2 kWh/km El car 
ElPrice = 2.00  # El price Kr. 2.00 per kWh
FuelCon = 1.0  # Fuel consumption petrol per km
RoadTaxEl = 0.1  # Road tax kr. 0.1 per km El
RoadTaxBen = 0.3  # Road tax kr. 0.3 per km Petrol

#%%
#  Computing the intermediate results

InsFeeYear = TrInsFee*365  # Årlig trafikkforsikringsavgift

PetFuelCar = KmY*FuelCon  # Årlig drivstofforbruk bensin
ElFuelCar = KmY*FuelEl*ElPrice  # Årlig drivstofforbruk el

RTaxYBen = RoadTaxBen*KmY  # Årlig bomavgift bensinbilk
RTaxYEl = RoadTaxEl*KmY  # Årlig bomavgift elbil


#%% 
#  Calculate and present the final results with insurance

# Electric car:
FinalEl = FsEl + InsFeeYear + ElFuelCar + RTaxYEl

# Petrol fuel car
FinalBen = FsBen + InsFeeYear + PetFuelCar + RTaxYBen

print("Oversikt over årlige kostnader for elbil og bensinbil.")
print("Med årlig kjørelengde 15.000 km ser det slik ut:\n")
print(f'Total årlig kostnad for elbil er kr: {FinalEl:.1f}')
print(f"Total årlig kostnad for bensinbil er kr: {FinalBen:.1f}")
print("Kostnadsdifferanse per år (Bensin - Elbil) er kr:", FinalBen - FinalEl)

# The End


