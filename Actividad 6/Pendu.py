
# coding: utf-8

# In[20]:

#Biblos
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#Constantes

g=9.81 
l= 3  
n= 50
e=0.001 
T0 =np.linspace(e, (np.pi)-e, n)

#Integrales
I = [0 for i in range(n)]
E = [0 for i in range(n)]
T = [0 for i in range(n)]
To = 2.0 * np.pi*np.sqrt(l/g)

#Integrando
inte = lambda x, c : 1.0 /(np.sqrt(np.cos(x)-np.cos(c)))

for i in range(n):
    
    T1 = T0[i]
    I[i] , E [i] = quad(inte, 0, T1, args=(T1))
    T[i] = 4*np.sqrt(l/(2*g)) * I[i]
       
R=T/To

Tg= (T0*180.0)/np.pi 

#Graph
plt.plot(Tg, R, "go")
plt.grid()
plt.title("Error ")
plt.xlabel("Angulo")
plt.ylabel("Razon entre periodos")
plt.axis([0,180,1,5])
plt.show()

