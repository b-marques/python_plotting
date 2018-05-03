from sklearn import datasets
from matplotlib import pyplot as plt
# %pylab
# %matplotlib inline
import numpy as np
from matplotlib import lines, markers
from cycler import cycler

# Create cycler object. Use any styling from above you please
# monochrome = (cycler('color', ['k']) * cycler('linestyle', ['-', '--', ':', '=.']) * cycler('marker', ['^',',', '.']))

# Print examples of output from cycler object. 
# A cycler object, when called, returns a `iter.cycle` object that iterates over items indefinitely
# print("number of items in monochrome:", len(monochrome))
# for i, item in zip(range(15), monochrome()):
#     print(i, item)

fig, ax = plt.subplots(1,1)

# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(0, 101, 1)
minor_ticks = np.arange(0, 101, 0.5)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)

ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.6, dashes=(4,4))
ax.grid(which='major', alpha=1, dashes=(5,5), linewidth=1.0)

ticklines = ax.get_xticklines() + ax.get_yticklines()
gridlines = ax.get_xgridlines() + ax.get_ygridlines()
ticklabels = ax.get_xticklabels() + ax.get_yticklabels()


bar_cycle = (cycler('hatch', ['///', '--', '...','\///', 'xxx', '\\\\', '+', '.-.']) * cycler('color', 'w')*cycler('zorder', [10]))
styles = bar_cycle()

for x in range(1,10):
    ax.bar(x, np.random.randint(2,10), **next(styles), edgecolor='black',linewidth=2.0)

plt.show()