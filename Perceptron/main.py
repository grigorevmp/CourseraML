import numpy as np
import pandas
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

data = pandas.read_csv('perceptron-train.csv', header=None, names=['a', 'b', 'c'])
data_test = pandas.read_csv('perceptron-test.csv', header=None, names=['a', 'b', 'c'])

y = []
for i in range(len(data)):
    y.append(data.a[i])
y = np.array(y)

x = np.zeros(shape=(len(data), 2))
for i in range(len(x)):
    x[i][0] = data.b[i]
    x[i][1] = data.c[i]
x = np.array(x)

clf = Perceptron(random_state=241)
clf.fit(x, y)
predictions = clf.predict(x)

data_test.columns = ['a', 'b', 'c']
y_test = []
for i in range(len(data_test)):
    y_test.append(data_test.a[i])
y_test = np.array(y_test)

x_test = np.zeros(shape=(len(data_test), 2))
for i in range(len(x_test)):
    x_test[i][0] = data_test.b[i]
    x_test[i][1] = data_test.c[i]
x_test = np.array(x_test)

predictions_test = clf.predict(x_test)

# Подсчёт ошибки
a1 = accuracy_score(y_test, predictions_test)
print("ошибка без нормализации: ", a1)

# нормализация
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x)
X_test_scaled = scaler.transform(x_test)

clf = Perceptron()
clf.fit(X_train_scaled, y)
predict_train = clf.predict(X_train_scaled)
predict_test = clf.predict(X_test_scaled)

# подсчёт ошибки после нормализации

a2 = accuracy_score(y_test, predict_test)
print("ошибка c нормализации: ", a2)
print()
print(round((a2 - a1), 3))
