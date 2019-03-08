# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:44:45 2019

@author: Miguel Angel Saez
"""
#Import and packages
from math import *
from Cit_par import *
import numpy as np

#---------------------   Short Period Motion   --------------------------------
A1 = -2*muc*KY2
B1 = Cmq + Cmadot
C1 = Cma

coeffSP = [A1, B1, C1]
rootsSP = np.roots(coeffSP)

omega0_SPM = V0/B1 * sqrt(C1/A1)
zeta_SPM = -B1/(2*sqrt(A1*C1))


#---------------------   Phugoid Motion   -------------------------------------
A2 = 2*muc*(CZa*Cmq - 2*muc*Cma)
B2 = 2*muc*(CXu*Cma - Cmu*CXa) + Cmq*(CZu*CXa-CXu*CZa)
C2 = CZ0*(Cmu*CZa-CZu*Cma)

coeffPM = [A2, B2, C2]
rootsPM = np.roots(coeffPM)

omega0_PM = V0/B2 * sqrt(C2/A2)
zeta_PM = -B2/(2*sqrt(A2*C2))

#---------------------   Aperiodic Roll Motion   ------------------------------
eigenRollM = (Clp)/(4*mub*KX2)

#---------------------   Dutch Roll   -----------------------------------------
A4 = -2*mub*KZ2
B4 = 1/2 *Cnr
C4 = -Cnb

coeffDR = [A4, B4, C4]
rootsDR = np.roots(coeffDR)

omega0_DR = V0/B4 * sqrt(C4/A4)
zeta_DR = -B4/(2*sqrt(A4*C4))

#--------------------   Spiral Motion   ---------------------------------------
eigenSpiralM = (2*CL *(Clb*Cnr - Cnb*Clr))/(Clb*(CYb*Cnr + 4*mub*Cnb)-Cnp*(CYb*Clr + 4*mub*Clb))





print("---------------------   Short Period Motion:   ------------------------")
print("Eigenvalues:", rootsSP[0], rootsSP[1])
print("omega_0 =", omega0_SPM, "Damping ratio =", zeta_SPM)
print()
print("---------------------   Phugoid Motion:   -----------------------------")
print("Eigenvalues:", rootsPM[0], rootsPM[1])
print("omega_0 =", omega0_PM, "Damping ratio =", zeta_PM)
print()
print("---------------------   Aperiodic Roll Motion:   ----------------------")
print("Eigenvalue:", eigenRollM)
#print("omega_0 =", omega0_SP, "Damping ratio =", zeta_SPM)
print()
print("---------------------   Dutch Roll Motion:   --------------------------")
print("Eigenvalues:", rootsDR[0], rootsDR[1])
print("omega_0 =", omega0_DR, "Damping ratio =", zeta_DR)
print()
print("---------------------   Spiral Motion:   ------------------------------")
print("Eigenvalue:", eigenSpiralM)
#print("omega_0 =", omega0_SP, "Damping ratio =", zeta_SPM)
