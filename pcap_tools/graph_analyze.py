#TO DO
#change the way it detects the starting point
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
def confirm(vector,result):
	hit_vec=[]
	hit_res=0
	for i in range(0,36):
		if vector[i]==result[i]:
			hit_vec.append('H')
			hit_res=hit_res+1
		else:
			hit_vec.append('M')
	return hit_vec,int(100*(hit_res/36.0))
def check_intervals(train,test):
	train_avg = get_avg(train)
	res = time(test[1])-time(test[0])
	start = next(test.index(elem) for elem in test if val(elem)>train_avg)
	test = test[start:]
	predict=[]
	for chunk in chunks(test,int(5/res)):
		predict.append(get_avg(chunk))
	result=[]
	for avg in predict:
		if avg>train_avg:
			result.append(1)
		else:
			result.append(0)
	return result[:36]
def search_peeks(test,train,start):
	train_avg = get_avg(train)
	TH=5
	res=[]
	for elem in test:
		ind = test.index(elem)
		if ind>TH and val(elem)>train_avg:
			s=0
			for i in range(1,TH):
				s=s+val(test[ind-i])
			av=float(s)/TH
			if val(elem) > 5*av:
				res.append(time(elem))
	res = map(lambda x: x-start,res)
	ans= [0]*36
	for r in res:
		ans[int(r)/5]=1
	return ans
def naiv_check(test,start,th):
	test = test[int(start*10):]
	res=[]
	for i in range(0,len(test)-50,50):
		s=0
		for j in range(50):
			s=s+val(test[i+j])
		res.append(s/50)
	ret=[]
	for r in res:
		if r>th:
			ret.append(1)
		else:
			ret.append(0)
	return ret
	
	
vector = map(int, "1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0".split(','))
TH = 0.5

with open(sys.argv[1],"r") as f:
	train = f.readlines()
	train = train[1:-1]
with open(sys.argv[2],"r") as f:
	test = f.readlines()
	test = test[1:-1]
print get_avg(train)*0.6
res=[0]*4
res[0] = check_intervals(train,test)
res[1] = search_peeks(test,train,4.5)
res[2] = [0]*36
for i in range(35):
	if res[1][i]:
		res[2][i]=1
	else:
		res[2][i]=res[0][i]
res[3]=naiv_check(test,4.5,30)
for r in res:
	conf = confirm(vector,r)
	print conf[0]
	print >>sys.stderr, 'hit ratio %d%%' % int(conf[1])
