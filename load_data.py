import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import statistics 

def load_diabetes_data(filename):
    """
    Loads the wine quality dataset
    :param filename: path to csv file
    :return: X (data) and y (labels)
    """

    data = pd.read_csv(filename, sep=',')
    X = data.iloc[:, :-1]
    mymap = {'Female':0.0, 'Male':1.0, 'No':0.0, 'Yes':1.0}
    y = data.iloc[:, -1]
    y = y.values
    y[y == "Negative"] = 0
    y[y == "Positive"] = 1
    y=y.astype('int')
    for key,value in mymap.items():
        X = X.replace(to_replace=key,value=value)
    print(X)
    return X, y

def load_new_popularity_data(filename):
    """
    Loads the wine quality dataset
    :param filename: path to csv file
    :return: X (data) and y (labels)
    """
    data = pd.read_csv(filename, sep=',')
    X = data.iloc[:, np.r_[1:3,7,9:10,12,13:18,56,57]]
    y = data.iloc[:, -1]
    y = y.values
    y=y.astype('int')
    meanNum = np.median(y)
    print(meanNum)
    y[y<meanNum]=0
    y[y>=meanNum]=1
    return X, y