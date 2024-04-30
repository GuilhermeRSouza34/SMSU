# Importando bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Carregando os dados (substitua 'data.csv' pelo seu arquivo de dados)
data = pd.read_csv('data.csv')

# Dividindo os dados em conjunto de treinamento e teste
X = data[['Temperatura', 'Umidade', 'Poluentes']].values
y = data['Qualidade_do_ar'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo de regressão com RandomForest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliando o modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)



