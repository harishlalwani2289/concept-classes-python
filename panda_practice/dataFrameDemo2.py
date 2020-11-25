import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
"""
    Conditional Selection in data frame
"""
print(df)
booldf = df > 0
print(booldf)

print(df[booldf])
print(df[df > 0])

print(df['W'] > 0)
print(df[df['W'] > 0])

print(df[df['Z'] < 0])

resultdf = df[df['W'] > 0]
print(resultdf['X'])

print(df[df['W'] > 0][['X', 'Y']])

boolSeries = df['W'] > 0
print(boolSeries)
resultdf = df[boolSeries]
print(resultdf)
print(resultdf[['Y', 'X']])

"""
Multiple conditions
"""
# Below satement is error
# print(df[(df['W'] > 0) and (df['Y']  > 1) ])

print(df[(df['W'] > 0) | (df['Y'] > 1)])


df.reset_index()

newind = 'CS NY WY OR CO'.split()

df['states'] = newind
print(df)
df.set_index('states',inplace=True)
print(df)