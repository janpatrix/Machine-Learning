from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

data = np.asarray(pd.read_csv('/Users/patrick.gross/Development/MachineLearning/Lesson4/data/decision_tree_data.csv', header=None))
X = data[:,0:2]
y = data[:,2]
model = DecisionTreeClassifier(max_depth = 7, min_samples_leaf = 1)
model.fit(X, y)
y_pred = model.predict(X)

acc = accuracy_score(y, y_pred)
print(acc)