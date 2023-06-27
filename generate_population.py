# %%
import pandas as pd
import numpy as np
import argparse

# %%
def generate_uf_sample(df, uf, sample_weigth, std_pib=500):

    _, media_pib, size_pop = df[df['uf'] == uf].iloc[0].values

    return np.abs(np.random.normal(loc=media_pib,
                                   scale=std_pib,
                                   size=int(size_pop*sample_weigth)))

def generate_country_pib(df, sample_weigth=1):
    ufs = df['uf'].unique().tolist()
    dfs = []
    for i in ufs:
        df_tmp = pd.DataFrame({'pib_pessoa': generate_uf_sample(df, i, sample_weigth)})
        df_tmp['uf'] = i
        dfs.append(df_tmp)
    return pd.concat(dfs)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--weigth", default=1, type=float, help="Peso para proporção da amostra em relação à população")
    args = parser.parse_args()

    df = pd.read_csv("data/pib_ufs_2015.csv")

    df_pop = generate_country_pib(df, sample_weigth=args.weigth)
    df_pop.to_csv("data/pop_uf_pib.csv", index=False)


if __name__ == "__main__":
    main()
