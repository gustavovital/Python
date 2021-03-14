"""
Simple Support Vector Machine (SVM) example with character recognition
Author: pythonprogramming
Date: 13/03/2021

Simple Support Vector Machine (SVM) example with character recognition - first example of the
module sklearn

"""

# Modules
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

# Dataset
digits = datasets.load_digits()
# print(digits.data)
# print(digits.images)

clf = svm.SVC(gamma=0.0001, C=100)
x, y = digits.data[:-1], digits.target[:-1]
# print(len(digits.data))
clf.fit(x, y)

# print('Prediction:', clf.predict(digits.data[-1]))

count = 0
fig, axs = plt.subplots(2, 5)
for i in range(2):
    for j in range(5):
        print(i,j)
        axs[i,j].imshow(digits.images[count], cmap=plt.cm.gray_r, interpolation='nearest')
        count += 1
plt.show()