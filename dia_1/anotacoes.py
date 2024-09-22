#   LINK DA APRESENTAÇÃO .PPTX
# https://docs.google.com/presentation/d/1FZLyigxZiE8qJGHp9yxsM23h4K-8_2K8/edit#slide=id.g2c1da08af43_4_0

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