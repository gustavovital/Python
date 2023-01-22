"""
Intro and Getting Stock Price Data - Python Programming for Finance p.1
Author: PythonProgramming
Date: 17/03/2021
"""

# Modules and definitions
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# Begining of the script
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

# Dataframe
df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head())

# plt.plot(df['Close'])