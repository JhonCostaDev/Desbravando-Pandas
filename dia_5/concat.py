#%%
import pandas as pd 
import numpy as np 

data_01 = {
    'id': [1, 2, 3, 4],
    'name': ['Teo', 'Mat', 'Nah', 'Mah'],
    'age': [31, 31, 32,32]
}
df_01 = pd.DataFrame(data_01)

data_02 = {
    'id': [5,6,7,8],
    'name': ['Jose', 'Nathan', 'Arnaldo', 'Mario'],
    'age': [23, 33, 19,21]
}

df_02 = pd.DataFrame(data_02)
# %%

# Empilhando um dataframe em cima do outro
pd.concat([df_01, df_02]).reset_index(drop=True)
# %%
data_03 = {
    'sobrenome': ['Calvo', 'Silva', 'Sousa', 'Costa'],
    'renda': [3100, 3300, 3100,2180]
}

df_03 = pd.DataFrame(data_03).sort_values(by=['renda', 'sobrenome'], ascending=[False, True])
df_03 
# %%
pd.concat( [df_01, df_03], axis=1 )
# %%
df_01
# %%
