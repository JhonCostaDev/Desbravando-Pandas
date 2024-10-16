#%%
# Conectando pandas com banco de dados
import pandas as pd
import sqlalchemy
# %%

engine = sqlalchemy.create_engine('sqlite:///../data/database.db')
engine
# %%
df_customers = pd.read_sql_table('customers', engine) # não é a melhor forma.
# %%
# puxando as 10 primeiras linha
query = 'SELECT * FROM customers LIMIT 10'

df_customers = pd.read_sql_query(query, engine)
df_customers
# %%

query = '''
SELECT *
FROM customers AS t1
LEFT JOIN transactions AS t2
ON t1.UUID = t2.IdCustomer
LIMIT 10
'''

df_join = pd.read_sql_query(query, engine)
df_join.shape
# %%

# Enviando dados a um DB

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
df_01.to_sql('foda-se', engine, index=False)
# %%
df_02.to_sql('foda-se', engine, index=False, if_exists='append')
# %%

pd.read_sql('foda-se', engine)
# %%
