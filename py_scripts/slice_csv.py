import numpy as np
import pandas as pd
from pandas import Series,DataFrame

filename = input("Input the file name : ")

data = pd.read_csv(filename, header=None)
data = data.drop(8, axis = 1)

while True:
    ip_start = input("Input start time of the slice : ")
    ip_end = input("Input end time of the slice : ")

    start = data.ix[data[1] == ip_start].index[0]
    end = data.ix[data[1] == ip_end].index[0]

    df = data[start:(end+1)]

    name = input("Enter name of the destination file : ")
    df.to_csv(name, index = False)
