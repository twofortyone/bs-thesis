import pandas as pd 
import numpy as np
from tqdm import trange
import matplotlib.pylab as plt
lineas = pd.read_excel('./lines.xlsx')
lineas_np = lineas.to_numpy()

switches = pd.read_excel('./switches.xlsx')
switches_np = switches.to_numpy()

plt.figure()
plt.plot(lineas_np[:,0], lineas_np[:,1])
plt.ylabel('Memory required [GB]')
plt.xlabel('Number of lines')
plt.show

plt.figure()
plt.plot(switches_np[:-4,0], switches_np[:-4,1])
plt.ylabel('Memory required [GB]')
plt.xlabel('Number of switches')
plt.show