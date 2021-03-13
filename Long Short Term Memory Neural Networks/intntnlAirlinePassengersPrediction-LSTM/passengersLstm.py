# Import all the required python libraries
from matplotlib import pyplot as plt
import pandas as pd
import os

# Load the data, from the local dir
data = pd.read_csv('data/oldPassengers.csv', usecols=[1], engine='python')
plt.plot(data)
plt.title("A Raw plot of our Data")
plt.show()
