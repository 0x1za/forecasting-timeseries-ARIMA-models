# plot the timeseries data, Visualizing data is good.
from pandas import Series
import matplotlib.pyplot as plt
# load dataset
series = Series.from_csv('data/daily-minimum-temperatures.csv', header=0)

# split the dataset
split_point = len(series) - 7
dataset, validation = series[0:split_point], series[split_point:]
print ('Dataset %d, Validation %d' % (len(dataset), len(validation)))
dataset.to_csv('dataset.csv')
validation.to_csv('validation.csv')
