#TO DO
#change the way it detects the  starting point
#add more crotirior to the decision
#maby devide each cunck to n sections and base the decision on the majority in the chunk

import sys

def time(line):
	return float(line.split(",")[0].translate(None,'"'))
def val(line):
	return int(line.split(",")[1].translate(None,'"'))
def get_avg(data):
	acc=0
	cnt=0
	for elem in data:
		if val(elem):
			acc=acc+val(elem)
			cnt=cnt+1
	if cnt:
		return acc/cnt
	else:
		return 0
def chunks(l, n):
	new=[]
	for i in range(0, len(l), n):
		new.append(l[i:i + n])
	return new

vector = map(int, "1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0".split(','))
TH = 0.5

with open(sys.argv[1],"r") as f:
	train = f.readlines()
	train = train[1:-1]
with open(sys.argv[2],"r") as f:
	test = f.readlines()
	test = test[1:-1]

train_avg = get_avg(train)
res = time(test[1])-time(test[0])
start = next(test.index(elem) for elem in test if val(elem)>train_avg)
print start
#start = int(round(start_time/(5/res)))
print train_avg,5/res, len(test)/36, len(train)/36

test = test[start:]

predict=[]
for chunk in chunks(test,int(5/res)):
	predict.append(get_avg(chunk))
result=[]
for avg in predict:
	if avg>TH*train_avg:
		result.append(1)
	else:
		result.append(0)


print predict
print result
print vector
hit_vec=[]
hit_res=0
for i in range(0,36):
	if vector[i]==result[i]:
		hit_vec.append('H')
		hit_res=hit_res+1
	else:
		hit_vec.append('M')
print hit_vec
print >> sys.stderr, 'hit retio of %d%%' % int(100*(hit_res/36.0))

