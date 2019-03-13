#from sympy import *
from Cit_par import *
import numpy as np
import control
#var('C1 C2 C3 c V0 muc KY2 CXu CX0 CXa CXq CXde CXadot CZu CZ0 CZa CZq CZde CZadot Cmu Cmadot Cmq Cmde Cma')
C1=np.matrix([[-2*muc*c/(V0**2),0,0,0],[0,(CZadot-2*muc)*c/V0, 0, 0],[0,0,-c/V0,0],[0,Cmadot*c/V0,0,-2*muc*KY2*c**2/(V0**2)]])
C2=np.matrix([[CXu/V0,CXa, CZ0, CXq*c/V0],[CZu/V0,CZa, -CX0, (CZq+2*muc)*c/V0],[0,0,0,c/V0],[Cmu/V0, Cma, 0, Cmq*c/V0]])
C3=np.matrix([[CXde],[CZde],[0],[Cmde]])
C1_inv= np.linalg.inv(C1)
#A= -C1_inv.multiply(C2)
#B= -C1_inv.multiply(C3)
A1=np.matmul(-C1_inv, C2)
B1=np.matmul(-C1_inv, C3)
print(np.linalg.eig(A1))

C=np.matrix([1,0,0,0])
D=np.matrix([0])

sys=StateSpace(A1,B1,C,D)

T=np.arange(0,10,0.1)

T,y=step_response(sys,T,X0=0.0)

#Plot the step reponse
plt.plot(T,y)
plt.show()



