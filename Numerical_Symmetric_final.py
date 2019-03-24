# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:43:57 2019

@author: patri
"""
import numpy as np
import matplotlib.pyplot as plt
from control import *
import control.matlab
from Cit_par import *
import scipy as sp
from column_fe_plot import *
#from Plot_flightdata import *
import sys
sys.path.insert(0,'/Users/patri/documents/Year 3/Simulation, Verification and Validation/Flight Dynamics/SVV_FD_B23/Python M')
from graph1 import *
from matdata import *


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

C1=np.matrix([[-2*muc,0,0,0],[0,(CZadot-2*muc), 0, 0],[0,0,-1,0],[0,Cmadot,0,-2*muc*KY2]])
C2=np.matrix([[CXu,CXa, CZ0,0],[CZu,CZa, -CX0, (CZq+2*muc)],[0,0,0,1],[Cmu, Cma, 0, Cmq]])
C3=np.matrix([[CXde],[CZde],[0],[Cmde]])


######INITIATE STATE SPACE######
A=getStateSpaceGeneral(C1,C2,C3,4,4,1)[0]
B=getStateSpaceGeneral(C1,C2,C3,4,4,1)[1]
C=getStateSpaceGeneral(C1,C2,C3,4,4,1)[2]
D=getStateSpaceGeneral(C1,C2,C3,4,4,1)[3]

sys=StateSpace(A,B,C,D)

#Determine the eigenvalues of matrix A
eigs=(np.linalg.eig(A))
print("Eigenvalues are", eigs)

#From these get other comparable parameters
half_amp_1 = (np.log(0.5)*c)/(np.real(eigs[0][0])*V0)
half_amp_2 = (np.log(0.5)*c)/(np.real(eigs[0][2])*V0)
damping_1=(-np.real(eigs[0][0]))/(np.sqrt(np.real(eigs[0][0])**2+np.real(eigs[0][0])**2))
damping_2=(-np.real(eigs[0][1]))/(np.sqrt(np.real(eigs[0][1])**2+np.real(eigs[0][2])**2))
t_damp_halfamp_1=(np.log(0.5))/np.real(eigs[0][0])
t_damp_halfamp_2=(np.log(0.5))/np.real(eigs[0][2])



#This is the time vector


####SUBJECT SYSTEM TO IMPULSE RESPONSES####
##The impulse input to the aileron and rudder should be separated for meaningful results for each motion

##Here select the input index: 0=aileron, 1=rudder
input_index=0
#T,y=impulse_response(sys,T,X0=0.0,input=input_index)

##Plotting the responses to non zero initial conditions
#X0=[[1],[1],[1],[1]]

#####RESPONSES TO PILOT INPUTS FOR VARIOUS MOTIONS THROUGHOUT THE FLIGHT####

state_1=np.array(state_1)
state_2=np.array(state_2)
state_3=np.array(state_3)
state_4=np.array(state_4)
state_1=state_1-state_1[0]
state_2=state_2-state_2[0]
state_3=state_3-state_3[0]
state_4=state_4-state_4[0]

aileron_input=yaxis1

elevator_input=yaxis2
steps=length_of_time*10

T=np.arange(0,steps,1)


y,T,xout=control.matlab.lsim(sys,elevator_input,T,X0=0.)


#####PLOTTING#####

fig=plt.figure()
plt.subplot(211)
plt.plot(T,xout[:,0]*V0)
plt.plot(time1, state_1)
plt.xlabel('Time[s]')
plt.ylabel('V[m/s]')
plt.grid()

plt.subplot(212)
plt.plot(T,xout[:,1]*180/np.pi)
plt.plot(time1, state_2)
plt.xlabel('Time[s]')
plt.ylabel('alpha[rad]')
plt.grid()

fig=plt.figure()
plt.subplot(211)
plt.plot(T,xout[:,2]*180/np.pi)
plt.plot(time1, state_3)
plt.xlabel('Time[s]')
plt.ylabel('theta[rad] (pitch)')
plt.grid()

plt.subplot(212)
plt.plot(T,(xout[:,3]/(c/(V0)))*180/np.pi)
plt.plot(time1, state_4)
plt.xlabel('Time[s]')
plt.ylabel('q[rad/s] (pitch rate)')
plt.grid()

plt.show()