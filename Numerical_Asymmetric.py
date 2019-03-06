# -*- coding: utf-8 -*
"""
Created on Mon Mar  4 17:16:42 2019

@author: patri
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def getStateSpaceGeneral(C1,C2,C3):
    
    #This function takes the analytically determiner C1, C2 and C3 as inputs
    #Outputs the state space model in the following form:
    ################# x_dot = Ax+Bu
    ################# y=Cx+Du
    A=-C.inv.multiply(C2)
    B=-C.inv.multiply(C3)
    
    return A,B
    
    

###MAIN###


#C1=sp.Matrix([[CYb,0, 0, 0],[0,-0.5*(b/V),0,0],[0,0,-4*mub*KX2,4*mub*KXZ*(b/(2*V))],[Cnb*(b/V),0,4*mub*KXZ*(b/2V),-4*mub*KZ2*(b/2V)]])

sp.var('a,b,c,d,e,f,g,h,r,')

test1=sp.Matrix([a,b],[c,d])
test2=sp.Matrix([e,f],[g,h])
test3=sp.Matrix([g,r],[f,d])

out=getStateSpaceGeneral(test1,test2,test3)
print(out)