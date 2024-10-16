#%%
import pandas as pd 
import numpy as np
import os
# %%
# Foi criado uma função para fazer os importes do csv.
def import_etl(path: str): # Recebe o caminho para pasta onde estão os arquivos
    name = path.split('/')[-1].split('.')[0] # Variável que vai nomear as tabelas com o mesmo nome dos seus respectivos arquivos.
    
    df = ( # contruindo o dataframe
        pd.read_csv(path, sep=';')
        .rename(columns={'valor': name})
        .set_index(['cod', 'nome', 'período'])
    )
    return df
# %%
path = '../data/ipea/'
files = os.listdir(path)
files
dfs = []
for i in files:
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