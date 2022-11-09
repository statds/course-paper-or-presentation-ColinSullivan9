import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import stats

lst = []
with open("NBA_Combined.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        lst.append(row)



# print(x)
# print(y)

def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def plot_regression_line(x, y, b, stat):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

	# putting labels
	plt.title(stat)
	plt.xlabel('x')
	plt.ylabel('y')

	# function to show plot
	plt.show()

def main(x, y, stat):
	# observations / data

	# estimating coefficients
	b = estimate_coef(x, y)
# 	print("Estimated coefficients:\nb_0 = {} \
# 		\nb_1 = {}".format(b[0], b[1]))

	# plotting regression line
	plot_regression_line(x, y, b, stat)

header = lst[0]
# print(header)
x = np.array([0])
y = np.array([0])
for stat in header[9:]:
    ind = header.index(stat)
    x = []
    y = []
    for player in lst[1:]:
#     if type(player[0]) is int:
        x = np.append(x, float(player[0]))
#     print(player[14])
#         print(player[ind])
        y = np.append(y, float(player[ind]))
        
    main(x, y, stat)
#     print(y)
    res = stats.linregress(x, y)
    print(stat + ": " + f"R-squared: {res.rvalue**2:.6f}")
# main(x, y)

# res = stats.linregress(x, y)
# print(f"R-squared: {res.rvalue**2:.6f}")
