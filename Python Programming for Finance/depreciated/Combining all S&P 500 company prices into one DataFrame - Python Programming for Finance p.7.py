"""
Combining all S&P 500 company prices into one DataFrame - Python Programming for Finance p.7
Author: PythonProgramming
Date: 19/03/2021

---- Basically web scraping ----
"""
# Modules
import pickle
import pandas as pd
import bs4 as bs
import requests


# save_sp500_tickers
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


# Script
def compile_data():

    tickers = save_sp500_tickers()
    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):

        try:
            df = pd.read_csv('stocks_dfs/{}.csv'.format(ticker))
        except Exception as ex:
            print('Error: ', ex)
            continue

        df.set_index('Date', inplace=True)

        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Open', 'Volume', 'Close'], 1, inplace=True)
        # print(df.head())

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

compile_data()