#%%
import pandas as pd 
'''
data = {
    "nome":["jhon", "flower", "rose", "ana", "Tarcísio"],
    "sobrenome": ["costa", "costa", "oliveira", "alves", "costa"],
    "idade": [38, 12, 40, 71, 68]
    }
'''

data = {
    "Nome": ["Teo", "Nah", "Maria", "Nah","Lara", "Teo"],
    "Idade": [32, 33, 2, 33, 31, 32],
    "Updated_at": [1,2,3,1,2,3]
}
df = pd.DataFrame(data)

df
# %%
# Removendo duplicados 
df.drop_duplicates()
# %%
# Escolhendo as colunas que serão avaliadas os dados duplicados
df.drop_duplicates(subset=['Nome', 'Idade'], keep='last')


# %%
# ENCADEANDO COMANDOS

df = (df.sort_values(by='Updated_at', ascending=False)
    .drop_duplicates(subset=['Nome', 'Idade'], keep='first')
)
df
# %%
