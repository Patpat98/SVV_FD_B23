# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:44:45 2019

@author: Miguel Angel Saez
"""
#Import and packages
from math import *

#Short Period Motion
A1 = -2*muc*Ky**2
B1 = Cmq + Cmadot
C1 = Cma
eigenShortPMa = (-B1+sqrt(4*A1*C1-B1**2))/(2*A1)
eigenShortPMb = (-B1-sqrt(4*A1*C1-B1**2))/(2*A1)

