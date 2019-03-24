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
    return A,B,C,B
    
    

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
steps=length_of_time*10
T=np.arange(0,steps,1)

####SUBJECT SYSTEM TO IMPULSE RESPONSES####

#Here select the input index: 0=aileron, 1=rudder
input_index=0

#T,y=impulse_response(sys,T,X0=0.0,input=input_index)

#Plotting the responses to non zero initial conditi5ons
X0=[[1],[50],[3.4],[4]]

aileron_input=yaxis1
rudder_input=yaxis3

aileron_input_vector=np.column_stack((np.zeros(steps),yaxis1))
rudder_input_vector = np.column_stack((np.zeros(steps),yaxis3))

combined_input=np.column_stack((-aileron_input,-rudder_input))

y,T,xout=control.matlab.lsim(sys,combined_input,T,X0=0)

##The updated state space values are derivatives. You have to multiply by time step and integrate
dt=0.1

Beta=0
Phi=0
p=0
r=0
t=0
Beta_tab=[]
Phi_tab=[]
p_tab=[]
r_tab=[]
t_tab=[]
for i in range(len(y[:,0])):
    Beta+=y[:,0][i]*dt
    Phi+=y[:,1][i]*dt
    r+=y[:,2][i]*dt
    p+=y[:,3][i]*dt/((b/2*V0))
    t=t+dt
    t_tab.append(t)
    Beta_tab.append(Beta)
    Phi_tab.append(Phi)
    r_tab.append(r)
    p_tab.append(p)

state_1=np.array(state_1)
state_2=np.array(state_2)
state_3=np.array(state_3)
state_1=state_1-state_1[0]
state_2=state_2-state_2[0]
state_3=state_3-state_3[0]



#####PLOTTING#####
fig=plt.figure()
plt.subplot(211)
plt.plot(T,y[:,0]*(np.pi/180))
plt.xlabel('Time[s]')
plt.ylabel('Beta[rad] (sideslip angle)')
plt.grid()

plt.subplot(212)
plt.plot(T,y[:,1])
plt.plot(time1, state_1)
plt.xlabel('Time[s]')
plt.ylabel('Phi[rad] (roll angle)')
plt.grid()

fig=plt.figure()
plt.subplot(211)
plt.plot(T,y[:,2]*(2*V0/b))
plt.plot(time1, state_2)
plt.xlabel('Time[s]')
plt.ylabel('p [rad/s] (roll rate)')
plt.grid()

plt.subplot(212)
plt.plot(T,y[:,3]*(2*V0/b))
plt.plot(time1, state_3)
plt.xlabel('Time[s]')
plt.ylabel('r [rad/s] (yaw rate)')
plt.grid()

plt.show()