import pandas as pd

def backtest_strategy(df, buy_signal, sell_signal):
    """ Simulates a backtest of a trading strategy """
    balance = 1000
    for i in range(len(df)):
        if df.iloc[i][buy_signal]:
            balance -= df.iloc[i]['Close']
        elif df.iloc[i][sell_signal]:
            balance += df.iloc[i]['Close']

    return balance
