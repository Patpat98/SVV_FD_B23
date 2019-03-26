#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:30:38 2019

@author: edmundo
"""

import os
import pickle
import math
import matplotlib.pyplot as plt 
from eigenmotions import times, order, index


# Open the file with the mat file parameters
script_dir = os.path.dirname("/home/edmundo/Desktop/SVV/SVV_FD_B23/") #<-- absolute dir the script is in
rel_path = "mat_file_parameters.txt"
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

#print(parameters)



# CREATE A DICTIONARY WITH ALL VARIABLE NAMES AND THEIR VALUES.

dictionary={}

#Set the keys of the dictionaty to the names of the parameters.
for i in range(len(parameters)):
    dictionary[parameters[i]] = [] 

#print(dictionary)


#Append to the value of each key an array containing all the values of the measurement
#Obtained from the corresponding file.
for z in range(len(parameters)):
    directory = os.path.dirname("/home/edmundo/Desktop/SVV/SVV_FD_B23/Mat/")
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

for i in range(len(dictionary['vane_AOA'])):    
    dictionary['vane_AOA'][i] = dictionary['vane_AOA'][i] * math.pi/180
    dictionary['elevator_dte'][i] = dictionary['elevator_dte'][i] * math.pi/180
    dictionary['lh_engine_FU'][i] = dictionary['lh_engine_FU'][i] * 0.453592
    dictionary['rh_engine_FU'][i] = dictionary['rh_engine_FU'][i] * 0.453592
    dictionary['delta_a'][i] = dictionary['delta_a'][i] * math.pi/180
    dictionary['delta_e'][i] = dictionary['delta_e'][i] * math.pi/180
    dictionary['delta_r'][i] = dictionary['delta_r'][i] * math.pi/180
    dictionary['Ahrs1_Roll'][i] = dictionary['Ahrs1_Roll'][i] * math.pi/180
    dictionary['Ahrs1_Pitch'][i] = dictionary['Ahrs1_Pitch'][i] * math.pi/180
    dictionary['Ahrs1_bRollRate'][i] = dictionary['Ahrs1_bRollRate'][i] * math.pi/180
    dictionary['Ahrs1_bPitchRate'][i] = dictionary['Ahrs1_bPitchRate'][i] * math.pi/180
    dictionary['Ahrs1_bYawRate'][i] = dictionary['Ahrs1_bYawRate'][i] * math.pi/180
    dictionary['Dadc1_sat'][i] = dictionary['Dadc1_sat'][i] + 273.15
    dictionary['Dadc1_tat'][i] = dictionary['Dadc1_tat'][i] + 273.15
    dictionary['Dadc1_alt'][i] = dictionary['Dadc1_alt'][i] * 0.3048
    dictionary['Dadc1_bcAlt'][i] = dictionary['Dadc1_bcAlt'][i] * 0.3048
    dictionary['Dadc1_cas'][i] = dictionary['Dadc1_cas'][i] * 0.514444
    dictionary['Dadc1_tas'][i] = dictionary['Dadc1_tas'][i] * 0.514444
    dictionary['Dadc1_altRate'][i] = dictionary['Dadc1_altRate'][i] * 0.3048
    
# Find the mass at each point__________________________________________________
    
mass_original = 6704.218

lh_engine_FU = dictionary["lh_engine_FU"]
rh_engine_FU = dictionary["rh_engine_FU"]

mass= []

for i in range(len(lh_engine_FU)):
    mass0 = mass_original - (lh_engine_FU[i]) - (rh_engine_FU[i])
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


    
    
