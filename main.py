import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import statsmodels
import math

flight = pd.read_csv('flight.csv')
print(flight.head())

perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight_sub, line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()

## Task 5
# Inflight Meals
sns.histplot(flight, x = "coach_price", hue = flight.inflight_meal)
plt.show()
plt.clf()
 
# Inflight Entertainment
sns.histplot(flight, x = "coach_price", hue = flight.inflight_entertainment)
plt.show()
plt.clf()
 
# Inflight WiFi
sns.histplot(flight, x = "coach_price", hue = flight.inflight_wifi)
plt.show()
plt.clf()
 

## Task 6
sns.lmplot(x = "hours", y = "passengers", data = flight_sub, x_jitter = 0.25, scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False)
plt.show()
plt.clf()


sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight, hue = "weekend", fit_reg = False)
plt.show()
plt.clf()

sns.boxplot(x = "day_of_week", y="coach_price", data=flight, hue = "redeye").set(
    xlabel='Day Of Week', 
    ylabel='Price')
plt.show()
plt.clf()
