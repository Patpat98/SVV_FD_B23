# -*- coding: utf-8 -*
"""
Created on Mon Mar  4 17:16:42 2019

@author: patri
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def getStateSpaceGeneral(C1,C2,C3):
    
    #This function takes the analytically determiner C1, C2 and C3 as inputs
    #Outputs the state space model in the following form:
    ################# x_dot = Ax+Bu
    ################# y=Cx+Du
    C1_inv=-C1.inv()
    A=-C1_inv.multiply(C2)
    B=-C1_inv.multiply(C3)
    
    return A,B
    
    

###MAIN###

var('C1 C2 C3 c V0 muc KY2 CXu CX0 CXa CXq CXde CL Cnp Cnr CYp Clb Clp Clr CXadot CZu CZ0 CZa CZq CZde CZadot Cmu Cmadot Cmq Cmde Cma b CYr mub Cnb CYb KX2 KXZ KZ2 CYda CYdr Clda Cldr Cnda Cndr')

C1=Matrix([[CYb,0, 0, 0],[0,-0.5*(b/V0),0,0],[0,0,-4*mub*KX2,4*mub*KXZ*(b/(2*V0))],[Cnb*(b/V0),0,4*mub*KXZ*(b/(2*V0)),-4*mub*KZ2*(b/(2*V0))]])
C2=Matrix([[CYb,CL,CYp*(b/(2*V0)),(CYr-4*mub)*(b/(2*V0))],[0,0,(b/2*V0),0], [Clb,0,Clp*(b/2*V0), Clr*(b/2*V0)],[Cnb,0,Cnp*(b/(2*V0)),Cnr*(b/(2*V0))]])
C3=Matrix([[CYda,CYdr],[0,0],[Clda,Cldr],[Cnda,Cndr]])

statespace=getStateSpaceGeneral(C1,C2,C3)
print('A =', statespace[0])
print('B =', statespace[1])









###TEST CASE###
#var('a b c d e f g h r')
#test1=Matrix([[a,b],[c,d]])
#test2=Matrix([[e,f],[g,h]])
#test3=Matrix([[g,r],[f,d]])
#
#out=getStateSpaceGeneral(test1,test2,test3)
#print(out)