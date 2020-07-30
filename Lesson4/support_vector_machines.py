from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

data = np.array(pd.read_csv('Lesson4/data/svm.csv', header=None))

X = data[:,0:2]
y = data[:,2]

print(y)

#C: The C parameter.
#kernel: The kernel. The most common ones are 'linear', 'poly', and 'rbf'.
#degree: If the kernel is polynomial, this is the maximum degree of the monomials in the kernel.
#gamma : If the kernel is rbf, this is the gamma parameter.

model = SVC(kernel='rbf', gamma=10)

model.fit(X, y)
y_pred = model.predict(X)
acc = accuracy_score(y, y_pred)
print(acc)