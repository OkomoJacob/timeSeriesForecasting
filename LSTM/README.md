### Time Series Forecasting : Extrapolation
Having known the level of association between the dependent and dependent variables from analysis about the passt, making predictions about the future, also known as `Extrapolation`, but lately refered to as `time series forecasting`. is possible.
This is truest especially in the classical statistical modelling of time series data.

This statistical Modelling involves taking models fit on historical data and using them to predict future observations(Of course based on previous Records)

Descriptive models can borrow for the future (i.e. to smooth or remove noise), they only seek to best describe the data.

### Long Short-Term Memory Network(LSTM-NN)
<hr>

Long Short-Term Memory (LSTM) networks are a type of [Recurrent Neural Network(RNN)](link_here) that are trained using [Back Propagation](link) using data over a long period of time and are capable of learning order dependence in sequence prediction problems.
- Their main advantage is to overcome the problem of `vanishing gradient problem` that was initially seen in old traditional feed-foward ML models.

Having that in mind, LSTM can be `applicable` in complex problem domains e.g 
  * Machine translation
  * Speech recognition
  * High accuracy Weather Forecasting
  * More to achieve `state-of-the-art` results.

#### Minimum basic requirements for a Recurrent Neural Network to Work
The system be able to:
  * Store information for an arbitrary duration.
  * Resist noise (i.e. fluctuations of the inputs that are random or irrelevant to predicting a correct output)
  * Have parameters that are trainable within a reasonable time, not our machine running out of memeory
#### Architecture and operation of LSTM

It's is highly imperative to have an understanding of the overall achiteecture of the LSTM RNN, how the memory blocks are connected through the layers.

Have a look at the architecture [here](img/architectures/architecture.png).

A `block` has components(gates that manage the block's state of either on or off) that make it smarter than a classical neuron.
A block operates upon an input sequence and each gate within a block uses the sigmoid activation units to control whether they are triggered(fired) or not, making the change of state and addition of information flowing through the block conditional.

##### Gates

As discussed briefly aabove,we have three types of gates within a LSTM-RNN unit:

  - [Forget Gate](https): conditionally decides what information to throw away from the block.
  - [Input Gate](https): conditionally decides which values from the input to update the memory state.
  - [Output Gate](htttps): conditionally decides what to output based on input and the memory of the block.