import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/john/Downloads/RelatórioUltVendaECOM.xlsx')

print(df['VL de Venda'].sum())



# print(df)
# print(df.head())

plt.plot(df['Ult.Venda'], df['VL de Venda'])

# Configurar rótulos de eixo
plt.xlabel('Data')
plt.ylabel('Valor de venda')

plt.show()

novo_df = pd.DataFrame()
novo_df['data'] = df['Ult.Venda'].unique()

# Agora, vamos contar a frequência de cada valor único em 'Ult.Venda'
frequencias = df['Ult.Venda'].value_counts()

# Vamos mapear essas frequências para o nosso novo dataframe
novo_df['Qtd. Vendas'] = novo_df['data'].map(frequencias)

# Exibir o novo dataframe
print(novo_df)