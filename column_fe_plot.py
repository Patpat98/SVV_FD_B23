#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:19:17 2019

@author: edmundo
"""

import os
import matplotlib.pyplot as plt 

# Open the file
script_dir = os.path.dirname("/home/edmundo/Desktop/SVV/FLIGHT/Mat/") #<-- absolute dir the script is in
rel_path = "column_fe.txt"
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
plt.xlabel("Time (s)") 
plt.ylabel("Force on elevator control wheel (N)") 
plt.show()
        