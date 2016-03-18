
# coding: utf-8

# In[8]:

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

datos=np.loadtxt('s48.txt')
x=datos[:,0]
y=datos[:,1]

fitfunc = lambda p, x: p[0]*x + p[1]
errfunc = lambda p, x, y: fitfunc(p, x) - y 
p0=[1,1]
p1, success=optimize.leastsq(errfunc, p0[:], args=(x,y))

time = np.linspace(x.min(), x.max(), 100)
plt.plot(x, y, "go", label="Datos") 
plt.plot(time, fitfunc(p1, time), "b-", label="Ajuste ineal")

plt.title("Temperatura del invierno en Nueva York (1990-1999)")
plt.xlabel("Año")
plt.ylabel("Temperatura")
plt.grid()
plt.legend()
plt.show()

