# plot the timeseries data, Visualizing data is good.
from pandas import Series
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
# load dataset
series = Series.from_csv('data/daily-minimum-temperatures.csv', header=0)

# split the dataset
split_point = len(series) - 7
dataset, validation = series[0:split_point], series[split_point:]
print ('Dataset %d, Validation %d' % (len(dataset), len(validation)))
dataset.to_csv('dataset.csv')
validation.to_csv('validation.csv')

# create differenced series
def differenced(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return np.array(diff)

# load dataset for ARIMA model
series = Series.from_csv('dataset.csv', header=None)
# seasonal difference

# invert differenced value
def inverve_difference(history, yhat, interval=1):
    return yhat + history[-history]

