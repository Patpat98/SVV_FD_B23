#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:02:47 2019

@author: edmundo
"""

from eigenmotions import times, order, index
from matdata import parameters, dictionary


mass_original = 6704.218

lh_engine_FU = dictionary["lh_engine_FU"]
rh_engine_FU = dictionary["rh_engine_FU"]

mass= []

for i in range(len(lh_engine_FU)):
    mass0 = mass_original - (lh_engine_FU[i]*0.453592) - (rh_engine_FU[i]*0.453592)
    mass.append(mass0)
    
print(mass)

#Find mass at each point