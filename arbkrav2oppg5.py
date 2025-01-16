# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:06:55 2025

Oppgave 5 består i å beregne areal og omkrets av en figur bestående av
en rettviklet trekant med en halvsirkel på lille katet.
Beregningen skal utføres av en funksjon.

Resources used:
      https://www.matematikk.org/oss.html?tid=88992 (areal av trekant)
      https://www.matematikk.org/artikkel.html?tid=155041&within_tid=155190
      
    
@author: ole.skurdal
olsku9661@usn.no
"""

#%% Import packages

import numpy as np

#%% Definer funksjonen vi skal bruke først i programmet
#

def beregnAogO(kortKatet, langKatet):
    # En docstring kan vises ved kommando: help(beregnAogO) i konsollet
    """Funksjonen gjør følgende:
    Basert på lengden av de 2 katetene i trekanten beregner funksjonen
    areal og omkrets av rettvinklet trekant med en halvsirkel på kort katet
    Funksjonen returnerer figurens areal og omkrets
    """
    # Beregner hypotenusen vha. Pythagoras setning, trenger den til omkretsen
    hypotenus = np.sqrt(kortKatet**2 + langKatet**2)
    # Beregner arealet av trekanten
    arealTrekant = (kortKatet*langKatet)/2
    
    # Beregner sirkel, radius er 1/2 parten av kort katet som er lik diameteren
    radiusSirkel = kortKatet/2  # diameter / 2
    arealSirkel = np.pi*radiusSirkel**2  # A = πr²
    arealHalvSirkel = arealSirkel / 2
    omkretsSirkel = 2*np.pi*radiusSirkel  # O = 2πr
    omkretsHalvSirkel = omkretsSirkel / 2
    
    figurAreal = arealTrekant + arealHalvSirkel
    figurOmkrets = langKatet + hypotenus + omkretsHalvSirkel
    
    return (figurAreal, figurOmkrets)

    
#%% Request input
# Vi trenger lengden av begge katetene i trekanten

print("Vi regner areal og omkrets av en figur og trenger følgende:\n")
kortK = float(input("Hvor lang er den korte kateten i trekanten: " ))
langK = float(input("Hvor lang er den lange kateten i trekanten: " ))

# Vi overlater til funksjonen beregnAogO selve utregningen og kaller den
(areal, omkrets) = beregnAogO(kortK, langK)

# Skriv ut verdiene vi får tilbake fra funksjonen
print(f"\nArealet av hele figuren er: {areal:.2f}")
print(f"Omkrets av hele figuren er: {omkrets:.2f}")

# The End
