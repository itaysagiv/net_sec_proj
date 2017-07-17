
#TO DO
#change so the file name is hardcoded and only algorithm is argv
#change params in main
#add more algorithms, and change to be like the return value of model_selection
#add generity to vector size - 2D array
#replace to use timing function
#count and most_common in one function
#print results to file


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

'''
predict where train is the the output of wireshark_from_pcap.py csv
first parameter- train csv filr path (output of wireshark_from_pcap.py
probably will be saved in the project folder)
second parameter- algorythm to use,option:rf,bost,knn,Etree,lda,Etrees,k-means
thirs parameter- test csv path (output of wireshark_test_from_pcap.py)
'''

if __name__ == "__main__":
	params =len(sys.argv)'
	if params>1:
		file_path=sys.argv[1]
	if params>2:
		algorithrm=sys.argv[2]
	if params > 3:
		testpath=sys.argv[3]
#load data


dataset = pandas.read_csv(file_path)  # the data from offline measurments
test_observed = pandas.read_csv(testpath)  # , names=namesTrain
row = 5
# Split-out validation dataset
seed = 7
split=float(1-float(len(dataset))/float(len(test_observed)))
split=round(split, 5) 
test_observed, test = train_test_split(test_observed, test_size = split)
array = dataset.values
# array=transformed_values
for i in range(1, len(array) - 1):
   array[i].astype(float)
#array = list(map(int, array))

X = array[:, 0:row - 1]
Y = array[:, row - 1]

array = test_observed.values
# array=transformed_values
for i in range(1, len(array) - 1):
   array[i].astype(float)
#array = list(map(int, array))

X_test = array[:, 0:row - 1]
Y_test = array[:, row - 1]

#12803 in first vector


# Make predictions on validation dataset
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
			min_samples_leaf=1, min_samples_split=2,
			min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=2,
			warm_start=False)

if algorithrm=='rf':
	predicter= RandomForestClassifier()
if algorithrm=='bost':
	predicter=AdaBoostClassifier()
if algorithrm=='knn':
	predicter=KNeighborsClassifier() # so far knn wins
if algorithrm=='Etree':
	predicter=DecisionTreeClassifier()
if algorithrm=='lda':
	predicter=LinearDiscriminantAnalysis()
if algorithrm=='Etrees':
	predicter =ExtraTreesClassifier(max_depth=None, min_samples_split=2, random_state=0)
if algorithrm=='k-means':
	predicter=KMeans()
predicter.fit(X, Y)
predictions = predicter.predict(X_test)

print ("accuracy_score")
print(accuracy_score(Y, predictions))
#print ("classification_report")
#print(classification_report(Y, predictions))
print ("mean_squared_error")
print (mean_squared_error(Y, predictions))




X_test = array[:, 0:row - 1]

predictions = predicter.predict(X_test)
entry_1 = []
entry_2 = []
entry_3 = []
entry_4 = []
entry_5 = []
entry_6 = []
entry_7 = []
entry_8 = []
entry_9 = []
entry_10 = []
entry_11 = []
entry_12 = []
entry_13 = []
entry_14 = []
entry_15 = []
entry_16 = []
entry_17 = []
entry_18 = []
entry_19 = []
entry_20 = []
entry_21 = []
for i in range(len(predictions)):
	#print X_test[i, 3]
	#print predictions[i]
	time=float(X_test[i, 3])
	#print time
	vector = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
	if 0.0 <= time < 5.0:
		entry_1.append(predictions[i])
	elif 5.0 <= time < 10.0:
		entry_2.append(predictions[i])
	elif 10.0 <= time < 15.0:
		entry_3.append(predictions[i])
	elif 15.0 <= time < 20.0:
		entry_4.append(predictions[i])
	elif 20.0 <= time < 25.0:
		entry_5.append(predictions[i])
	elif 25.0 <= time < 30.0:
		entry_6.append(predictions[i])
	elif 30.0 <= time < 35.0:
		entry_7.append(predictions[i])
	elif 35.0 <= time < 40.0:
		entry_8.append(predictions[i])
	elif 40.0 <= time < 45.0:
		entry_9.append(predictions[i])
	elif 45.0 <= time < 50.0:
		entry_10.append(predictions[i])
	elif 50.0 <= time < 55.0:
		entry_11.append(predictions[i])
	elif 55.0 <= time < 60.0:
		entry_12.append(predictions[i])
	elif 60.0 <= time < 65.0:
		entry_13.append(predictions[i])
	elif 65.0 <= time < 70.0:
		entry_14.append(predictions[i])
	elif 70.0 <= time < 75.0:
		entry_15.append(predictions[i])

#print entry_2[5]
#print type(entry_1)

x = Counter(entry_1)
ans1= int(x.most_common(1)[0][0])
x = Counter(entry_2)
ans2= int(x.most_common(1)[0][0])
x = Counter(entry_3)
ans3= int(x.most_common(1)[0][0])
x = Counter(entry_4)
ans4= int(x.most_common(1)[0][0])
x = Counter(entry_5)
ans5= int(x.most_common(1)[0][0])
x = Counter(entry_6)
ans6= int(x.most_common(1)[0][0])
x = Counter(entry_7)
ans7= int(x.most_common(1)[0][0])
x = Counter(entry_8)
ans8= int(x.most_common(1)[0][0])
x = Counter(entry_9)
ans9= int(x.most_common(1)[0][0])
x = Counter(entry_10)
ans10= int(x.most_common(1)[0][0])
x = Counter(entry_11)
ans11= int(x.most_common(1)[0][0])
x = Counter(entry_12)
ans12= int(x.most_common(1)[0][0])
x = Counter(entry_13)
ans13= int(x.most_common(1)[0][0])
x = Counter(entry_14)
ans14= int(x.most_common(1)[0][0])
x = Counter(entry_15)
ans15= int(x.most_common(1)[0][0])
print 'guess vector'
print (ans1,ans2,ans3,ans4,ans5,ans6,ans7
	   ,ans8,ans9,ans10,ans11,ans12,ans13,ans14,ans15)
previous_vector = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
new_vector=[0,1,1,0,0,1,1,1,0,0,0,1,1,1,0]
print 'original vector'
print new_vector

