#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:32:02 2019

@author: edmundo
"""

#------------------- GRAPH MAKER ----------------------------------------------
import matplotlib.pyplot as plt 
from matdata import parameters, dictionary
from eigenmotions import times, order, index


#------------------------------------------------------------------------------
#Write parameter of interest. Eg: Ahrs1_Roll, written as in the file mat_file_parameters.txt
#Write eigenmotions to be compared and length of time in seconds

length_of_time = 30 #in seconds
interest = "Ahrs1_Roll"
eigenmotion1 = "DutchRoll"
eigenmotion2 = "DutchRollYD"




#-----------------------PROGRAM-------------------------------------------

n1 = order.index(eigenmotion1)
n2 = order.index(eigenmotion2)

xaxis1 = dictionary[interest][index[n1]:(index[n1]+length_of_time*10)]
xaxis2 = dictionary[interest][index[n2]:(index[n2]+length_of_time*10)]
time1 = []
for i in range(length_of_time*10):
    time1.append(i)



plt.figure(2)
#DutchRoll
plt.subplot(211)
plt.scatter(time1, xaxis1)
plt.ylabel(eigenmotion1) 
#DutchRollYD
plt.subplot(212)
plt.scatter(time1, xaxis2)
plt.xlabel("Time (0.1 sec)") 
plt.ylabel(eigenmotion2) 
plt.suptitle(interest, fontsize=16)

