"""
Handling Data and Graphing - Python Programming for Finance p.2
Author: PythonProgramming
Date: 17/03/2021
"""

# Modules
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web

style.use('ggplot')

# Begining of the script
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

df = web.DataReader('TSLA', 'yahoo', start, end)
df.to_csv('TSLA.csv')

# Reading the file
df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)

# Plotting
df.plot()
plt.show()

df['Adj Close'].plot()
plt.show()

df[['High', 'Low']].plot()
plt.show()