# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:38:35 2021

@author: gusta
"""
# import pandas.rpy2. as com
import pandas as pd

# Read R file (rds)

data = pd.read_csv("E:\\Python\\Python para Investimentos\\BVSP.csv",
                   parse_dates=["Date"])
# data.info()

data["Date"] = pd.to_datetime(data["Date"]).dt.date
data.set_index("Date", inplace = True)

data.drop(columns=data.columns[0], axis = 1, inplace = True)

data["Close"].plot(figsize = (22, 8))

data.to_pickle("BVSP.pkl")
