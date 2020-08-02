import numpy as np 
from sys import getsizeof

l = np.ones(10)*117
s = np.arange(10,20)
states = 2**s*l
sizes = []
for i in range(10):
    z = np.ones((int(states[i]),int(s[i])))
    sizes.append(getsizeof(z))

sizes = np.asarray(sizes)