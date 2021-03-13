### Problem Statement and Solution in LSTM with Keras and Tensorflow
<hr>

As seen in in the folder name, the problem we are going to look at in this post is the International Airline Passengers prediction problem.
- For 12 year from January 1949, flight data was collected from a good number of Flight Terminals globally (Airports) till December 1960.

The data is in CSV format and with only 2 columns, i.e `Month`, `number of passengers` and 144 rows

#### Execution
since we're not interested in the dates, we load the dataset excluding the first column.

#### Built With
Please refer to the `requirements.txt` file in this repo for more.
In a nutshell:
  - data.csv
  - pandas
  - matplotlib
  - keras
  - tensorflow
  - numpy

in your terminal or command line, run `pip3 install -r requirements.txt`.
- This will tell pip3 or pip to read and install the contents of the .txt file

#### Code Explanation
1.`Import the NN required Libraries, functions and classes`
2.`Prepare the data for pandas dataframe and reshape it as foat 32`
3.`Rescale the data(Normalize it) from 0 to 1`
  * LSTMs are sensitive to the scale of the input data especially if it , specifically when the sigmoid activation function (default) or tanh activation functions are used. 
  * We thus rescale the data to the range of 0-to-1, also called normalizing using the `MinMaxScaler` preprocessing class from the `scikit-learn` library.

4.`Split the data into train and test`
  * For a normal classification or regression problem, we would use cross validation, however for time series data, the sequence of values is important. A simple method that we can use is to split the ordered dataset into train and test datasets.
  * Use about 70% for train and 30% for test using the 

5. `Define a function to create a new dataset`
  * The function takes two arguments: the `dataset`, which is a NumPy array that we want to convert into a dataset, and the `look_back`, which is the number of previous time steps to use as input variables to predict the next time period — in this case defaulted to 1.

6. Reshape the data in the form of `samples, time steps, features`
  * The LSTM network expects the input data (X) to be provided with a specific array structure in the above specified form.

7.  `Create and Fit the model` with the necessary training parameters, [epochs](https://deepai.org/machine-learning-glossary-and-terms/epoch) and [verbose](http://discuss.codingblocks.com/t/verbosity-mode-in-keras-callbacks/20529/2).
8.  