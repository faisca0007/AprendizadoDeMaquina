import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Carregar os dados
data = pd.read_csv('imc_data.csv')

# 2. Preparar os dados
X = data[['IMC']]  # Feature
y = data['Obeso']   # Target

# 3. Dividir em treino e teste (usando todos os dados para treino neste caso pequeno)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Criar e treinar o modelo
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Avaliar o modelo (opcional)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2f}")

# 6. Função para fazer previsões
def predict_obesity(imc):
    prediction = model.predict([[imc]])
    return "Obeso" if prediction[0] else "Não obeso"

# 7. Testar com valores fora do range original
test_values = [17.5, 28.0, 31.5, 42.0]  # Valores abaixo e acima do range original

print("\nTestando com valores fora do range original:")
for imc in test_values:
    print(f"IMC: {imc} - Classificação: {predict_obesity(imc)}")