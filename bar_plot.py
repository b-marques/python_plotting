from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

## CONFIGS: ##
# Turn grid on
plt.rcParams['axes.grid'] = True
# Put grid to background
plt.rcParams['axes.axisbelow'] = True
# Grid lines configs
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.color'] = '6d6d6d'
plt.rcParams['grid.linewidth'] = 0.2
plt.rcParams['lines.dashed_pattern'] = [10, 20]
# Configure bar plot
BAR_linewidth = 1 # set to 0 to remove edge
BAR_color = 'white'
BAR_edgecolor = 'black'
plt.rcParams['hatch.linewidth'] = 0.01
# Configure ticks
plt.rcParams['xtick.top'] = True
plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 1.5
plt.rcParams['ytick.left'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 1.5
# Labels
FONT_SIZE = 26
plt.rcParams['ytick.labelsize'] = FONT_SIZE
plt.rcParams['ytick.major.pad'] = 20
plt.rcParams['xtick.labelsize'] = FONT_SIZE
plt.rcParams['xtick.major.pad'] = 20
plt.rcParams['axes.labelsize'] = FONT_SIZE
plt.rcParams['axes.labelpad'] = 15
plt.rcParams['axes.linewidth'] = 2
# Legends
plt.rcParams['legend.fontsize'] = FONT_SIZE -1
plt.rcParams['legend.labelspacing'] = .01
plt.rcParams['legend.fancybox'] = False
plt.rcParams['legend.edgecolor'] = 'black'

patterns = [ "///" , " " , "/\\/\\" , "\\" , "+" , "x", "o", "O", ".", "*" ]

raw_data = {
            'application': ['Convolution', 'GoL', 'Jacobi'],
            'MPPA-256': [100, 100, 60],
            'Xeon E5': [600, 480, 480],
            'Tesla K40': [450, 400, 250]
           }
df = pd.DataFrame(raw_data, columns = ['application', 'MPPA-256', 'Xeon E5', 'Tesla K40'])

# Setting the positions and width for the bars
pos = list(range(len(df[df.columns[1]]))) 
width = 0.2 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(10,8))

# Create a bar for each application data,
# in position pos,
for i in range(1, len(df.columns)):
  plt.bar([p + width*i for p in pos], 
          #using df['application'] data,
          df[df.columns[i]], 
          # of width
          width, 
          # with color
          color = BAR_color,
          #pattern,
          hatch=patterns[i],
          # edge color 
          edgecolor = BAR_edgecolor,
          # with label the first value in first_name
          label=df['application'][i-1])

# Set the y axis label
ax.set_ylabel('Energy (J)')

# Set the chart's title
# ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 2 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['application'])

# Setting the x-axis and y-axis limits
# plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, 700] )

# Adding the legend and showing the plot
plt.legend([x for x in df.columns if x != 'application'] , loc='upper right')

# for i in range(len(y)):
#   plt.bar(x[i], 
#           y[i],
#           color=BAR_color,
#           edgecolor=BAR_edgecolor,
#           linewidth=BAR_linewidth,
#           hatch=patterns[i])

plt.tight_layout()
plt.savefig("fig.pdf")
