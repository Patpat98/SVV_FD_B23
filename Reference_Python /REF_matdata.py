#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:30:38 2019

@author: edmundo
"""

import os
import pickle
import matplotlib.pyplot as plt 
from REF_eigenmotions import times, order, index


# Open the file with the mat file parameters
script_dir = os.path.dirname("/home/edmundo/Desktop/SVV/SVV_FD_B23/Reference Data/") #<-- absolute dir the script is in
rel_path = "REF_mat_file_parameters.txt"
abs_file_path = os.path.join(script_dir, rel_path)


#Store all the parameter names in an array.
parameters = []
with open(abs_file_path, 'r') as fp:
    for line in fp:
        line = line.replace('\n', '').replace("'", '')
        result = [x.strip() for x in line.split(',')]
        parameters.append(result[0])

del parameters[-1]
del parameters[-1]

print(parameters)



# CREATE A DICTIONARY WITH ALL VARIABLE NAMES AND THEIR VALUES.

dictionary={}

#Set the keys of the dictionaty to the names of the parameters.
for i in range(len(parameters)):
    dictionary[parameters[i]] = [] 

#print(dictionary)


#Append to the value of each key an array containing all the values of the measurement
#Obtained from the corresponding file.
for z in range(len(parameters)):
    directory = os.path.dirname("/home/edmundo/Desktop/SVV/SVV_FD_B23/Reference Data/")
    file = parameters[z] + ".txt"
    path = os.path.join(directory, file)
    array = []
    with open(path, 'r') as txt:
        for line in txt:
            array.append(float(line))
    dictionary[parameters[z]] = array

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
# Find the mass at each point__________________________________________________
    
payload_mass = 695
OEW = 9165*0.453592
fuel_mass = 4050*0.453592
mass_original = payload_mass + OEW + fuel_mass
lh_engine_FU = dictionary["lh_engine_FU"]
rh_engine_FU = dictionary["rh_engine_FU"]

mass= []

for i in range(len(lh_engine_FU)):
    mass0 = mass_original - (lh_engine_FU[i]*0.453592) - (rh_engine_FU[i]*0.453592)
    mass.append(mass0)
    

    


#------------------------------------------------------------------------------
# -------------Find values for a table, work with Emilie-----------------------
#---------------------------------------------------------------------------
required = ["Dadc1_alt", "Dadc1_tas", "vane_AOA", "Ahrs1_Pitch"]
required2 = ["Dadc1_alt", "Dadc1_tas", "vane_AOA", "Ahrs1_Pitch", "mass", "CD0"]

required_dictionary = {}
for k in range(len(order)):
    array = []
    for g in range(len(required)):
        array.append(dictionary[required[g]][index[k]])
    array.append(mass[index[k]])
    
    required_dictionary[order[k]] = array
    
for r in range(len(required_dictionary)):
    required_dictionary[order[r]][0] = required_dictionary[order[r]][0] * 0.3048
    required_dictionary[order[r]][1] = required_dictionary[order[r]][1] * 0.514444
#print (required_dictionary) 

fuel_used = []
for u in range(len(order)):
    fuel_used.append(mass_original - required_dictionary[order[u]][4])
 
#print(fuel_used)   

for i in range(len(order)):
    print(required_dictionary[order[i]][0])
    

for i in range(len(order)):
    print(dictionary["Dadc1_tat"][index[i]])

print(required_dictionary)
#------------------------------------------------------------------------------
# -------------End of finding the values for the table ------------------------
#------------------------------------------------------------------------------


    
    
