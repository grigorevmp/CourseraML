import pandas
import numpy as np
from sklearn.metrics import roc_auc_score
from scipy.spatial import distance

"Логистическая регрессия"

# Убедитесь, что выше выписаны правильные формулы для градиентного спуска.
# Обратите внимание, что мы используем полноценный градиентный спуск, а не его стохастический вариант!

def split(data):
    X = data.iloc[:, 1:].values
    y = data.iloc[:, 0].values
    return X, y


def sigmoid(X, w):
    return 1 / (1 + np.exp(-np.dot(X, w)))


def cost(X, y, w, C):
    sum = 0
    n = X.shape[0]
    m = X.shape[1]
    for i in range(n):
        sum += np.log(1 + np.exp(-y[i] * np.dot(X[i], w)))
    reg = C * (w ** 2).sum() / m
    cost = sum / np.double(n) + reg
    return cost

# Запустите градиентный спуск и доведите до сходимости
# (евклидово расстояние между векторами весов на соседних итерациях должно быть не больше 1e-5)


def train(X, y, k, C):
    n = X.shape[0]
    m = X.shape[1]
    w = np.zeros(m)
    c = cost(X, y, w, C)
    threshold = 1e-5
    for iteration in range(10000):
        new_w = np.zeros(m)
        for j in range(m):
            sum = 0
            for i in range(n):
                sum += y[i] * X[i, j] * (1 - 1 / (1 + np.exp(-y[i] * np.dot(X[i], w))))
            new_w[j] = w[j] + k * sum / np.double(n) - k * C * w[j]
        new_cost = cost(X, y, new_w, C)
        if distance.euclidean(w, new_w) <= threshold:
            return new_w
        c = new_cost
        w = new_w
    return w


# Загрузите данные из файла data-logistic.csv.
# Это двумерная выборка, целевая переменная на которой принимает значения -1 или 1.

data = pandas.read_csv('data-logistic.csv', header=None)
X, y = split(data)
k = 0.1

# Реализуйте градиентный спуск для обычной и L2-регуляризованной
# (с коэффициентом регуляризации 10) логистической регрессии.

score = roc_auc_score(y, sigmoid(X, train(X, y, k, C=0)))
score_reg = roc_auc_score(y, sigmoid(X, train(X, y, k, C=10)))

# Какое значение принимает AUC-ROC на обучении без регуляризации и при ее использовании?

with open("q1.txt", "w") as output:
    output.write('%.3f %.3f' % (score, score_reg))
