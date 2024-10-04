import pandas as pd 
import numpy as np 
df = pd.read_csv('/home/jonathan/Documents/myGitHub/Desbravando-Pandas/data/customers.csv', sep=';')
df

# Renomeando as colunas
df.rename(columns={'Points':"Pontos", "UUID": "Id", "Name": "Nome"}, inplace=True)
# Criando novas colunas

df["Dobro Pontos"] = df["Pontos"] * 2

df["Pontos Ratio"] = df["Dobro Pontos"] / df["Pontos"]

df["Constante"] = 1

# Aplicando logarítmo em uma coluna
df["Log dos Pontos"] = np.log(df['Pontos'])

# Colacando os Nomes dos usuários em Caixa Alta


df["Nome"].isnull().sum()