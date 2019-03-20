#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:20:15 2019

@author: edmundo
"""

#------------------- GRAPH MAKER ----------------------------------------------
import os
import matplotlib.pyplot as plt 
from matdata import parameters, dictionary
from eigenmotions import times, order, index
#from Plot_flightdata import xaxis, yaxis, zaxis


#------------------------------------------------------------------------------
#Write eigenmotion of interest. 'AperiodicRoll', 'ShortPeriod', 'Phugoid', 'DutchRoll', 'DutchRollYD', 'Spiral'
#Write parameters to be compared and length of time in seconds. Eg: Ahrs1_Roll, written as in the file mat_file_parameters.txt

eigenmotion = "DutchRoll"
length_of_time = 60 #in seconds
interest1 = "delta_a"
interest2 = "delta_e"

#--------------------------IMPORT THE GPS COORDINATES--------------------------
# Open the file
script_dir = os.path.dirname("/home/edmundo/Desktop/SVV/FLIGHT/") #<-- absolute dir the script is in
rel_path = "gps.txt"
abs_file_path = os.path.join(script_dir, rel_path)

time = []
xaxis = []
yaxis = []
zaxis = []
with open(abs_file_path, 'r') as fp:
    for x in fp:
        if (x[:6] == "<when>"):
            time.append(x[17:25])
        if (x[:10] == "<gx:coord>"):
            xdir, ydir, zdir = x.split()
            xaxis.append(float(x[10:28]))
            yaxis.append(float(ydir))
            zaxis.append(int(zdir.replace('</gx:coord>', '')))

#-----------------------PROGRAM-------------------------------------------
n = order.index(eigenmotion)

#GPS coordinates:
x_axis = dictionary["Ahrs1_Roll"][index[n]:(index[n]+length_of_time*10)]
y_axis = dictionary["Ahrs1_Pitch"][index[n]:(index[n]+length_of_time*10)]
z_axis = dictionary["Dadc1_bcAlt"][index[n]:(index[n]+length_of_time*10)]

print(len(x_axis))



# Parameters
yaxis1 = dictionary[interest1][index[n]:(index[n]+length_of_time*10)]
yaxis2 = dictionary[interest2][index[n]:(index[n]+length_of_time*10)]
time1 = []
for i in range(length_of_time*10):
    time1.append(i)


plt.figure(2)
#Plot1
plt.subplot(511)
plt.scatter(time1, yaxis1)
plt.ylabel(interest1) 
#Plot2
plt.subplot(512)
plt.scatter(time1, yaxis2)
plt.xlabel("Time (0.1 sec)") 
plt.ylabel(interest2) 
#Plot3
plt.subplot(513)
plt.scatter(time1, x_axis)
plt.xlabel("Time (0.1 sec)") 
plt.ylabel("Ahrs1_Roll") 
#Plot4
plt.subplot(514)
plt.scatter(time1, y_axis)
plt.xlabel("Time (0.1 sec)") 
plt.ylabel("Ahrs1_Pitch") 
plt.suptitle(eigenmotion, fontsize=16)
#Plot5
plt.subplot(515)
plt.scatter(time1, z_axis)
plt.xlabel("Time (0.1 sec)") 
plt.ylabel("Altitude") 
plt.suptitle(eigenmotion, fontsize=16)
