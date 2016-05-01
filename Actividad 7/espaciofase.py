
# coding: utf-8

# In[45]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pend(y, t, b, c):
        theta, omega = y
        dydt = (omega, -b*omega - c*np.sin(theta))
        return dydt
        
b = 0           
g= 9.8           
l=1              
c=g/l
t = np.linspace(0.0,20,500)  

X_f1 =np.array([-90.0*np.pi,20])
X_f2 =np.array([-2.0*np.pi,0.0]) 


values1 =np.linspace(-1,1,45)                
values2 =np.linspace(-1,1,90)                
vcolors1 = plt.cm.flag(np.linspace(.7, .2, len(values1))) 
vcolors2 = plt.cm.gist_ncar(np.linspace(0.4, 0.8, len(values2)))  

plt.figure(2)


#Trayectorias de arriba
for v1, col1 in zip(values1, vcolors1):
    y1 = v1 * X_f1                                
    x1 = odeint(pend, y1, t, args=(b,c))         
    plt.plot( x1[:,0], x1[:,1], lw=1.5*v1, color=col1 )

#Trayectorias del centro                             
for v2, col2 in zip(values2, vcolors2):
    y2 = v2 * X_f2                                 
    x2 = odeint(pend, y2, t, args=(b,c))           
    plt.plot( x2[:,0], x2[:,1], lw=1.5*v2, color=col2 )


#Para graficar
plt.title('Espacio Fase')
plt.xlabel('Angulo')
plt.ylabel('Velocidad Angular')
plt.grid()
plt.xlim(-3.0*np.pi,3.0*np.pi)
plt.ylim(-15,15)


plt.show()

