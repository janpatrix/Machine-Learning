from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Lesson2/data/bmi_and_life_expectancy.csv")
model = LinearRegression()
model.fit(data[['BMI']], data[['Life expectancy']])

test = np.array(21.07931).reshape(1, -1)
print(model.predict(test))