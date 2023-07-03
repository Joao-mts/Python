import pandas as pd
from sklearn import neural_network
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_excel('C:/Users/john/Documents/Untitled Folder/Inverno22_fechamento.xlsm', sheet_name=1)

label_encoder = LabelEncoder()

df['Linha_encoded'] = label_encoder.fit_transform(df['Linha'])
df['Modelo_encoded'] = label_encoder.fit_transform(df['Modelo'])
df['Grupo_encoded'] = label_encoder.fit_transform(df['Grupo'])
df['TIPO ESTAMPA_encoded'] = label_encoder.fit_transform(df['TIPO ESTAMPA'])

X = df[['Linha_encoded', 'Modelo_encoded', 'Grupo_encoded', 'TIPO ESTAMPA_encoded']]
y = df['Qtd. Venda'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = MLPRegressor(hidden_layer_sizes=(200,200, 200,200), activation='relu', solver='adam',  max_iter=10000, random_state=42)
model.fit(X_train_scaled, y_train)


y_pred = model.predict(X_test_scaled)
y_pred

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R2:", r2)

