from sympy import *
var('C1 C2 C3 c V0 muc KY2 CXu CX0 CXa CXq CXde CXadot CZu CZ0 CZa CZq CZde CZadot Cmu Cmadot Cmq Cmde Cma')
C1=Matrix([[-2*muc*c/(V0**2),0,0,0],[0,(CZadot-2*muc)*c/V0, 0, 0],[0,0,-c/V0,0],[0,Cmadot*c/V0,0,-2*muc*KY2*c**2/(V0**2)]])
C2=Matrix([[CXu/V0,CXa, CZ0, CXq*c/V0],[CZu/V0,CZa, -CX0, (CZq+2*muc)*c/V0],[0,0,0,c/V0],[Cmu/V0, Cma, 0, Cmq*c/V0]])
C3=Matrix([[CXde],[CZde],[0],[Cmde]])
C1_inv= C1.inv()
A= -C1_inv.multiply(C2)
B= -C1_inv.multiply(C3)