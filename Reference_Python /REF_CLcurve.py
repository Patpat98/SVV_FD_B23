#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:12:40 2019

@author: edmundo
"""
import os
import matplotlib.pyplot as plt 

# Open the file
script_dir = os.path.dirname("/home/edmundo/Desktop/SVV/FLIGHT/Mat/") #<-- absolute dir the script is in
rel_path = "Dadc1_alt.txt"
abs_file_path = os.path.join(script_dir, rel_path)

AOA = []
time = []

with open(abs_file_path, 'r') as fp:
    for x in fp:
        AOA.append(float(x))

for i in range(0, len(AOA)):
    time.append(i/10)
    
print(AOA)
    
plt.plot(time, AOA)
plt.show()
        
#print(len(AOA))
        
