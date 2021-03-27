## Global Warming and Climate Change Prediction using Time Series Analysis

### Contents:
- What is Time Series Data and Time Series Analysis
- Time Series Use Cases
- Tools and Requirements

#### Time Series Data and Time Series Analysis
[Time Series(Time Stamped) Data](https://www.investopedia.com/terms/t/timeseries.asp) can be seen as temporal data, i.e that collected over time at fixed intervals repeatedly.

[Time Series Analysis](link) Is the Statistical Act/Technique of collecting of Time Series Data and Trends and Anlyssing them.Purposely for [Monitoring of Nature of the Pheenomena](link) to aid in the [Forecasting](link) of measurable outcomes by extrapolating in time.
### Built With
[Python3](https)
[Data, CSV](https)
[Statsmodels](https)
[Statstools](https)

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

Date: starts in 1743 for average land temperature.
By 1850 , there were provisions for max and min land temperatures and global ocean and land temperatures
LandAverageTemperature: global average land temperature in celsius
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
