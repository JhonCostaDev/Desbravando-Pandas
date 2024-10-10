#%%
import pandas as pd 
import numpy as np 

data = {
    'nome': ['teo', 'Nah', 'Lah', 'Mah', 'Jo'],
    'Idade': [31, 32, 34, 12, np.nan],
    'renda': [np.nan, 3245, 357, 12432, np.nan]
}
# %%
df = pd.DataFrame(data)
df
# %%
# Contagem de dados nulos Nan
# isna()renorna uma seria com as colunas que contém dados nulos
df.isna().sum()
# %%
# Adicionando mais um SUm() conseguimos o total de nulos no dataframe. 
df.isna().sum().sum()
# %%
# Descobrir a Proporção de Nan
# Depois de obter o DataFrame booleano, usar mean() calcula a média de valores True (1) e False (0) para cada coluna. A média, nesse caso, representa a proporção de valores True, que são os valores nulos.
df.isna().mean()

# %%
# SUBSTITUINDO NANS POR OUTRO VALOR

# 0
df.fillna(0)
# %%
# Preenchendo com a média da coluna.
# Passando um dicionário ou uma série.
df.fillna(
    {
        'Idade': df['Idade'].mean(),
        'renda': df['renda'].mean()
    }
)
# %%
# DROP NAn
# 
df.dropna() # Remove todas as linhas com NaN
# %%
# Melhorando
df.dropna(how='all') # só remove se todas as colunas da linha são NaN
# %%
# Passando uma condição, as colunas do subset tem que ser Nan
df.dropna(subset=['Idade', 'renda'], how='all')
# %%
# Passando uma condição, as colunas do subset ao menos uma tem que ser Nan
df.dropna(subset=['Idade', 'renda'], how='any')
# %%
# Usando axis para mudar a avaliação para colunas
df.dropna(axis=1, how='any')
# %%
# Remove a coluna com base na quantidade de não nulos no dataframe.
df.dropna(axis=1, thresh=3)
# %%
