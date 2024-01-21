import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score

# Загрузка набора данных
heart_data = pd.read_csv('heart.csv')

# Проверка данных
# print(heart_data.hist())
# print(heart_data.head())
# heart_data.tail()
# heart_data.shape
# heart_data.info()
heart_data.isnull().sum()
heart_data.describe()
heart_data['target'].value_counts()

# Разделение данных на входные и целевые переменные
X = heart_data.drop(columns='target', axis=1).values
Y = heart_data['target']

# Разделение данных на обучающие и тестовые наборы
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Обучение модели
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Оценка модели на обучающих данных
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
training_data_f1_score = f1_score(Y_train, X_train_prediction)

# Оценка модели на тестовых данных
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
test_data_f1_score = f1_score(Y_test, X_test_prediction)

# Cross-Validation
cv_scores = cross_val_score(model, X, Y, cv=5)
mean_cv_score = np.mean(cv_scores)
std_cv_score = np.std(cv_scores)

# Сделать прогноз
# input_data = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1)
# input_data_as_numpy_array = np.asarray(input_data)
# input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
# prediction = model.predict(input_data_reshaped)
# print(prediction)
# if (prediction[0]== 0):
#   print('The Person does not have a Heart Disease')
# else:
#   print('The Person has Heart Disease')

print('Точность данных обучения: ', training_data_accuracy)
print('Оценка F1 по тренировочным данным: ', training_data_f1_score)
print('Точность тестовых данных: ', test_data_accuracy)
print('Оценка F1 по тестовым данным: ', test_data_f1_score)
print('Средний балл перекрестной проверки:', mean_cv_score)
print('Стандартное отклонение перекрестной проверки:', std_cv_score)
