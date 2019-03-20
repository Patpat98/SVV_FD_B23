# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:42:49 2019

@author: patri
"""

import numpy as np
import matplotlib.pyplot as plt
from control import *
import control.matlab
from Cit_par import *
import scipy as sp
from column_fe_plot import *

Force_control_wheel=np.array(Force_control_wheel)

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
print("Eigenvalues are", eigs)

#From these get other comparable parameters
half_amp= (np.log(0.5)*c)/(np.real(eigs[0][1])*V0)
damping=(-np.real(eigs[0][1]))/(np.sqrt(np.real(eigs[0][1])**2+np.real(eigs[0][1])**2))
t_damp_halfamp=(-np.log(0.5))/np.real(eigs[0][1])




#This is the time vector
T=np.arange(0,4695.1,0.1)

elevator_input = np.column_stack((np.zeros(46951),Force_control_wheel))


####SUBJECT SYSTEM TO IMPULSE RESPONSES####
#The impulse input to the aileron and rudder should be separated for meaningful results for each motion

#Here select the input index: 0=aileron, 1=rudder
input_index=0

#T,y=impulse_response(sys,T,X0=0.0,input=input_index)

#Plotting the responses to non zero initial conditions
#X0=[[1],[1],[1],[1]]

y,T,xout=control.matlab.lsim(sys,elevator_input,T,X0=0.)

#Plotting the response from flight data elevator force


#Here try and compare with pilot input




#####PLOTTING#####
fig=plt.figure()
plt.subplot(211)
plt.plot(T,xout[:,0])
plt.xlabel('Time[s]')
plt.ylabel('Beta[rad]')
plt.grid()

plt.subplot(212)
plt.plot(T,xout[:,1])
plt.xlabel('Time[s]')
plt.ylabel('Phi[rad]')
plt.grid()

fig=plt.figure()
plt.subplot(211)
plt.plot(T,xout[:,2])
plt.xlabel('Time[s]')
plt.ylabel('p [rad/s]')
plt.grid()

plt.subplot(212)
plt.plot(T,xout[:,3])
plt.xlabel('Time[s]')
plt.ylabel('r [rad/s]')
plt.grid()

plt.show()