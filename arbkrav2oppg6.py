# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:06:55 2025

Oppgave 6:
Oppgaven består i å plotte en funksjon 𝑓(𝑥)= −𝑥**2 − 5

Resources used:
    https://matplotlib.org/ 
      
@author: ole.skurdal
olsku9661@usn.no
"""

#%% Import packages

import numpy as np
import matplotlib.pyplot as plt

#%% Definer funksjon, utfør beregning og plott

# Definer ligningen som en funksjonen
def f(x):
    return -x**2 -5

plt.close('all')  # Lukk alle figurvinduer

# Lag en array av x-verdier
x = np.linspace(-10, 10, 200)  # 200 verdier fra -10 til 10

# Kall funksjonen f(x) og beregn y-verdiene
y = f(x)

# Plot grafen
plt.figure(1, figsize=(6, 4), layout='constrained') 
plt.plot(x, y, label=r'$f(x) = -x^2 - 5$', color="red")  # Lager grafen med label

# Legg til tittel og etiketter
plt.title("Graf av funksjonen $f(x) = -x^2 - 5$")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Lag x-akse
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Lag y-akse
plt.grid(True)  # Tegn rutenett
plt.legend()  # Vis legend

# Skriver et plot av grafen til en fil (fjern #)
#plt.savefig("GrafOppg2_6Ole.pdf", format="pdf", dpi=600, facecolor="white")
# Vis grafen
plt.show()

# The End
