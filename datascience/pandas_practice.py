import numpy as np
import pandas as pd
from numpy.random import randn


np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df['Z'])  # df['Z'] grabs column, df.Z is also possible but not recommended

print(df[['W', 'X']])  # Use list to get multiple columns

df['New'] = df['X'] + df['Y']  # Add new column to df

print(df)

df.drop('New',axis=1,inplace=True)  # To drop a column use axis and inplace to specify

print(df)

print(df[df['X']>0]['W'])  # Conditional Selection 

df1 = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[10,np.nan,np.nan],
                  'C':[1,2,3]})

print(df1.dropna())
print(df1.fillna(value=df1.mean()))  # Fills nan with mean of each column