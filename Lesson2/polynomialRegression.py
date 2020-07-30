import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("/Users/patrick.gross/Development/MachineLearning/Lesson2/data/polynomial_data.csv")
X = data['Var_X'].values.reshape(-1, 1)
Y = data['Var_Y'].values


model = PolynomialFeatures(degree=4)
X_poly = model.fit_transform(X)

poly_model = LinearRegression(fit_intercept = False).fit(X_poly, Y)


