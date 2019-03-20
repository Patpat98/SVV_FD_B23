#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:02:47 2019

@author: edmundo
"""

from eigenmotions import times, order, index
from matdata import parameters, dictionary
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


mass_original = 6704.218

lh_engine_FU = dictionary["lh_engine_FU"]
rh_engine_FU = dictionary["rh_engine_FU"]

mass= []

for i in range(len(lh_engine_FU)):
    mass0 = mass_original - (lh_engine_FU[i]*0.453592) - (rh_engine_FU[i]*0.453592)
    mass.append(mass0)
    
time = []
for i in range(len(mass)):
    time.append(i)


def fit_func(x, a, b):
    return a*x + b

params = curve_fit(fit_func, time, mass)

[a, b] = params[0]

line = []
for i in range(len(mass)):
    line.append(a*time[i] + b)


print()

plt.plot(time, mass)
#plt.plot(time, line)
plt.xlabel("Time (0.1 sec)")
plt.ylabel("Mass (kg)") 
