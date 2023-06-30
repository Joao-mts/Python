import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import os

# Obtendo dados do Google Trends
pytrends = TrendReq(hl='en-US', tz=360)
pesquisa = 'BB Básico'
kw_list = ['BB Básico', 'bb básico', 'bbbasico', 'bebe basico', 'bbbasico', 'bb basico lojas']

arquivo_salvo = 'C:/Users/john/Documents/GitHub/Python/df_trends.csv'

if not os.path.exists(arquivo_salvo):
    # Se o arquivo não existir, faça a solicitação e salve os dados
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-y', geo='', gprop='')
    df_trends = pytrends.interest_over_time()
    df_trends.to_csv(arquivo_salvo)
else:
    # Se o arquivo já existir, apenas leia os dados salvos
    df_trends = pd.read_csv(arquivo_salvo, index_col='date', parse_dates=True)
