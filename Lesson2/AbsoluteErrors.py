import math

#Compute the mean absolute error for the following line and points:
#line: y = 1.2x + 2
#points: (2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)

points = [(2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)]
error = 0.0
length = len(points)
def calc_error(x,y):
    y_hat =  1.2*x + 2
    error = y - y_hat
    return abs(error)

for point in points:
    error += calc_error(point[0], point[1])

print("Absolute Mean Error: %s" %(error/length))
    
#Compute the mean squared error for the following line and points:
#line: y = 1.2x + 2
#points: (2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)

points = [(2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)]
error = 0.0
length = len(points)
def calc_error(x,y):
    y_hat =  1.2*x + 2
    error = (y - y_hat)**2
    return error

for point in points:
    error += calc_error(point[0], point[1])

print("Absolute Squared Error: %s" %(error/(2*length)))