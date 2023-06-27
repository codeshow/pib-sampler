# %%

import pandas as pd

# %%

def format_text_to_number(x):
    return (x.replace('\xa0', '')
             .replace(',','.'))

url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

dfs = pd.read_html(url)
df_pib = dfs[1]

# %%

df_pib['pib_per_capita'] = ((df_pib['PIB per capita (R$) (2015)'].apply(format_text_to_number)
                                                                 .astype(float)))

df_pib['populacao'] = ((df_pib['População (2014)'].apply(format_text_to_number)
                                                  .astype(int)))

df_pib['uf'] = df_pib['Abreviação']

df_pib[['uf', 'pib_per_capita', 'populacao']].to_csv("data/pib_ufs_2015.csv", index=False)
