import pandas as pd # Manipulação e Análise de Dados
from sklearn.tree import DecisionTreeClassifier    # Classificador da Árvore de Decisão
from sklearn.model_selection import train_test_split # Dividir o conjunto de dados de treinamento e teste
from sklearn import metrics # Calcular a acurácia do modelo

from sklearn.metrics import confusion_matrix

# carrega o conjunto de dados
pima = pd.read_csv("diabetes.csv")

# print(pima.head(10))

# Divisão do conjunto de dados em variáveis dependendentes e independentes 
feature_cols = ['Pregnancies', 'Insulin', 'BMI', 'Age', 'Glucose', 'BloodPressure', 'DiabetesPedigreeFunction']

X = pima[feature_cols] # Variável Independente
y = pima['Outcome'] # Variável dependente

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% de treinamento e 30% de teste

# Cria o objeto da Árvore de Decisão
clf = DecisionTreeClassifier()  

# Classificador
clf = clf.fit(X_train, y_train)

# Predição baseado no conjunto de dados
y_pred = clf.predict(X_test)

# Acurácia do Modelo
print("Acurácia: ", metrics.accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))
