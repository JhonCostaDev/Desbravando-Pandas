#%%
import pandas as pd 
import numpy as np 

# %%
# Agregação: Forma de resumir um conjunto de dados em um único valor por meio de uma estatística.

file_path = '../data/transactions.xlsx'
df = pd.read_excel(file_path)
df
# %%
# Quantos pontos o usuário 5f8fcbe0-6014-43f8-8b83-38cf2f4887b3 teve acumulado?

mascara = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'

df_user = df[mascara]
# Dataframe apenas com as transações do usuário.
df_user
# %%
# Pontos acumulados do usuário
pontos = df_user['Points'].sum()
print(f'O usuário tem {pontos} pontos')
# %%

# Como fazer um somatório de todos os usuários?

# Forma Burra

pontos = {}
for uuid in df['IdCustomer'].unique():
  user_points = df[df['IdCustomer'] == uuid]
  pontos[uuid] = user_points['Points'].sum()

burra = pd.DataFrame(pontos.items(), columns=['IdCustomer', 'Points'])
burra
# %%
# USANDO GROUPBY e sort_values para ordenar
pontos_por_usuario = df.groupby(['IdCustomer'])['Points'].sum().sort_values(ascending=False).reset_index()
pontos_por_usuario
# %%
# Descobrindo quantas transações fez cada usuário e adicionando ao dataframe recem criado.

# GroupBy com Agg 
transacoes_pontos_usuario = (df.groupby(['IdCustomer'])
                             .agg({
                                 'Points': 'sum', 
                                 'UUID': 'count',
                                 'DtTransaction': 'max'
                                 })
                             .sort_values(by='Points', ascending=False))

transacoes_pontos_usuario
# %%
# Renomeando as colunas

atual = list(transacoes_pontos_usuario.keys())
nova = ['Pontos', 'Frequência', 'Última_transação']
dic = dict(zip(atual, nova))
transacoes_pontos_usuario.rename(columns=dic, inplace=True)
# %%
transacoes_pontos_usuario
# %%
# Descobrir quantos dias tem de diferença da última transação para o data atual

# Importando as bibliotecas necessárias
from dateutil import relativedelta
import datetime

# Atribuindo a data atual a uma variável
dt_atual = datetime.datetime.now()

# Pegando uma data do dataframe
df_data = df['DtTransaction'].dt.date[0]
# %%
# Calculando a diferença
diferanca = relativedelta.relativedelta(dt_atual, df_data)
diferanca
# %%
# FORMA CURTA

import datetime
df_data = df['DtTransaction'][0]
dt_atual = datetime.datetime.now()

diferenca = (dt_atual - df_data).days
str(diferenca) + ' Dias de diferenaça'
# %%
# Saber a quantos dias cada um do usuário está sem comprar.
df
# %%
def recencia(vetor):
    diff = datetime.datetime.now() - vetor.max()
    return diff.days
# %%
df_recencia = (df.groupby(['IdCustomer'])
                             .agg({
                                 'Points': 'sum', 
                                 'UUID': 'count',
                                 'DtTransaction': ['max', recencia]
                                 }))
#%%
df_recencia.rename(columns={
    'sum': 'Pontos', 'count': 'Operações', 'max': 'Última Transação', 'recencia': 'Dias da última operação'
}, inplace=True)
# %%
df_recencia.sort_values(by=('Points', 'Pontos'),ascending=False, inplace=True)
# %%
# Gravando em um csv
df_recencia.to_csv('recencia.csv')
# %%
# TOBE COntinue: min 1:28:40