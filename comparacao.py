import pandas as pd
import matplotlib.pyplot as plt

dfp = pd.read_excel('C:/Users/john/Documents/GitHub/Python/Pesquisa.xlsx')

dfp['agregado']=dfp['soma'].cumsum()

df = pd.read_excel('C:/Users/john/Downloads/RelatórioUltVendaECOM.xlsx')


novo_df = pd.DataFrame()
novo_df['data'] = df['Ult.Venda'].unique()

# Agora, vamos contar a frequência de cada valor único em 'Ult.Venda'
frequencias = df['Ult.Venda'].value_counts()

# Vamos mapear essas frequências para o nosso novo dataframe
novo_df['Qtd. Vendas'] = novo_df['data'].map(frequencias)

novo_df['greg'] = novo_df['Qtd. Vendas'].cumsum()

print(dfp)
print(novo_df)


# Plotando os gráficos
fig, ax = plt.subplots()

# Gráfico do Google Trends em azul
ax.plot(dfp['Semana'], dfp['agregado'], color='blue', label='Google Trends')

# Gráfico de Vendas em vermelho
ax.plot(novo_df['data'], novo_df['greg'], color='red', label='Vendas')

# Configurar rótulos de eixo
ax.set_xlabel('Data')
ax.set_ylabel('Valor')

# Adicionar legenda
ax.legend()

# Mostrar o gráfico
plt.show()


dfp['Semana'] = pd.to_datetime(dfp['Semana'])
novo_df['data'] = pd.to_datetime(novo_df['data'])

# Configurando as colunas de data como índice
dfp.set_index('Semana', inplace=True)
novo_df.set_index('data', inplace=True)

# Agregando por semana e calculando a soma
dfp_resampled = dfp.resample('W').sum()
novo_df_resampled = novo_df.resample('W').sum()

# Agora vamos unir os dois dataframes
df_merged = pd.merge(dfp_resampled, novo_df_resampled, left_index=True, right_index=True, how='inner')

# Calculando a correlação
correlation = df_merged['agregado'].corr(df_merged['greg'])

print(df_merged)

print(f"A correlação entre 'soma' e 'Qtd. Vendas' é: {correlation}")




