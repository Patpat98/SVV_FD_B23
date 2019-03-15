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
A1 = -2*muc*KY2#*c/V0
B1 = Cmadot + Cmq#*c/V0 
C1 = Cma

coeffSP = [A1, B1, C1]
rootsSP = np.roots(coeffSP)

#omega0_SPM = (V0/B1) * sqrt(C1/A1)
#zeta_SPM = -B1/(2*sqrt(A1*C1))
zeta_newSPM = (-rootsSP[0].real)/(sqrt((rootsSP[0].real)**2)+(rootsSP[0].imag)**2)
omega0_newSPM = (rootsSP[0].imag)/(sqrt(1-rootsSP[0].real))
T_halfSPM = (0.693)/(rootsSP[0].real)


#---------------------   Phugoid Motion   -------------------------------------
A2 = 2*muc*(CZa*Cmq - 2*muc*Cma)#*c/(V0**2)
B2 = 2*muc*(CXu*Cma - Cmu*CXa) + Cmq*(CZu*CXa-CXu*CZa)
#B2 = 2*muc*(CXu*Cma - Cmu*CXa)*c/(V0**2) + Cmq*(CZu*CXa-CXu*CZa)*c/(V0**2)
C2 = CZ0*(Cmu*CZa-CZu*Cma)#*c/V0

coeffPM = [A2, B2, C2]
rootsPM = np.roots(coeffPM)

#omega0_PM = V0/B2 * sqrt(C2/A2)
#zeta_PM = -B2/(2*sqrt(A2*C2))
zeta_newPM = (-rootsPM[0].real)/(sqrt((rootsPM[0].real)**2)+(rootsPM[0].imag)**2)
omega0_newPM = (rootsPM[0].imag)/(sqrt(1-rootsPM[0].real))
T_halfPM = -(0.693)/(rootsPM[0].real)

#---------------------   Aperiodic Roll Motion   ------------------------------
eigenRollM = (Clp)/(4*mub*KX2)# *(b/V0))


#---------------------   Dutch Roll   -----------------------------------------
A4 = -2*mub*KZ2#*b/(2*V0)
B4 = 1/2 *Cnr#*b/(2*V0)
C4 = -Cnb

coeffDR = [A4, B4, C4]
rootsDR = np.roots(coeffDR)

#omega0_DR = V0/B4 * sqrt(C4/A4)
#zeta_DR = -B4/(2*sqrt(A4*C4))
zeta_newDR = (-rootsDR[0].real)/(sqrt((rootsDR[0].real)**2)+(rootsDR[0].imag)**2)
omega0_newDR = (rootsDR[0].imag)/(sqrt(1-rootsDR[0].real))
T_halfDR = -(0.693)/(rootsDR[0].real)

#--------------------   Spiral Motion   ---------------------------------------
eigenSpiralM = (2*CL *(Clb*Cnr - Cnb*Clr))/(Clp*(CYb*Cnr + 4*mub*Cnb)-Cnp*(CYb*Clr + 4*mub*Clb))

e#igenSpiralM = (2*CL *(Clb*Cnr - Cnb*Clr))/(Clb*(CYb*Cnr + 4*mub*Cnb)*b/(2*V0) \
                #   -Cnp*(CYb*Clr + 4*mub*Clb)*b/(2*V0))






print("---------------------   Short Period Motion:   ------------------------")
print("Eigenvalues:", rootsSP[0], rootsSP[1])
print("omega_0new =", omega0_newSPM)
print("Damping ratio new =", zeta_newSPM)
print("T_half =", T_halfSPM, "(that's actually T_2)")
print()
print("---------------------   Phugoid Motion:   -----------------------------")
print("Eigenvalues:", rootsPM[0], rootsPM[1])
print("omega_0new =", omega0_newPM)
print("Damping ratio new =", zeta_newPM)
print("T_half =", T_halfPM)
print()
print("---------------------   Aperiodic Roll Motion:   ----------------------")
print("Eigenvalue:", eigenRollM)
print()
print("---------------------   Dutch Roll Motion:   --------------------------")
print("Eigenvalues:", rootsDR[0], rootsDR[1])
print("omega_0new =", omega0_newDR)
print("Damping ratio new =", zeta_newDR)
print("T_half =", T_halfDR)
print()
print("---------------------   Spiral Motion:   -----------------------------")
print("Eigenvalue:", eigenSpiralM)

#print("omega_0 =", omega0_SP, "Damping ratio =", zeta_SPM)
