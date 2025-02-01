import pandas as pd
import numpy as np

def load_csv_data(path, separation, decimal, reversed):

    X = pd.read_csv(path, parse_dates=["Date"], sep=separation, decimal=decimal)

    # We will need the data ordered in an ascending way
    if reversed:
        X = X.iloc[::-1]

    return X

def fit_X(dates,a,b):
    return a + b*dates



# The equipment price calculation per month will be the follows:
# We will suppose that the percentajes given in the problem description 
# are the percentaje of a material unity we need to buy

def Equipment1_month_calculation(X,Y):
    return 0.2 * X + 0.8 * Y

def Equipment2_month_calculation(X,Y,Z):
    return 0.33*X + 0.33*Y + 0.33*Z