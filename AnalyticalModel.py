# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:44:45 2019

@author: Miguel Angel Saez
"""
#Import and packages
from math import *
from Cit_par import *

#Short Period Motion
A1 = -2*muc*KY2
B1 = Cmq + Cmadot
C1 = Cma
eigenShortPMa = (-B1+sqrt(4*A1*C1-B1**2))/(2*A1)
eigenShortPMb = (-B1-sqrt(4*A1*C1-B1**2))/(2*A1)

omega0_SPM = V0/B1 * sqrt(C1/A1)
zeta_SPM = -B1/(2*sqrt(A1*C1))

#Phugoid Motion
A2 = 2*muc*(CZa*Cmq - 2*muc*Cma)
B2 = 2*muc*(CXu*Cma - Cmu*CXa) + Cmq*(CZu*CXa-CXu*CZa)
C2 = CZ0*(Cmu*CZa-CZu*Cma)
eigenPhugoidMa = (-B2+sqrt(4*A2*C2-B2**2))/(2*A2)
eigenPhugoidMb = (-B2-sqrt(4*A2*C2-B2**2))/(2*A2)

omega0_PM = V0/B2 * sqrt(C2/A2)
zeta_PM = -B2/(2*sqrt(A2*C2))

#Aperiodic Roll Motion
eigenRollM = (Clp)/(4*mub*KX2)

#Dutch Roll
A4 = -2*mub*KZ2
B4 = 1/2 *Cnr
C4 = -Cnb
eigenDutchRollMa = (-B4+sqrt(4*A4*C4-B4**2))/(2*A4)
eigenDutchRollMb = (-B4-sqrt(4*A4*C4-B4**2))/(2*A4)

omega0_DR = V0/B4 * sqrt(C4/A4)
zeta_DR = -B4/(2*sqrt(A4*C4))

#Spiral Motion
eigenSpiralM = (2*CL *(Clb*Cnr - Cnb*Clr))/(Clb*(CYb*Cnr + 4*mub*Cnb)-Cnp*(CYb*Clr + 4*mub*Clb))



