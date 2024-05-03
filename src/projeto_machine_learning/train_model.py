import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Passo 1: Carregamento dos Dados
dados = pd.read_csv('dados_poluicao_ar.csv')

# Passo 2: Pré-processamento dos Dados
X = dados[['hora']]  # Recursos (hora do dia)
y = dados['poluicao_ar']  # Rótulos (índice de poluição do ar)

# Divisão dos dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 3: Treinamento do Modelo
modelo = LinearRegression()  # Criação do modelo de regressão linear
modelo.fit(X_train, y_train)  # Treinamento do modelo

# Passo 4: Avaliação do Modelo
y_pred = modelo.predict(X_test)  # Previsões do modelo para os dados de teste
r2 = r2_score(y_test, y_pred)  # Coeficiente de determinação (R²)

print("Modelo treinado com sucesso!")
print(f"Coeficiente de Determinação (R²): {r2:.2f}")
