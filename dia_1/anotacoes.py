#%%
print("Hello World!")
# %%
import pandas as pd 
import numpy as np
# %%
# Lista de idades
idades = [30, 42, 90, 34]

# Como calcular a media com listas
media = sum(idades) / len(idades)
media
# %%
# Usando numpy
media = np.mean(idades)
media

# %%

# Calculando desvio padrão