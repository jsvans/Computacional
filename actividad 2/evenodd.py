
# coding: utf-8

# In[4]:

n = int(input("Enter an integer: "))
if n%2==0:
     print("even")
else:
     print("odd")
        


# In[5]:

print("Enter two integers, one even, one odd.")
m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))
while (m+n)%2==0:
    print("One must be even and the other odd.")
    m = int(input("Enter the first integer: "))
    n = int(input("Enter the second integer: "))
print("The numbers you chose are",m,"and",n)

