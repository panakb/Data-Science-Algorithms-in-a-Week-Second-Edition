import sys
sys.path.append('../../common')  # noqa
import common
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
matplotlib.style.use('ggplot')

if len(sys.argv) < 2:
    sys.exit('Please, input as arguments:\n' +
             '1. the generated pgm image name,\n' +
             '2. the full pgm image name,\n' +
             'Example usage:\n' +
             'python italy_draw_graph.py ' +
             'italy_100completed_3.pgm ' +
             'italy.pgm')
generated_name = sys.argv[1]
full_name = sys.argv[2]

# generated_data = np.loadtxt(open(generated_name, 'r'),skiprows=3)
generated_data = pd.read_csv(generated_name, sep=" ", header=None, skiprows=3)

full_data = pd.read_csv(full_name, sep=" ", header=None, skiprows=3)

rows = generated_data.shape[0]
collumns = generated_data.shape[1]

for x in range(0, rows):
    for y in range(0, collumns):
        if generated_data[x][y] == full_data[x][y]:
            generated_data[x][y] = lambda x: 'blue' if x == 1 else 'green'
        else:
            generated_data[x][y] = 'red'
# Convert the array into the format ready for drawing functions.
# data_processed = common.get_x_y_colors(generated_data)


# Draw the graph.
plt.title('Mary and temperature preferences')
plt.xlabel('temperature in C')
plt.ylabel('wind speed in kmph')
plt.axis([0, rows, 0, collumns])
# Add legends to the graph.
blue_patch = mpatches.Patch(color='blue', label='cold')
red_patch = mpatches.Patch(color='red', label='warm')
plt.legend(handles=[blue_patch, red_patch])
plt.scatter(generated_data,
            c=generated_data.values) # , s=[1400] * len(data))
plt.show()
