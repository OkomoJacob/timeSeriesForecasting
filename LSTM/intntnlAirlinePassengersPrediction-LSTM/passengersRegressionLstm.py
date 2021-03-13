"""
STEP 1: Import the necessary libraries,ffunctions and classes
"""
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from matplotlib import pyplot as plt
from keras.layers import Dense
from keras.layers import LSTM
import pandas as pd
import numpy as np
import math

"""
STEP 2: Data preprocessing
"""
# For reproduciblity, fix the random number seed.
np.random.seed(7)

"""
Load the passenger dataset as a dataframe
Extract the NumPy array from the dataframe and convert the integer values to floating point values, 
which are more suitable for modeling with a neural network.
"""

dataframe = pd.read_csv('airline-passengers.csv', usecols=[1], engine='python')
dataset = dataframe.values
dataset = dataset.astype('float32')

# Normalize the data 0-to-1
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)