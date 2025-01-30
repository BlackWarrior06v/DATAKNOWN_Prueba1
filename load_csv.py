import pandas as pd

def load_csv_data(path, separation, decimal, reversed):

    X = pd.read_csv(path, parse_dates=["Date"], sep=separation, decimal=decimal)

    if reversed:
        X = X.iloc[::-1]

    return X