# -*- coding: utf-8 -*
"""
Created on Mon Mar  4 17:16:42 2019

@author: patri
"""

import numpy as np
import matplotlib.pyplot as plt

#from sympy import *
from control import *
from Cit_par import *



def getStateSpaceGeneral(C1,C2,C3,m,s,r):
    
    #This function takes the analytically determiner C1, C2 and C3 as inputs
    #Outputs the state space model in the following form:
    ################# x_dot = Ax+Bu
    ################# y=Cx+Du
    C1_inv=C1_inv= np.linalg.inv(C1)
    A=np.matmul(-C1_inv, C2)
    B=np.matmul(-C1_inv, C3)
    
    C=np.zeros((s,m))
    for i in range(len(C)):
        C[i,i]=1.
#    C=np.matrix([[1,0,0,0]])
    D=np.zeros((s,r))
#    D=np.matrix([[0,0]])
    return A,B,C,D
    
    

###MAIN###

#('C1 C2 C3 c V0 muc KY2 CXu CX0 CXa CXq CXde CL Cnp Cnr CYp Clb Clp Clr CXadot CZu CZ0 CZa CZq CZde CZadot Cmu Cmadot Cmq Cmde Cma b CYr mub Cnb CYb KX2 KXZ KZ2 CYda CYdr Clda Cldr Cnda Cndr')

#C1=np.matrix([[CYb,0, 0, 0],[0,-0.5*(b/V0),0,0],[0,0,-4*mub*KX2*(b**2/(2*V0**2)),4*mub*KXZ*(b/(2*V0))],[Cnb*(b/V0),0,4*mub*KXZ*(b/(2*V0)),-4*mub*KZ2*(b/(2*V0))]])
#C2=np.matrix([[CYb,CL,CYp*(b/(2*V0)),(CYr-4*mub)*(b/(2*V0))],[0,0,(b/2*V0),0], [Clb,0,Clp*(b/2*V0), Clr*(b/2*V0)],[Cnb,0,Cnp*(b/(2*V0)),Cnr*(b/(2*V0))]])
#C3=np.matrix([[CYda,CYdr],[0,0],[Clda,Cldr],[Cnda,Cndr]])

#C1=np.matrix([[(CYb-2*mub)*(b/V0),0, 0, 0],[0,-0.5*(b/V0),0,0],[0,0,-4*mub*KX2*(b/(V0)),4*mub*KXZ*(b/(V0))],[Cnb*(b/V0),0,4*mub*KXZ*(b/(V0)),-4*mub*KZ2*(b/(V0))]])
#C2=np.matrix([[CYb,CL,CYp,(CYr-4*mub)],[0,0,1,0], [Clb,0,Clp, Clr],[Cnb,0,Cnp,Cnr]])
#C3=np.matrix([[CYda,CYdr],[0,0],[Clda,Cldr],[Cnda,Cndr]])
#C3=np.matrix([[0,0],[0,0],[0,0],[0,0]])

C1=np.matrix([[(CYbdot-2*mub),0, 0, 0],[0,-0.5,0,0],[0,0,-4*mub*KX2,4*mub*KXZ],[Cnbdot,0,4*mub*KXZ,-4*mub*KZ2]])
C2=np.matrix([[CYb,CL,CYp,(CYr-4*mub)],[0,0,1,0], [Clb,0,Clp, Clr],[Cnb,0,Cnp,Cnr]])
C3=np.matrix([[CYda,CYdr],[0,0],[Clda,Cldr],[Cnda,Cndr]])


######INITIATE STATE SPACE######
A=getStateSpaceGeneral(C1,C2,C3,4,4,2)[0]
B=getStateSpaceGeneral(C1,C2,C3,4,4,2)[1]
C=getStateSpaceGeneral(C1,C2,C3,4,4,2)[2]
D=getStateSpaceGeneral(C1,C2,C3,4,4,2)[3]

sys=StateSpace(A,B,C,D)

#Determine the eigenvalues of matrix A
eigs=(np.linalg.eig(A))

#This is the time vector
T=np.arange(0,100,0.1)


####SUBJECT SYSTEM TO impulse RESPONSES####
#The impulse input to the aileron and rudder should be separated for meaningful results for each motion

#Here select the input index: 0=aileron, 1=rudder
input_index=0

T,y=impulse_response(sys,T,X0=0.0,input=input_index)


#####PLOTTING#####
fig=plt.figure()
plt.subplot(211)
plt.plot(T,y[0])

plt.subplot(212)
plt.plot(T,y[1])

plt.subplot(213)
plt.plot(T,y[2])

plt.subplot(214)
plt.plot(T,y[3])

plt.show()
















