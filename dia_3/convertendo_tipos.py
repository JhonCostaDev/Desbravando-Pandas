#%%
import pandas as pd 

df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%
df.dtypes
df.shape
# adicionando uma nova colunas pontos dobrados

df['Points_doubled'] = df['Points'] * 2



# %%
df.rename(columns={'UUID': 'ID', 'Name': 'Nome', 'Points':'Pontos', 'Points_doubled': 'Pontos Dobrados'}, inplace=True)
# %%
df.dtypes
# %%
# Convertendo colunas para float

df[['Pontos', 'Pontos Dobrados']].astype(float)
# %%
df.dtypes
# %%
df[['Pontos', 'Pontos Dobrados']] = df[['Pontos', 'Pontos Dobrados']].astype(float)
# %%
df
# %%
