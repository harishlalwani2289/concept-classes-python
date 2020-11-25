import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
"""
    MultiIndex and index hierarchy
"""
outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index1 = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index1,['A','B'])

print(df)
print(df.loc['G1'].loc[1])

print(df.index.names)
df.index.names = ['Groups','Num']
print(df)


print(df.loc['G2'].loc[2]['B'])
print(df.loc['G1'].loc[3]['A'])

"""
    Cross section
"""
print(df.xs(1,level='Num'))

