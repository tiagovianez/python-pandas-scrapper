import pandas as pd
import requests

header = {'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

url = 'https://br.investing.com/equities/brazil'
request = requests.get(url, headers=header)

## CRIANDO UMA REQUISIÇÃO DE LISTA
df = pd.read_html(request.text)
# print(df)

## CRIANDO UMA NUMERAÇÃO DE TABELAS
for i, table in enumerate(df):
    print('--------------')
    print(i)
    print(table)

## CRIANDO UM DATAFRAME
df = pd.DataFrame(df[0])
# print(df)

## MOSTRANDO RESULTADOS: "Último, Máxima e Mínima COM CASAS DECIMAIS".
df['Último'] = df['Último'] /100
df['Máxima'] = df['Máxima'] /100
df['Mínima'] = df['Mínima'] /100
print(df)