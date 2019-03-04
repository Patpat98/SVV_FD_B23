# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:16:42 2019

@author: patri
"""

import numpy as np
import matplotlib.pyplot as plt

def getStateSpace(C1,C2,C3):
    
    #This function takes the analytically determiner C1, C2 and C3 as inputs
    #Outputs the state space model in the following form:
    ################# x_dot = Ax+Bu
    ################# y=Cx+Du