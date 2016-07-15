import pandas as pd
from pandas import Series, DataFrame

data = pd.read_csv('SACHIN4.CSV', header=None)
list = data[0].unique()

for i in list:
    val = data[data[0] == i]
    name = i + '.csv'
    val.to_csv(name.replace('/', '-'))