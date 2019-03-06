import sympy as sp
sp.var('C1 C2 C3 c V0 muc KY2 CXu CX0 CXa CXq CXde CXadot CZu CZ0 CZa CZq CZde CZadot Cmu Cmadot Cmq Cmde Cma')
C1=sp.Matrix([[-2*muc*c/(V0**2),0,0,0],[0,(CZadot-2*muc)*c/V0]])
C2=sp.Matrix([[a,b],[c,s]])
C3=sp.Matrix([[a,b],[c,s]])