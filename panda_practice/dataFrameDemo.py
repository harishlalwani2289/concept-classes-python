import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'],['W', 'X', 'Y', 'Z'])
"""
    W X Y Z are individual series sharing same index A, B,C,D and E
"""
print(type(df['W']))
print(df[['W','X']])

# Creating new column
df['new'] = df['W'] + df['Y']
print(df)
df.drop('new',axis=1,inplace=True)
print(df)
"""
    Axis defines whether we are dropping the row or column
    Axis is 0 for rows -- by default
    Axis value should be 1 for columns
"""
df.drop('E',inplace=True)
print(df)

print(df.shape)

print(df.loc['A'])
"""
    Rows are series to
"""
print(df.iloc[2])

print(df.loc['B','Y'])

print(df.loc[['B','C'],['W','Z']])