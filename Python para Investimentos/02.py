# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:48:40 2021

@author: gusta
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


bvsp = pd.read_pickle("BVSP.pkl")
# bvsp.head()
# bvsp.tail()
bvsp.index = pd.to_datetime(bvsp.index)
bvsp.dropna(inplace=True)
# bvsp.info()

# analise grafica
bvsp["Close"].plot(label="IBOV")
bvsp["Close"].rolling(21).mean().plot(label="MM21")
bvsp["Close"].rolling(200).mean().plot(label="MM200")
plt.legend()

# IBOV 2008
bsvp_2008 = bvsp[bvsp.index.year == 2008]

bsvp_2008["Close"].plot(label="IBOV")
bsvp_2008["Close"].rolling(21).mean().plot(label="MM21")
bsvp_2008["Close"].rolling(200).mean().plot(label="MM200")
plt.legend()

# IBOV >= 2020
bsvp_2020 = bvsp[bvsp.index.year >= 2020]

bsvp_2020["Close"].plot(label="IBOV")
bsvp_2020["Close"].rolling(21).mean().plot(label="MM21")
bsvp_2020["Close"].rolling(200).mean().plot(label="MM200")
plt.legend()



