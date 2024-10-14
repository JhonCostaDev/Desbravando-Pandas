#%%
import pandas as pd 
import numpy as np
import os
# %%
# Foi criado uma função para fazer os importes do csv.
def import_etl(path: str):
    name = path.split('/')[-1].split('.')[0]
    
    df = (
        pd.read_csv(path, sep=';')
        .rename(columns={'valor': name})
        .set_index(['cod', 'nome', 'período'])
    )
    return df
# %%
path = '../data/ipea/'
files = os.listdir(path)

dfs = []
for i in files_path:
    dfs.append(import_etl(path + i))
# %%
# Juntando todos os arquivos em um único DataFrame.

df = pd.concat(dfs, axis=1).reset_index()
df
# %%
df.to_parquet(path + 'consolidado.parquet')

# %%
# Verificando se foi salvo corretamente.
teste = pd.read_parquet(path + 'consolidado.parquet')
teste
# %%
teste[teste['nome'] == 'CE']
# %%
# TODO: continuar no minuto: 1:04 - conectando banco de dados com pandas.