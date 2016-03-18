
# coding: utf-8

# In[1]:

f1,f2 = 1,1
while f2<1000:
      print(f2)
      f1,f2 = f2,f1+f2


# In[2]:

n,C1,C2 = 0,1,1
while(C2 < 1000000): 
    print(C2)
    C2= C1*(4*n+2)/(n+2)
    n=n+1
    C1=C2

