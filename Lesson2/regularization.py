import pandas as pd
from sklearn.linear_model import Lasso
import numpy as np

data = pd.read_csv("/Users/patrick.gross/Development/MachineLearning/Lesson2/data/lasso_data.csv", header=None)

X = np.array(data)[:, :6]
y = np.array(data)[:, 6:]

lasso_reg = Lasso()
lasso_reg.fit(X, y)

reg_coef = lasso_reg.coef_
print(reg_coef)