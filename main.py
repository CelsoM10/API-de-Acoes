from chave import chave_api
from IPython.display import display
import pandas as pd
from io import StringIO # -> biblioteca que transforma text em csv
import pprint
import requests


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=ITUB3.SAO&apikey={chave_api}'
r = requests.get(url)
data = r.json()

#print(data)

#pegando cotaçoes semanais em csv:
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={chave_api}&datatype=csv'
r = requests.get(url)
tabela = pd.read_csv(StringIO(r.text)) #--> transformar o arquivo text em csv
display(tabela)

#Pegando cotaçao de mais de uma ação --> olhando na API as ultimas citaçoes de cada açoes esolhidadas
acoes = ['ITUB4', 'ABEV3', 'BBAS3']
#Como quremos fazer esse processo para 3 cotaçoes e armazer em uma unica tabela, vamos precorrer a lista de açoes:
compilada = pd.DataFrame()

for acao in acoes: 
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SAO&apikey={chave_api}&datatype=csv'
    r = requests.get(url)
    tabela = pd.read_csv(StringIO(r.text)) #--> transformar o arquivo text em csv
    lista_tabelas = [compilada, tabela] # --> lista das nosss duas tabelas
    compilada = pd.concat(lista_tabelas) # --> adicionando as duas tabelas para aramazenar os resultados numa unica

display(compilada)

#descobrindo Açoes fazendo busca 
url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=Amazon&apikey={chave_api}&datatype=csv'
r = requests.get(url)
tabela = pd.read_csv(StringIO(r.text)) #--> transformar o arquivo text em csv
display(tabela)

#Informações de Resultado
url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol=AMZN&apikey={chave_api}'
r = requests.get(url)
data = r.json()
pprint.pprint(data)

resultado = pd.DataFrame(data['annualEarnings'])
display(resultado)
