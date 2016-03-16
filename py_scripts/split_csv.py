import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#data = data.drop(8, axis = 1)

while True:
	filename = input("Input the file name to split: ")
	data = pd.read_csv(filename, header=None)

    length = len(data)
    data1 = data[0:length:2]
    data2 = data[1:length:2]
    data1.to_csv(filename+'A.csv', index = False)
    data2.to_csv(filename+'B.csv', index = False)
