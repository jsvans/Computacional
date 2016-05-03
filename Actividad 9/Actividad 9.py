
# coding: utf-8

# In[3]:


from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt


g=9.8        
l=2  


T0=2*np.pi*np.sqrt(l/g)
n=1000
e=0.0001
theta0=np.linspace(e,(np.pi)+e,n) 


#Definiendo arreglos para resultados arrojados
S=[0 for i in range(n)]
TT=[0 for i in range(n)]
R=[0 for i in range(n)]
T=[0 for i in range(n)]
real0=[0 for i in range(n)]
real2=[0 for i in range(n)]
real4=[0 for i in range(n)]
real6=[0 for i in range(n)]
real8=[0 for i in range(n)]

#------------------------------------------
#Creando doble loop para considerar los casos
#donde se agregan mas terminos de la serie de potencias


M0=0

#Comenzando un loop para poder calcular todos los resultados 
#posibles contemplando un angulo inicial variante
for i in range(M0):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real0[j]=(T[j]/T0)
#------------------------------------------        
M2=2
for i in range(M2):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real2[j]=(T[j]/T0)-1
#------------------------------------------        
M4=4
for i in range(M4):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real4[j]=(T[j]/T0)-2
#------------------------------------------
M6=6
for i in range(M6):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real6[j]=(T[j]/T0)-3
#------------------------------------------
M8=8
for i in range(M8):
    for j in range(0,n):
        F1=float(math.factorial(2*i))
        F2=float(((2**i)*(math.factorial(i)))**2)
        
        S[j]=np.sin(theta0[j]/2)**(2*i)
        TT[j]=((F1/F2)**2)*(S[j])
        R[j]=TT[j]+R[j]
        T[j]=R[j]*T0
        real8[j]=(T[j]/T0)-4

#Gráfica
plt.plot(theta0, real0, 'b',linewidth=2, label="T0")
plt.plot(theta0, real2, 'g',linewidth=2, label="T2")
plt.plot(theta0, real4, 'r',linewidth=2, label="T4")
plt.plot(theta0, real6, 'm',linewidth=2, label="T6")
plt.plot(theta0, real8, 'c',linewidth=2, label="T8")
plt.title('Error utilizando series de potencia')
plt.grid()
plt.xlabel('Angulo')
plt.xlim(0,np.pi)
plt.ylim(0,1)
plt.ylabel('Error')
plt.legend(loc='best')


fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.5,5.5)
fig.savefig('error.png',dpi=100)

