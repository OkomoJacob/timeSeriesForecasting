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
LSTMs are sensitive to the scale of the input data especially if it , specifically when the sigmoid (default) or tanh activation functions are used. It can be a good practice to rescale the data to the range of 0-to-1, also called normalizing. We can easily normalize the dataset using the MinMaxScaler preprocessing class from the scikit-learn library.