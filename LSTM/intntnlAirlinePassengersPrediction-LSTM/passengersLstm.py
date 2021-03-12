# Import the required libraries
from matplotlib import pyplot as plt
import pandas as pd
import os

print(os.getcwd())
data = os.path.join('data/', 'myPassengers.csv')
dataset = pd.read_csv(data, usecols=[1], engine='python')
plt.plot(data)
plt.show()
