"""
More stock manipulations - Python Programming for Finance p.4
Author: PythonProgramming
Date: 17/03/2021
"""

# Modules
# import datetime as dt
import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import style
# import pandas_datareader.data as web
import mplfinance as mpl
# import matplotlib.dates as mdates

# Code
df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)
print(df.head())

mpl.plot(df[1000:], volume=True, type='candle', mav=(7, 15, 30, 150))