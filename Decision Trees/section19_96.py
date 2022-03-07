
# Modules
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# Data
data = pd.read_csv('Data\\loan_data.csv')
# data.head()
# data.info()
# data.describe()

# Analise
data[data['credit.policy']==1]['fico'].hist(alpha=0.5, color='blue', bins=30, label='Credit Policy = 1')
data[data['credit.policy']==0]['fico'].hist(alpha=0.5, color='red', bins=30, label='Credit Policy = 0')

plt.legend()
plt.show()

data[data['not.fully.paid']==1]['fico'].hist(alpha=0.5, color='green', bins=30, label='not fully paid = 1')
data[data['not.fully.paid']==0]['fico'].hist(alpha=0.5, color='yellow', bins=30, label='not fully paid = 0')

plt.legend()
plt.show()

sns.countplot(x='purpose', hue='not.fully.paid', data=data, palette='Set1')
sns.jointplot(x='fico', y='int.rate', data=data, color='purple')

sns.lmplot(y='int.rate', x='fico', data=data, hue='credit.policy', col='not.fully.paid',palette='Set1')

# Decision tree
final_data = pd.get_dummies(data, columns=['purpose'], drop_first=True)
# final_data.info()

X = final_data.drop('not.fully.paid', axis=1)
y = final_data['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

prediction = dtree.predict(X_test)
print(classification_report(y_test, prediction))
print(confusion_matrix(y_test, prediction))

rfc = RandomForestClassifier(n_estimators=600)
rfc.fit(X_train, y_train)

predictions = rfc.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
