#!/usr/bin/env python

#takes the csv test file created by wirshar_test_from_pcap
#performs many statistics tests on the data - retuns all the cross-validations results

import sys
from numpy import genfromtxt
import numpy
# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
from sklearn.decomposition import FactorAnalysis
from sklearn.svm import NuSVC
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.svm import SVR
from  sklearn.linear_model import LinearRegression
# from sklearn.p
# from matplotlib.mlab import PCA
from sklearn.linear_model import Perceptron
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import Imputer
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
'''
this code is simply evaluate 
of clasification based on only train test(split from train to test and train)
the closer to 1 the better the prediction
take as parameter validation size the size of the train to split(for example 0.3 means 
0.3 of the data to test and 0.7 to train)
'''

if __name__ == "__main__":
	params=len(sys.argv)
	validation_size = 0.3
	if params>1:
		validation_size = sys.argv[1]
	# Load dataset
	url ='/root/PycharmProjects/security/data_sniff_from_pcap_wireshark.csv'
	#url = '/root/PycharmProjects/security/test_pcap.csv'

	names = ['udp_Length', 'total_length', 'pkt_number', 'time_from_last_packet',
				  'time_since_first_packet', 'decision']
	colsRes = ['decision']
	namesTrain = ['udp_Length', 'total_length', 'pkt_number', 'time_from_last_packet',
				  'time_since_first_packet']

	dataset = pandas.read_csv(url)  # the data from offline measurments
	sampleNumber = 5
	# Split-out validation dataset
	array = dataset.values
	# array=transformed_values
	row=5
	for i in range(1, len(array) - 1):
		array[i].astype(float)
	X = array[:, 0:row - 1]
	Y = array[:, row - 1]
	#  print X
	# print Y
	seed = 7
	X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
																					random_state=seed)
	# Test options and evaluation metric
	seed = 7
	scoring = 'accuracy'
	#  Check Algorithms
	models = []
	models.append(('LR', LogisticRegression()))
	models.append(('Ridge', RidgeClassifier(tol=1e-2, solver="lsqr")))
	models.append(('Perceptron', Perceptron(n_iter=50)))
	models.append(('PASAG', PassiveAggressiveClassifier(n_iter=50)))
	#models.append(('LDA', LinearDiscriminantAnalysis()))
	models.append(('KNN', KNeighborsClassifier()))
	models.append(('CART', DecisionTreeClassifier()))
	models.append(('NB', GaussianNB()))
	models.append(('lr', LinearRegression()))
	#models.append(('SVM', SVC(kernel="rbf")))
	models.append(('RF', RandomForestClassifier(n_estimators=10)))
	#models.append(('GB', GradientBoostingClassifier()))
	models.append(('Boost', AdaBoostClassifier()))
	# models.append(("Quadratic",QuadraticDiscriminantAnalysis()))
	#models.append(("SGD", SGDClassifier()))
	models.append(("Tree", DecisionTreeClassifier()))
	models.append(("ETrees", ExtraTreesClassifier(max_depth=None, min_samples_split=2, random_state=0)))
	models.append(('LinearSVC', LinearSVC(random_state=0)))
	# evaluate each model in turn
	results = []
	names = []
	for name, model in models:
		kfold = model_selection.KFold(n_splits=10, random_state=seed)
		cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
		results.append(cv_results)
		names.append(name)
		msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
		print(msg)
	# Compare Algorithms
