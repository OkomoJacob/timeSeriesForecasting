## Time Series Forecasting : Extrapolation

![Twitter Follow](https://img.shields.io/twitter/follow/okomojacob?style=social)

Having known the level of association between the dependent and independent variables from analysis about the past, making predictions about the future, also known as `Extrapolation`, but lately refered to as `time series forecasting`. is possible.
This is truest especially in the classical statistical modelling of time series data.

This statistical Modelling involves taking models fit on historical data and using them to predict future observations(Of course based on previous Records)

Descriptive models can borrow for the future (i.e. to smooth or remove noise), they only seek to best describe the data.

### Long Short-Term Memory Network(LSTM-NN)
<hr>

Long Short-Term Memory (LSTM) networks are a type of [Recurrent Neural Network(RNN)](https://d1wqtxts1xzle7.cloudfront.net/31279335/___Recurrent_Neural_Networks_Design_And_Applicatio%28BookFi.org%29.pdf?1369075425=&response-content-disposition=inline%3B+filename%3DEffects_of_Liquid_and_Encapsulated_Lacti.pdf&Expires=1615627088&Signature=XHX~PcZuSaHUyIwCRus-hC4jb8DXlqU8u5wGEBHs9qyv4KOPu1fU4MugZ1R1eA-G1E~KFwWzYb1DfJk~np~VYpxYWD1lChkiKw8HPvqucha7RaGr6MLCvCBPFlNLeOd6zKowqtNT15Nom~YbV4DEKXCSPs3hLxnzADFZ6mUSqYNTvyQFs5ijkvqBRU76j6lwVzpIa9YX8HBSj4UD-vz63mK2IC-Ks-qNvzQx6fnlwAoURr2JoC~dUVkAHjo8nV1ZcKvnr3kXJJvNdtF~roaYycDqnb26gC-SCh8016Ce0CMuTwTJJiy2whFGlfxy6rBgQ7PKN9EmCHsUpSDAFK5TNg__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) that are trained using [Back Propagation](https://www.sciencedirect.com/science/article/pii/B9780127412528500108) using data over a long period of time and are capable of learning order dependence in sequence prediction problems.
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

  - [Forget Gate](https://colah.github.io/posts/2015-08-Understanding-LSTMs/): conditionally decides what information to throw away from the block.
  - [Input Gate](https://colah.github.io/posts/2015-08-Understanding-LSTMs/): conditionally decides which values from the input to update the memory state.
  - [Output Gate](https://colah.github.io/posts/2015-08-Understanding-LSTMs/): conditionally decides what to output based on input and the memory of the block.
  
#### Built With
  - [Comma Seperated Value Data](https://www.bigcommerce.com/ecommerce-answers/what-csv-file-and-what-does-it-mean-my-ecommerce-business/)
  - [Pandas](https://pandas.pydata.org/docs/)
  - [Matplotlib](https://matplotlib.org/stable/faq/howto_faq.html)
  - [keras](https://keras.io/)
  - [Scikit-learn](https://scikit-learn.org/stable/)
  - [Tensorflow](https://www.tensorflow.org/api_docs)
  - [Numpy](https://numpy.org/doc/)
  
#### Errata

Although I have taken every care to ensure the accuracy my my content, mistakes
do happen. If you find a mistake in this project—maybe a mistake in the text or
the code—I would be grateful if you could report this to me via [mail](jaylabs2030@gmail.com) or via visiting my official [website](https://okomojacob.herokuapp.com). By doing so, you can
save others from frustration and help me improve subsequent versions of this mini-project and related works. 

#### Getting Further Help
One of the greatest benefits of `keras`, `python` and `deeplearning` is its great kind and helpful user community and heavy documentation.
For help with any aspect of related to the above mentioned and related - from installation, to application design,to deployment - feel free to ask questions online in the appended links.

• [The python official website](http://www.python.org)
• [Keras official Documentation](https://keras.io/)
• [scikit-learn](https://scikit-learn.org/stable/)
