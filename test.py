import matplotlib.pyplot as plt
import pandas as pd

# Reading in the global temperature data
global_temp = pd.read_csv('datasets/global_temperature.csv')

# Take a look at the first datapoints
# ... YOUR CODE FOR TASK 3 ...
# Plotting global temperature in degrees celsius by year
plt.plot(global_temp['year'], global_temp['degrees_celsiuses_celsius'])

# Adding some nice labels
plt.xlabel('...')
plt.ylabel('...')