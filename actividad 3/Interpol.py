
# coding: utf-8

# In[27]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

xa=np.random.random(10)
x0 = xa*3
y0 = np.sin(2*x0)

plt.plot(x0, y0, 'o', label='Data')

x = np.linspace(min(x0),max(x0),101)

# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)   
    plt.plot(x, f(x), label=o)      
plt.legend()
plt.show()


# In[35]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

xa = np.random.random(20)
x0= (xa-(1/2))*20
y0 = np.sin(x0)/x0

plt.plot(x0, y0, 'o', label='Data')

x=np.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    
    plt.plot(x, f(x), label=o)     
plt.legend()
plt.show()


# In[37]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

xa = np.random.random(16)
x0= (xa-(1/2))*6
y0 = (x0**2)*np.sin(2*x0)

plt.plot(x0, y0, 'o', label='Data')

x=np.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    
    plt.plot(x, f(x), label=o)     
plt.legend()
plt.show()


# In[39]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

xa = np.random.random(12)
x0= (xa-(1/2))*4
y0 = (x0**3)*np.sin(x0*3)

plt.plot(x0, y0, 'o', label='Data')

x=np.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    
    plt.plot(x, f(x), label=o)     
plt.legend()
plt.show()

