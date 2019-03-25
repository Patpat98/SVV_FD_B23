#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:44:51 2019

@author: edmundo
"""

#Store the time of eigen motions in an array

AperiodicRoll = 59*60 + 10
ShortPeriod = 1*3600 + 35
Phugoid = 53*60 + 57
DutchRoll = 1*3600 + 1*60 + 57
DutchRollYD = 1*3600 + 2*60 + 47
Spiral = 1*3600 + 5*60 + 20

times = [AperiodicRoll, ShortPeriod, Phugoid, DutchRoll, DutchRollYD, Spiral]
order = ['AperiodicRoll', 'ShortPeriod', 'Phugoid', 'DutchRoll', 'DutchRollYD', 'Spiral']

index = []
for i in range(len(times)):
    ind = int(times[i])*10
    index.append(ind)


print(times)
print(order)
print(index)