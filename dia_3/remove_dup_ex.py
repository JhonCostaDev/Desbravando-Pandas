#%%
import pandas as pd 

df = pd.read_excel('../data/transactions.xlsx')
df

# %%
# Qual o valor da última trasação de cada ID_Customer

df_unicos = df.sort_values(by='DtTransaction', ascending=False).drop_duplicates(subset=['IdCustomer'], keep='last')

# %%
# Saber quantos únicos tem 
df_unicos['IdCustomer'].nunique()

# %%
mascara = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_unicos[mascara]
# %%
