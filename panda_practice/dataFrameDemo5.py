import numpy as np
import pandas as pd

"""
        Group By
"""

data = {'Company': ['Google', 'Google', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Venessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]
        }
df = pd.DataFrame(data)
print(df)


byCompany = df.groupby('Company')
print(byCompany)

print(byCompany.sum())
print(df.groupby('Company').sum().loc['FB'])
print(df.groupby('Company').max())
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
print(df.groupby('Company').describe().transpose()['FB'])