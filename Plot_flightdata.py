#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:17:58 2019

@author: edmundo
"""
import os
import matplotlib.pyplot as plt 
# =============================================================================
from mpl_toolkits.mplot3d import Axes3D 
#from eigenmotions import times, order
# =============================================================================

#To see the plot in a new window:
# Using Spyder menu options Tools -> Preferences -> Graphics Tab -> and changed the setting to Automatic (from default Inline).

# Open the file
script_dir = os.path.dirname("") #<-- absolute dir the script is in
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
            
            
# Initial time
start = int(time[0][:2])*3600 + int(time[0][3:5])*60 + int(time[0][6:])

for i in range(len(time)):
    time[i] = int(time[i][:2])*3600 + int(time[i][3:5])*60 + int(time[i][6:]) - start
    



#fig = plt.figure(1)
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(xaxis, yaxis, zaxis, c=time, cmap='gnuplot')
#plt.axis(autoscale_on = True)
#plt.colorbar()
#plt.show


#Coment above and Uncoment below to show ground track and altitude vs time

# =============================================================================
# plt.figure(2)
# #Ground map
# plt.subplot(211)
# plt.scatter(xaxis, yaxis, c=zaxis, cmap='winter')
# #Altitude vs Time
# plt.subplot(212)
# plt.scatter(time, zaxis, c=zaxis, cmap='cool')
# =============================================================================

