#%%
import pandas as pd 
import numpy as np 

# %%
data_dogs = {
    'id': [1, 2, 3, 4],
    'name': ['Fulio', 'Jrunior', 'Bolots', 'Filha Menina'],
    'age': [8, 1, 2, 4]
}

df_dogs = pd.DataFrame(data_dogs)
df_dogs
# %%
data_transactions = {
    'id_user': [1, 1, 1, 2, 3, 3, 5],
    'v1': [432, 532, 123, 6, 4, 87, 10],
    'qtProdutos': [2, 1, 3, 6, 10, 2, 7]
}
df_transactions = pd.DataFrame(data_transactions)
df_transactions 
# %%
# Juntando dataframes, aqui os valores que não concidirem serão preenchidos com Nan

df_transactions.merge(df_dogs, 
                      how='left',
                      left_on=['id_user'],
                      right_on=['id'],
                      )
# %%
# Pegando apenas os dados que constam em ambas as tabelas.
df_transactions.merge(df_dogs, 
                      how='inner',
                      left_on=['id_user'],
                      right_on=['id'],
                      )
# %%
