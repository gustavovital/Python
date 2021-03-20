"""
Getting all company pricing data in the S&P 500 - Python Programming for Finance p.6
Author: PythonProgramming
Date: 19/03/2021

---- Basically web scraping ----
"""

# Modules
import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas_datareader.data as web


# Script
def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class', 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        tickers.append(ticker)

    with open("sp500tickers.pickle", 'wb') as f:
        pickle.dump(tickers, f)

    return tickers

# save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stocks_dfs'):
        os.makedirs('stocks_dfs')

    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.today()

    for ticker in tickers:
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            try:
                df = web.DataReader(ticker, 'yahoo', start, end)
                df.to_csv("stocks_dfs/{}.csv".format(ticker))
            except Exception as ex:
                print('Error: ', ex)
            # df.reset_index(inplace=True)
            # df.set_index("Date", inplace=True)
            # df = df.drop("Symbol", axis=1)
        else:
            print("Already have {}".format(ticker))

get_data_from_yahoo(True)