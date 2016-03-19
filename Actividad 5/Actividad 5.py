
# coding: utf-8

# In[34]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Definiendo ecuaciones
def pend(y, t, b, c):
        theta, omega = y
        dydt = (omega, -b*omega - c*np.sin(theta))
        return dydt
    
#Parametros    
b = .2 #fricciòn
g= 9.81 #gravity
l=5 #longitud de la cuerda
c=g/l #frecuencia

#Condiciones iniciales
y0 = [np.pi/4, 1 ]

#Intervalo de tiempo
t = np.linspace(0, 30, 1000)

#solution
sol = odeint(pend, y0, t, args=(b,c))
#gràficas
plt.plot(t, sol[:, 0], 'yo', label='theta(t)')
plt.plot(t, sol[:, 1], 'b', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

