# pib-sampler
Demonstração de amostragem aleatória simples e amostragem aleatória estratificada

## Preparação do ambiente

Para utilizar esse código é necessário realizar a instalação de algumas bibliotecas que utilizaremos nos exemplos:

```bash
$ pip install -r requirements.txt
```

Alem disso, é necessário preparar a base de dados:

### 1 Obtenção dos dados de PIB e População do Brasil

Obtemos estes dados a partir da wikipedi, e um arquivo é salvo no endereço `data/pib_ufs_2015.csv`. Basta executar o comando abaixo:

```bash
$ python get_pib.py
```

Além disso, para finalidade didática, geramos uma população (simulada) para representar nosso conjunto de dados, como se cada pessoa brasileira contruibisse para o PIB. O cósigo abaixo gera uma população relativa à 1% do tamanho real do Brasil.

```bash
python generate_population.py -w 0.01
```

Um novo arquivo é criado em `data/pop_uf_pib.csv`, que sera utilizado pelo nosso script de amostragem.

## Análise

Você pode gerar a análise de forma iterativa a partir do arquivo `samples.py`.