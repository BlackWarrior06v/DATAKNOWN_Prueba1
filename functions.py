import pandas as pd
import numpy as np

def load_csv_data(path, separation, decimal, reversed):

    X = pd.read_csv(path, parse_dates=["Date"], sep=separation, decimal=decimal)

    if reversed:
        X = X.iloc[::-1]

    return X

def fit_X(dates,a,b):
    return a + b*dates