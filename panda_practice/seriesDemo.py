import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}
series1 = pd.Series(data=my_data, index=labels)
series2 = pd.Series(d)

print(series1)
print(series2)

ser1 = pd.Series([1, 2, 3, 4], ["USA", "Germany", 'USSR', 'Italy'])
ser2 = pd.Series([1, 2, 5, 4], ["USA", "Germany", "Italy", "japan"])
print(ser1["USA"])
ser3= pd.Series(labels)
print(ser3[1])
print(ser1+ser2)