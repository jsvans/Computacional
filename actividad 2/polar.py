
# coding: utf-8

# In[3]:

from math import pi,atan,acos
x=float(input("Introduce x:"))
y=float(input("introduce y:"))
z=float(input("introduce z:"))
r= (x**2+y**2+z**2)**(1/2)
theta= atan(y/x)
phi= acos(z/r)
a=theta*180/pi
b=phi*180/pi
print("r=",r ,"theta=",a ,"phi=",b, )

