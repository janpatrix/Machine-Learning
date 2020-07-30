import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
import numpy as np

data = pd.read_csv("Lesson2/data/lasso_standardization.csv", header = None)

X = np.array(data)[:, :6]
y = np.array(data)[:, 6:]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X, y)

lasso_reg = Lasso()
lasso_reg.fit(X_scaled, y)

reg_coef = lasso_reg.coef_
