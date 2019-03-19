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


zeta_SPM = (-rootsSP[0].real)/(sqrt((rootsSP[0].real)**2)+(rootsSP[0].imag)**2)
omega_SPM = sqrt(rootsSP[0].real**2 + rootsSP[0].imag**2)
T_halfSPM = (log(1/2) * c)/(rootsSP[0].real * V0)
tau_SPM = -(1*c)/(rootsSP[0].real *V0)


#---------------------   Phugoid Motion   -------------------------------------
A2 = 2*muc*(CZa*Cmq - 2*muc*Cma)#*c/(V0**2)
B2 = 2*muc*(CXu*Cma - Cmu*CXa) + Cmq*(CZu*CXa-CXu*CZa)
#B2 = 2*muc*(CXu*Cma - Cmu*CXa)*c/(V0**2) + Cmq*(CZu*CXa-CXu*CZa)*c/(V0**2)
C2 = CZ0*(Cmu*CZa-CZu*Cma)#*c/V0

coeffPM = [A2, B2, C2]
rootsPM = np.roots(coeffPM)


zeta_PM = (-rootsPM[0].real)/(sqrt((rootsPM[0].real)**2)+(rootsPM[0].imag)**2)
omega_PM = sqrt(rootsPM[0].real**2 + rootsPM[0].imag**2)
T_halfPM = (log(1/2) *c)/(rootsPM[0].real *V0)
tau_PM = -(1*c)/(rootsPM[0].real *V0)

#---------------------   Aperiodic Roll Motion   ------------------------------
eigenRollM = (Clp)/(4*mub*KX2)# *(b/V0))
T_halfRM = (log(1/2) *c)/(eigenRollM *V0)
tau_RM = -(1*c)/(eigenRollM *V0)

#---------------------   Dutch Roll   -----------------------------------------
A4 = -2*mub*KZ2#*b/(2*V0)
B4 = 1/2 *Cnr#*b/(2*V0)
C4 = -Cnb

coeffDR = [A4, B4, C4]
rootsDR = np.roots(coeffDR)


zeta_DR = (-rootsDR[0].real)/(sqrt((rootsDR[0].real)**2)+(rootsDR[0].imag)**2)
omega_DR = sqrt(rootsDR[0].real**2 + rootsDR[0].imag**2)
T_halfDR = (log(1/2) *c)/(rootsDR[0].real *V0)
tau_DR = -(1*c)/(rootsDR[0].real *V0)

#--------------------   Spiral Motion   ---------------------------------------
eigenSpiralM = (2*CL *(Clb*Cnr - Cnb*Clr))/(Clp*(CYb*Cnr + 4*mub*Cnb)-Cnp*(CYb*Clr + 4*mub*Clb))

#eigenSpiralM = (2*CL *(Clb*Cnr - Cnb*Clr))/(Clb*(CYb*Cnr + 4*mub*Cnb)*b/(2*V0) \
                #   -Cnp*(CYb*Clr + 4*mub*Clb)*b/(2*V0))

T_halfSM = -(log(1/2) *c)/(eigenSpiralM *V0)
tau_SM = (1*c)/(eigenSpiralM *V0)




print("---------------------   Short Period Motion:   ------------------------")
print("Eigenvalues:", rootsSP[0], rootsSP[1])
print("omega =", omega_SPM)
print("Damping ratio =", zeta_SPM)
print("T_half =", T_halfSPM)
print("tau = ", tau_SPM)
print()
print("---------------------   Phugoid Motion:   -----------------------------")
print("Eigenvalues:", rootsPM[0], rootsPM[1])
print("omega =", omega_PM)
print("Damping ratio =", zeta_PM)
print("T_half =", T_halfPM)
print("tau = ", tau_PM)
print()
print("---------------------   Aperiodic Roll Motion:   ----------------------")
print("Eigenvalue:", eigenRollM)
print("T_half =", T_halfRM)
print("tau = ", tau_RM)
print()
print("---------------------   Dutch Roll Motion:   --------------------------")
print("Eigenvalues:", rootsDR[0], rootsDR[1])
print("omega =", omega_DR)
print("Damping ratio =", zeta_DR)
print("T_half =", T_halfDR)
print("tau =", tau_DR)
print()
print("---------------------   Spiral Motion:   -----------------------------")
print("Eigenvalue:", eigenSpiralM)
print("T_half =", T_halfSM, "(Actually T_2)")
print("tau =", tau_SM)
