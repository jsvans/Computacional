
# coding: utf-8

# In[4]:

from math import pi
M=5.97e24
G=6.67e-11
R=6371e3
T=float(input("Ingrese el valor del periodo del satélite en minutos:"))
h=((G*M*((T*60)**2)*4*pi**2)**(1/3))+R
print("La altitud del satélite es de ",h,"metros")

