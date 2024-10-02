#%%
import pandas as pd 

df = pd.read_csv('../data/customers.csv')
df
# %%
df.dtypes
# convertendo para strings

#%%
df['Points'].astype(str)