## Global Warming and Climate Change Prediction using Time Series Analysis
<hr>

<img align="left" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"><br>
![GitHub repo size](https://img.shields.io/github/repo-size/okomojacob/8d19d988d6f?color=green-yellow&logo=github&logoColor=blue) ![GitHub language count](https://img.shields.io/github/languages/count/OkomoJacob/8d19d988d6f?logo=visual-studio-code) ![GitHub last commit](https://img.shields.io/github/last-commit/OkomoJacob/8d19d988d6f?style=plastic&color=brightgreen) 
![Forks](https://img.shields.io/github/forks/OkomoJacob/8d19d988d6f?style=social) ![APM](https://img.shields.io/apm/dm/vim-mode) ![shields](https://img.shields.io/opencollective/sponsors/0) ![Hackage-Deps](https://img.shields.io/hackage-deps/v/lens) ![GitHub top language](https://img.shields.io/github/languages/top/okomojacob/8d19d988d6f)

#### Find Me on Twitter

### Contents:
- What is Time Series Data and Time Series Analysis
- Time Series Use Cases
- Tools and Requirements

#### Usage

-To succesfully use this project, run `pip3 install -r requirements.txt` to install the needed packages.Then start [jupyter-notebook](link) to launch the `timeSeries.ipynb` notebook to explore.
- You can as well open the `resultImgs` folder to see the expected outputs.
#### Time Series Data and Time Series Analysis
[Time Series(Time Stamped) Data](https://www.investopedia.com/terms/t/timeseries.asp) can be seen as temporal data, i.e that collected over time at fixed intervals repeatedly.

[Time Series Analysis](link) Is the Statistical Act/Technique of collecting of Time Series Data and Trends and Anlyssing them.Purposely for [Monitoring of Nature of the Pheenomena](link) to aid in the [Forecasting](link) of measurable outcomes by extrapolating in time.
### Built With
[Python3](https) : Easy to Learn and Use, easy to maintain
[Data, CSV](https) : 
[Pandas](link)
[Numpy](link) for numerical operation
[Matplotlib](link) for interactive charts and dates, plots
[Datetime](link) supplies Classes to work with dates and times and time intervals.
[Statsmodels](https) Distinguishable patterns, e.g Seasonality, trends and noise.
[Statstools](https) for [Seasonal Decomposition](link)

### Steps in this Deep Learning Prediction
1. [Data Preparation](link)
2. [Data Analysis and Visualization](link) :Trend and Stationality
3. [Test Stationary](link)
   - Use [Dicky Fuller Test](link) to Test for The hypothesis.
   - `Assumptions made for Any Stationary Time Series:`
     - The `Mean of the Series` should not be a Function of Time, but should be `Constant`
     - The `Variance of the Series` should not be a Function of Time, but should be `Constant`
     - The `Covariance` of the `ith` and the `i+nth term of the Series` should not be a Function of Time, but should be `Constant`
4. [Data Transformation](link) : Employs tecchniques e.g [Moving Average](link), [Exponential smoothing](link)
   -Done to `make the Data Stationary` 
5. [Review With SARIMA with ACF and PACF](link) :AutoRegressive Ingtegrated Moving Average([ARIMA](link))
    - How to find the [Autoregressive(p)](link), [Integrated(d)](link) and [Moving Averages(q)](link)
### Time Series Analysis Use Cases
- Financial Analysis : Sales Forecasting, Inentory Analysis, Stock Prediction, Price Estimation, Momentum, etc
- Weather Forecastion(Analysis): Temp change analysis, Global Climate Change, Seasonal Shift Recognition,
- Health Care Analysis : Network Usage Prediction,Predictive Maintanance, Intrusion Detection etc.
- Network Data Analysis :Senses Prediction, Insurance benefit analysis

It is an unmaskable fact that, lately, there has been a negative trend in the rate of Global Average Temp.This is negatively impacting the gloabl population as most(if not all) depend directly on the climate.
##### Negative impacts include but are not limited to:
    - Melting of ICE and Snows
    - Rising of the Sea Levels

#### Importance of Stationarity in Time Series Analysis
 Since Time Series assumes that each data point is independent from each other, and that statistical pperties of the data should not cchange over time, stationariy help us better understand and thus identify the Driving Parameters, to ensure consistence in correlation.

### Data Overview

Date: starts in 1743 for average land temperature.
By 1850 , there were provisions for max and min land temperatures and global ocean and land temperatures
LandAverageTemperatureUncertainty: the 95% confidence interval around the average
LandMaxTemperature: global average maximum land temperature in celsius
LandMaxTemperatureUncertainty: the 95% confidence interval around the maximum land temperature
LandMinTemperature: global average minimum land temperature in celsius
LandMinTemperatureUncertainty: the 95% confidence interval around the minimum land temperature
LandAndOceanAverageTemperature: global average land and ocean temperature in celsius
LandAndOceanAverageTemperatureUncertainty: the 95% confidence interval around the global average land and ocean temperature.

Global Average Land Temperature by State (GlobalLandTemperaturesByState.csv)
### Find Raw Data at :
[Berkeley Earth data page](linkhere).


#### Errata.
<hr>

Although we have taken every care to ensure the accuracy of our content, mistakes
do happen. If you find a mistake in this project—maybe a mistake in the text or
the code—We would be grateful if you could report this to us via [Jacob Okomo](https://okomojacob.herokuapp.com) or [Christine Joy](https://github.com/JoyChristine) By doing so, you can
save others from frustration and help me improve subsequent versions of this mini-project and related works. 

#### Credits and Acknowledgements
<hr>

Hitherto, we give sincere credits to [Jacob Okomo](https://okomojacob.herokuapp.com), and [Christine Joy](https://github.com/JoyChristine) who has since been committing to this project.
-Thank you

##### Progress Report
-Merge Joy's work(Search bar) <br>
-Scroll to top working on Elijah's, merge to main from the owl folder <br>
-Check in the issues section <br>
