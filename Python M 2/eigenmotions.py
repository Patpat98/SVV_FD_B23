#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:44:51 2019

@author: edmundo
"""

#Store the time of eigen motions in an array

AperiodicRoll = 51*60 + 13
ShortPeriod = 52*60 + 3
Phugoid = 53*60 + 21
DutchRoll = 56*60 + 14
DutchRollYD = 57*60 + 7
Spiral = 1*3600 + 1*60 + 10

times = [AperiodicRoll, ShortPeriod, Phugoid, DutchRoll, DutchRollYD, Spiral]
order = ['AperiodicRoll', 'ShortPeriod', 'Phugoid', 'DutchRoll', 'DutchRollYD', 'Spiral']

index = []
for i in range(len(times)):
    ind = int(times[i])*10
    index.append(ind)


print(times)
print(order)
print(index)