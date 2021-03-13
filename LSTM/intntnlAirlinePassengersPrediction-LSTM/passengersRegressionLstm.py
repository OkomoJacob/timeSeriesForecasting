"""
STEP 1: Import the necessary libraries,ffunctions and classes
"""
# from sklearn.model_selection import train_test_split
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

df = pd.read_csv('data/oldPassengers.csv', usecols=[1], engine='python')
dataset = df.values
dataset = dataset.astype('float32')

"""
plt.plot(data)
plt.title("A Raw plot of our Data")
plt.show()
"""

# Normalize the data 0-to-1
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# split into train and test sets
train_size = int(len(dataset) * 0.70)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))
"""
SPET 3: Convert an array of values into a dataset matrix
"""
def createDataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX), np.array(dataY)

"""
STEP 4: Prepare the train and test datasets for modeling
"""

# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = createDataset(train, look_back)
testX, testY = createDataset(test, look_back)

# Further reshape, by appending timestamps to our dataset
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

"""
STEP 5: Create and fit the LSTM network
"""
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

"""
STEP 6: Make predictions
"""

trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

# calculate root mean squared error(MSE)
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

"""
STEP 7: Generate Predictions
"""
# shift train predictions for plotting
trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
# shift test predictions for plotting
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()