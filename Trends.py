from pytrends.request import TrendReq
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


pytrends = TrendReq(hl='en-US', tz=360)

# Construindo a payload
pesquisa = 'BB Básico'
kw_list = [pesquisa]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

# Chamando o método interest_over_time e armazenando o resultado
df = pytrends.interest_over_time()

# Agora você pode trabalhar com o DataFrame df. Por exemplo, imprimindo ele:
print(df)

df['Acumulado'] = df[pesquisa].cumsum()

# Plotando os dados
plt.plot(df.index, df[pesquisa])

# Configurar rótulos de eixo
plt.xlabel('Data')
plt.ylabel('Valor Acumulado')

# Mostrar o gráfico
plt.show()
