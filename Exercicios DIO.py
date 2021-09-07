
import pandas as pd
# Importando dados sobre pessoa negras no Brasil.
df = pd.read_csv('/content/drive/MyDrive/vw_per_pessoas_pretas.csv')

#Primeira visualização dos dados
df.head()

del df['FID']

df.head()

# Remoção das colunas que nao iram ser usadas
df = df.drop(df.columns[[0, 3,10 ]], axis=1)

df.columns
df.head(3)

import matplotlib.pyplot as plt

df.dtypes

 #Verificando a população Total x Populaçao Negra

 x=[1,2]
 plt.title("Pessoas Negras por Total de População")
 plt.bar(x,height=[df["POP_TOT"].sum(),df["Pessoas_Pretas"].sum()])
 plt.xticks(x,("População Total", "Pessoas Negras"))
 plt.show

 # Verificando a quantidade de pessoas pretas ou pardas por Estados .
# Agrupamento da coluna UF(Estados)(df.groupy)
df.groupby(['UF']).UF.count().sort_values()[-26:].plot(kind = 'bar',figsize=(20,5), color =  'green')
plt.title('Quantidade de Pessoas Pretas por Estados')

#A média de cada estado.

import numpy as np
UF = np.where(df['UF'])

UF_group = df.groupby(['UF','UF']).size().unstack().fillna(0).mean()
UF_group

