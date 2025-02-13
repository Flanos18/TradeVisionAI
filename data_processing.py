import pandas as pd
import numpy as np

def clean_data(df):
    """ Cleans financial data by removing NaN values and duplicates """
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def calculate_moving_average(df, window=14):
    """ Calculates the moving average for given window size """
    df['Moving_Avg'] = df['Close'].rolling(window=window).mean()
    return df
