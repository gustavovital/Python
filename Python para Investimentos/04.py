# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:42:06 2021

@author: gusta
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Leitura dos dados
carteira02 = pd.read_csv("E:\\Python\\Python para Investimentos\\carteira02.csv",
                   parse_dates=["Date"])


carteira02["Date"] = pd.to_datetime(carteira02["Date"]).dt.date
carteira02.set_index("Date", inplace = True)

carteira02.drop(columns=carteira02.columns[0], axis = 1, inplace = True)

carteira02.to_pickle("carteira02.pkl")
carteira02.dropna(inplace=True)

# Leitura de bvsp

BVSP = pd.read_csv("E:\\Python\\Python para Investimentos\\BVSP.csv",
                   parse_dates=["Date"])
BVSP["Date"] = pd.to_datetime(BVSP["Date"]).dt.date
BVSP.set_index("Date", inplace = True)

BVSP.drop(columns=BVSP.columns[0], axis = 1, inplace = True)
BVSP.dropna(inplace=True)

BVSPAdj = BVSP["Adjusted"]

# config sns
sns.set()
carteira02.plot()

# ibov/carteira normalizada
carteira02_normalizada = (carteira02 / carteira02.iloc[0])
carteira02_normalizada.plot()
carteira02_normalizada["Saldo"] = carteira02_normalizada.sum(axis=1)

BVSPAdj_normalizado = (BVSPAdj / BVSPAdj.iloc[0])*5
BVSPAdj_normalizado.plot()

carteira02_normalizada["Saldo"].plot(label="Saldo")
BVSPAdj_normalizado.plot(label="bvsp")
plt.legend()

