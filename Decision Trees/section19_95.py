# Modules to import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# Iterative plot
matplotlib.use('Qt5Agg')

# Data
data = pd.read_csv('Data\\kyphosis.csv')
# data.head()
# data.info()
# sns.pairplot(data, hue='Kyphosis')
# plt.show()

# Training the model
X = data.drop('Kyphosis', axis=1)
y = data['Kyphosis']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.30)

# Decision tree
dtree = DecisionTreeClassifier()
dtree.fit(X_train, Y_train)

# Prediction
pred = dtree.predict(X_test)

# print(classification_report(Y_test, pred))
# print('\n')
# print(confusion_matrix(Y_test, pred))

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, Y_train)
rfc_pred = rfc.predict(X_test)

print(classification_report(Y_test, pred))
print('\n')
print(confusion_matrix(Y_test, pred))

print(classification_report(Y_test, rfc_pred))
print('\n')
print(confusion_matrix(Y_test, rfc_pred))