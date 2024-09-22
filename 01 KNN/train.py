import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from KNN import KNN  # Importa a implementação personalizada do KNN

# Define um mapa de cores para a visualização (vermelho, verde, azul)
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Carrega o dataset Iris, um conjunto de dados clássico para classificação
iris = datasets.load_iris()
X, y = iris.data, iris.target  # X contém as features e y contém os rótulos (targets)

# Divide o dataset em conjunto de treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Cria uma nova figura para o gráfico
plt.figure()

# Cria um gráfico de dispersão usando as características 3 (petal length) e 4 (petal width) do dataset Iris
# c=y define as cores dos pontos com base nas classes (0, 1, 2), cmap usa o mapa de cores definido anteriormente
plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap, edgecolor='k', s=20)
plt.show()  # Exibe o gráfico

# Cria uma instância do classificador KNN com k=5
clf = KNN(k=5)

# Treina o classificador KNN com os dados de treino (X_train, y_train)
clf.fit(X_train, y_train)

# Faz previsões para os dados de teste (X_test)
predictions = clf.predict(X_test)

# Exibe as previsões para o conjunto de teste
print(predictions)

# Calcula a precisão do modelo comparando as previsões com os rótulos reais do conjunto de teste
acc = np.sum(predictions == y_test) / len(y_test)

# Exibe a acurácia do modelo (proporção de previsões corretas)
print(acc)
