import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import os

# Obtendo dados do Google Trends
pytrends = TrendReq(hl='en-US', tz=360)
pesquisa = 'BB Básico'
kw_list = [pesquisa]

arquivo_salvo = 'C:/Users/john/Documents/GitHub/Python/df_trends'

if not os.path.exists(arquivo_salvo):
    # Se o arquivo não existir, faça a solicitação e salve os dados
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-y', geo='', gprop='')
    df_trends = pytrends.interest_over_time()
    df_trends['Acumulado'] = df_trends[pesquisa].cumsum()
    df_trends.to_csv(arquivo_salvo)
else:
    # Se o arquivo já existir, apenas leia os dados salvos
    df_trends = pd.read_csv(arquivo_salvo, index_col='date', parse_dates=True)


# Obtendo dados do DataFrame
df = pd.read_excel('C:/Users/john/Downloads/RelatórioUltVendaECOM.xlsx')

novo_df = pd.DataFrame()
novo_df['data'] = df['Ult.Venda'].unique()

# Agora, vamos contar a frequência de cada valor único em 'Ult.Venda'
frequencias = df['Ult.Venda'].value_counts()

# Vamos mapear essas frequências para o nosso novo dataframe
novo_df['Qtd. Vendas'] = novo_df['data'].map(frequencias)

# Plotando os gráficos
fig, ax = plt.subplots()

# Gráfico do Google Trends em azul
ax.plot(df_trends.index, df_trends[pesquisa], color='blue', label='Google Trends')

# Gráfico de Vendas em vermelho
ax.plot(novo_df['data'], novo_df['Qtd. Vendas'], color='red', label='Vendas')

# Configurar rótulos de eixo
ax.set_xlabel('Data')
ax.set_ylabel('Valor')

# Adicionar legenda
ax.legend()

# Mostrar o gráfico
plt.show()
