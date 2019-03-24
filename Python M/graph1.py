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

###Here specify if either symmetric or assymmetric case

symmetric=False

eigenmotion = "AperiodicRoll"
length_of_time = 50 #in seconds
interest1 = "delta_a"
interest2 = "delta_e"

#--------------------------IMPORT THE GPS COORDINATES--------------------------
# Open the file
script_dir = os.path.dirname("/Users/patri/documents/Year 3/Simulation, Verification and Validation/Flight Dynamics/SVV_FD_B23/") #<-- absolute dir the script is in
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


if symmetric:
    state_1 = dictionary["Dadc1_tas"][index[n]:(index[n]+length_of_time*10)]
    state_2 = dictionary["vane_AOA"][index[n]:(index[n]+length_of_time*10)]
    state_3 = dictionary["Ahrs1_Pitch"][index[n]:(index[n]+length_of_time*10)]
    state_4 = dictionary["Ahrs1_bPitchRate"][index[n]:(index[n]+length_of_time*10)]
    V_0=state_1[0]
    alpha_0=state_2[0]
    pitch_0=state_3[0]
    
    
else:
    state_1 = dictionary["Ahrs1_Roll"][index[n]:(index[n]+length_of_time*10)]
    state_2 = dictionary["Ahrs1_bRollRate"][index[n]:(index[n]+length_of_time*10)]
    state_3 = dictionary["Ahrs1_bYawRate"][index[n]:(index[n]+length_of_time*10)]
    state_4=dictionary["Dadc1_tas"][index[n]:(index[n]+length_of_time*10)]
    #Speed at the beginning of maneuver, V0 for asymmetric numerical model
    V_0=state_4[0]
    alpha_0=dictionary["vane_AOA"][index[n]:(index[n]+length_of_time*10)][0]
    pitch_0=dictionary["Ahrs1_Pitch"][index[n]:(index[n]+length_of_time*10)][0]

Alt_0=dictionary['Dadc1_bcAlt'][index[n]:(index[n]+length_of_time*10)][0] 


#print(len(x_axis))


# Parameters
yaxis1 = dictionary[interest1][index[n]:(index[n]+length_of_time*10)]
yaxis2 = dictionary[interest2][index[n]:(index[n]+length_of_time*10)]

time1 = []
for i in range(length_of_time*10):
    time1.append(i)


####PLOTTING###
#
###Here the pilot inputs are plotted:
#fig=plt.figure()
##Plot1
#plt.subplot(211)
#plt.plot(time1, yaxis1)
#plt.ylabel(interest1) 
##Plot2
#plt.subplot(212)
#plt.plot(time1, yaxis2)
#plt.xlabel("Time (0.1 sec)") 
#plt.ylabel(interest2) 
#
###Here we plot the state outputs over the specified time
#fig=plt.figure()
##Plot3
#plt.subplot(411)
#plt.plot(time1, state_1)
#plt.xlabel("Time (0.1 sec)") 
#if symmetric:
#    plt.ylabel("u")
#else:
#    plt.ylabel("Roll")
#
##Plot4
#plt.subplot(412)
#plt.plot(time1, state_2)
#plt.xlabel("Time (0.1 sec)") 
#if symmetric:
#    plt.ylabel("AOA")
#else:
#    plt.ylabel("Roll Rate") 
#plt.suptitle(eigenmotion, fontsize=16)
##Plot5
#plt.subplot(413)
#plt.plot(time1, state_3)
#plt.xlabel("Time (0.1 sec)") 
#if symmetric:
#    plt.ylabel("Pitch")
#else:
#    plt.ylabel("Yaw Rate") 
#plt.suptitle(eigenmotion, fontsize=16)
#
#plt.subplot(414)
#plt.plot(time1, state_4)
#plt.xlabel("Time (0.1 sec)") 
#if symmetric:
#    plt.ylabel("Pitch Rate")
#else:
#    plt.ylabel("TAS") 
#plt.suptitle(eigenmotion, fontsize=16)
#
#plt.show()