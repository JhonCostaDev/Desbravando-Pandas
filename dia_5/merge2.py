#%%
import pandas as pd 
import numpy as np 
# %%
# Importando CSV
costumer_path = '../data/customers.csv'
df_costumer = pd.read_csv(costumer_path, sep=';')
df_costumer.head()
# %%
# Importando Excel
transactions_path = '../data/transactions.xlsx'
df_transactions = pd.read_excel(transactions_path)
df_transactions.head()
# %%

# IMportando Parquet
transactions_product_path = '../data/transactions_cart.parquet'
df_transactions_product = pd.read_parquet(transactions_product_path)
df_transactions_product
# %%
# Juntando primeiras duas Tabelas

df_join = df_transactions.merge(df_costumer, 
                      how='inner',
                      left_on=['IdCustomer'],
                      right_on=['UUID'],
                      suffixes=['_transacao', '_cliente']
                      )
df_join 
# %%
# Merge da terceira tablea
df_join.merge(df_transactions_product,
            how='inner',
            left_on='UUID_transacao',
            right_on='IdTransaction'
    
).head()
# %%

# fazendo dois merges em um mesmo comando
df_join = df_transactions.merge(df_costumer, 
                    how='inner',
                    left_on=['IdCustomer'],
                    right_on=['UUID'],
                    suffixes=['_transacao', '_cliente']
                    ).merge(df_transactions_product,
                    how='inner',
                    left_on='UUID_transacao',
                    right_on='IdTransaction'
    
)
                    
df_join.head()
# %%
df_join.shape
# %%
