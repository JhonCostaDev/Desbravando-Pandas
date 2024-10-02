#%%
import pandas as pd
import numpy as np 

df = pd.read_csv('../data/customers.csv', sep=';')

df

#%%
# SORT_VALUES -ordenando do menor  para o maior.

df.sort_values(by='Points')

# ordenando do maior para o menor

df.sort_values(by='Points', ascending=False)

# Sobreescrever o comando.
df.sort_values(by='Points', ascending=False, inplace=True)

# Renomeando as colunas
#%%
df.rename(columns={'Name': 'Nome', 'Points': 'Pontos'}, inplace=True)
df
# %%
# ENCADEANDO COMANDOS
df = (
    df.sort_values(by='Points', ascending=False)
    .rename(columns={'Name': 'Nome', 'Points': 'Pontos'})
)
# %%
# ORDENANDO OS CRITÉRIOS DE DESEMPATE - Usado quando tiver empates, e então o desempate ordem
#alfabética.
df = (
    df.sort_values(by=['Points', 'Name'], ascending=[False, True])
    .rename(columns={'Name': 'Nome', 'Points': 'Pontos'})
)
df.tail(10)
# %%
