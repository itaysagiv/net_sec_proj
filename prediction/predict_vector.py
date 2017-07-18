
#TO DO
#change so the file name is hardcoded and only algorithm is argv **
#change params in main **
#add more algorithms, and change to be like the return value of model_selection
#add generity to vector size - 2D train_set_values **
#replace to use timing function **
#count and most_common in one function **
#print results to file **


from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import explained_variance_score
import sys
import pandas
from numpy import genfromtxt
from sklearn import model_selection
from collections import Counter
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import fbeta_score
from sklearn.linear_model import RidgeClassifier
import numpy as np
'''
predict where train is the the output of wireshark_from_pcap.py csv
first parameter- train csv filr path (output of wireshark_from_pcap.py
probably will be saved in the project folder)
second parameter- algorythm to use,option:rf,bost,knn,Etree,lda,Etrees,k-means
thirs parameter- test csv path (output of wireshark_test_from_pcap.py)
'''
predict_vector=''

def one_interval_decision(interval,predictions,X_test):
	result_count=[0]
	global predict_vector 
	for i in range(len(predictions)):
		index=int(float(X_test[i, 3]))/5
	   	if index == interval: 
			result_count.append(predictions[i]) 
	x = Counter(result_count)
	ans= int(x.most_common(1)[0][0])
	predict_vector+= str(ans)
	predict_vector+= ','	



if __name__ == "__main__":
	train_path=sys.argv[1]
	algorithrm=sys.argv[2]
	test_path=sys.argv[3]
	vector = map(int, sys.argv[4].split(','))
	row = 5 # number of rows means number of features 
#load data
train_set = pandas.read_csv(train_path)  # the data from offline measurments
test_set = pandas.read_csv(test_path)  # , names=namesTrain

# Split-out validation train_set
seed = 7 
split=abs(1-float(float(len(test_set))/float(len(train_set))))
split=round(split, 10) 
train_set,test = train_test_split(train_set, test_size = split)
train_set_values = train_set.values
# train_set_values=transformed_values
for i in range(1, len(train_set_values) - 1):
   train_set_values[i].astype(float)
#train_set_values = list(map(int, train_set_values))

X = train_set_values[:, 0:row - 1]
Y = train_set_values[:, row - 1]

test_set_values = test_set.values
# train_set_values=transformed_values
for i in range(1, len(train_set_values) - 1):
   train_set_values[i].astype(float)
#train_set_values = list(map(int, train_set_values))



# Make predictions on validation train_set
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
			min_samples_leaf=1, min_samples_split=2,
			min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=2,
			warm_start=False)
algorithrm='rf'
if algorithrm=='rf':
	#predicter= RandomForestClassifier()
	predicter=RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
			min_samples_leaf=1, min_samples_split=2,
			min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=2,
			warm_start=False)
algorithrm='Ridge'	
if algorithrm=='bost':
	predicter=AdaBoostClassifier()
if algorithrm=='RF':
	predictor=RandomForestClassifier(n_estimators=10)
if algorithrm=='knn':
	predicter=KNeighborsClassifier() # so far knn wins
if algorithrm=='Etree':
	predicter=DecisionTreeClassifier()
if algorithrm=='lda':
	predicter=LinearDiscriminantAnalysis()
if algorithrm=='Etrees':
	predicter =ExtraTreesClassifier(max_depth=None, min_samples_split=2, random_state=0)
if algorithrm=='Ridge':
	RidgeClassifier(tol=1e-2, solver="lsqr")
predicter.fit(X, Y)

X_test = test_set_values[:, 0:row - 1]

predictions = predicter.predict(X_test)

#accuracy measurments for future 
#print ("accuracy_score")
#print(accuracy_score(Y, predictions))
#print ("classification_report")
#print(classification_report(Y, predictions))
#print ("mean_squared_error")
#print (mean_squared_error(Y, predictions)) 



for i in range(len(vector)):
	one_interval_decision(i,predictions,X_test)
global predict_vector 
print  predict_vector  #presnted to the screen and to file
f = open("gussed_vector.txt", "w")
f.writelines( predict_vector )
f.close()





