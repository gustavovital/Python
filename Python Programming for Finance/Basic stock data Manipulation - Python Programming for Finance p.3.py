"""
Basic stock data Manipulation - Python Programming for Finance p.3
Author: PythonProgramming
Date: 17/03/2021
"""

import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# Begining of the script
df = pd.read_csv('TSLA.csv')
print(df.head())

# Creating rolling mean (by 100 days)
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# Graphing the stuff
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])

plt.show()