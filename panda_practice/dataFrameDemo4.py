import numpy as np
import pandas as pd
from numpy.random import randn

d = {
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3]
    }
df = pd.DataFrame(d)
print(df)
"""
    drop na method
"""
print(df.dropna(axis=1))
print(df.dropna())
print(df.dropna(thresh=2))

"""
df fill na
"""
print(df.fillna(value='Harish'))
print(df.fillna(value=df['A'].mean()))
