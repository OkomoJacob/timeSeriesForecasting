# Import the necessary libraries,ffunctions and classes
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from matplotlib import pyplot as plt
from keras.layers import Dense
from keras.layers import LSTM
import pandas as pd
import numpy as np
import math

# For reproduciblity, fix the random number seed.
np.random.seed(7)