
# coding: utf-8

# In[20]:

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data=np.loadtxt('s24.txt')
x=data[:,0]
y=data[:,1]

def f(x, a, b, c):
    return a * np.exp(-b * x) + c
popt, pcov = curve_fit(f,x,y)
plt.plot(x, y, 'bo', label='Datos')
plt.plot( x, f(x, *popt), 'g-',label='Ajuste')

plt.title("Presion vs altitud")
plt.xlabel("Altitud")
plt.ylabel("Presion")
plt.grid()
plt.legend()
plt.show()


