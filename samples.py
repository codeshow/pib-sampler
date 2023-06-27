# %%

import pandas as pd
import numpy as np

from tqdm import tqdm

# %%

df = pd.read_csv("data/pop_uf_pib.csv")
df.head()

# %%

media_pib_nacional = df['pib_pessoa'].mean()
print(f"PIB per capita Pop R${media_pib_nacional:.02f}")

print("Tamanho da população", df['pib_pessoa'].shape[0])

# %%

medias_simples = []
for i in tqdm(range(100)):
    amostra_simples = np.random.choice(df['pib_pessoa'], size=100)
    media_simples = amostra_simples.mean()
    # print(f"PIB per capita Amostra R${media_simples:.02f}")
    medias_simples.append(media_simples)

print(f"Média das médias: {np.mean(medias_simples):.02f}")
print(f"Desvio das médias: {np.std(medias_simples):.02f}")

# %%

df_peso = df.groupby('uf')['pib_pessoa'].count()
df_peso = df_peso/df.shape[0]
df_peso = (df_peso.reset_index()
                  .rename(columns={'pib_pessoa':'peso'}))

medias_estratificadas = []
for i in tqdm(range(100)):
    medias_ufs = []
    for uf in df['uf'].unique():
        peso = df_peso[df_peso['uf']==uf]['peso'].iloc[0]
        data = df[df['uf']==uf]
        amostra = np.random.choice(data['pib_pessoa'], size=max([int(100*peso),1]))
        media_uf = np.mean(amostra)
        media_uf_penalizada = media_uf * peso
        medias_ufs.append(media_uf_penalizada)

    medias_estratificadas.append(np.sum(medias_ufs))

print(f"Média das médias Estrat.: {np.mean(medias_estratificadas):.02f}")
print(f"Desvio das médias Estrat: {np.std(medias_estratificadas):.02f}")
