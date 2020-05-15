import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

data = pd.read_csv('/Users/patrick.gross/Development/MachineLearning/Lesson2/data/absoluteError.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)

w1 = 0
w2 = 0

learning_rate = 0.1
#iterations
epochs = 25

#number if elements in X
n = float(len(X))

#Performing Gradient Decent
for i in range(epochs):
    Y_pred = w1*X + w2
    D_w1 = (-2/n) * sum(X*(Y - Y_pred))
    D_w2= (-2/n) * sum(Y - Y_pred)
    w1 = w1 - learning_rate * D_w1
    w2 = w2 - learning_rate * D_w2
    plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line

plt.show()

#Making Predictions
Y_pred = w1 * X + w2

plt.scatter(X, Y) 
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
plt.show()

