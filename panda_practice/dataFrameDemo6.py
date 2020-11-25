import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

print(df.head())

print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

print(df[(df['col1'] > 2) & (df['col2'] == 444)])


def times2(x):
    return x * 2


print(df['col2'].apply(times2))
print(df['col2'].apply(lambda x:x*2))

print(df.drop('col1',axis=1))

print(df.columns)
print(df.index)


print(df.sort_values('col2'))

print(df.isnull())