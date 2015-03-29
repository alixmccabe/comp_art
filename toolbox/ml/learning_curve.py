""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
num_trials = 10
train_percentages = range(5,95,5)

# train a model with training percentages between 5 and 90 (see train_percentages) and evaluate
# the resultant accuracy.
# You should repeat each training percentage num_trials times to smooth out variability
# for consistency with the previous example use model = LogisticRegression(C=10**-10) for your learner

def get_plots(data):
	
	averages = []

	for i in range(5,95,5):
		counter = 0
		test = []

		while counter <= 10:
			counter += 1

			test_accuracies = numpy.zeros(len(train_percentages))
			X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=i*0.01)
			model = LogisticRegression(C=10**-10)
			model.fit(X_train, y_train)

			test.append(float("%f" %model.score(X_test,y_test)))

		averages.append(sum(test)/len(test))

	return averages

fig = plt.figure()
plt.plot(range(5,95,5),get_plots(data))
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()
