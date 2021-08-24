# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:54:17 2021

@author: gusta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

carteira01 = pd.read_csv("E:\\Python\\Python para Investimentos\\carteira01.csv",
                   parse_dates=["Date"])
# data.info()

carteira01["Date"] = pd.to_datetime(carteira01["Date"]).dt.date
carteira01.set_index("Date", inplace = True)

carteira01.drop(columns=carteira01.columns[0], axis = 1, inplace = True)

carteira01.to_pickle("carteira01.pkl")
carteira01.dropna(inplace=True)
# ======================================================================#

carteira01.plot(subplots=True)

# Dados sobre a carteira
carteira01.corr()
sns.heatmap(carteira01.corr(), annot=True)

carteira01["USDBRL=X"].rolling(252).corr(carteira01["BVSP"]).plot()
carteira01["BVSP/USD"] = (carteira01["BVSP"]/carteira01["USDBRL=X"])

carteira01.plot(subplots=True)
