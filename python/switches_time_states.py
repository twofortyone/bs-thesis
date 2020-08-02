import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
t = np.arange(5, 16)
data1 = np.array([7.3,8.4,11, 15.5, 17.7, 41.3, 72.5, 145, 290.3, 602.4, 1198.2])
data2 = np.array([3744,7588,14976,29952, 59904, 119808,239616,479232,958464,1916928,3833856])

fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel('No. of switches')
ax1.set_ylabel('Time [min]', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('No. of states', color=color)  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
fig.tight_layout()  # otherwise the right y-label is slightly clipped
#ax1.grid(which='both',axis='both',linestyle='-', linewidth=0.5)
#ax2.grid(axis='y',linestyle='-', linewidth=1)
plt.show()