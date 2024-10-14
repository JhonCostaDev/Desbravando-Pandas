#%%
import pandas as pd 
import numpy as np 

file_path = '../data/ipea/homicidios.csv'
df_1 = pd.read_csv(file_path, sep=';')
df_1 = df.rename(columns={'valor':'homicidios'})
df_1

# %%
file_path_2 = '../data/ipea/homicidios-por-armas-de-fogo.csv'
df_2 = pd.read_csv(file_path_2, sep=';')
df_2 = df_2.rename(columns={'valor':'homicidios-por-armas-de-fogo'})
df_2
# %%
df_1 = df_1.set_index(['cod','nome','período'])
df_2 = df_2.set_index(['cod','nome','período'])
# %%
df_2
# %%
pd.concat([df_1, df_2], axis=1).reset_index()
# %%
