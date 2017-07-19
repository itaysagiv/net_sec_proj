import sys
import numpy as np
import os

def time(line):
	return float(line.split(",")[0].translate(None,'"'))
def val(line,i):
	return int(line.split(",")[i].translate(None,'"'))
def get_avg(data,g,start):
	data[int(start*10):]
	acc=0
	cnt=0
	for elem in data:
		if val(elem,g):
			acc=acc+val(elem,g)
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
			hit_vec.append(str(vector[i]))
			hit_res=hit_res+1
		else:
			hit_vec.append(str(result[i])+'*')
	return int(100*(hit_res/36.0))

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

def naiv_check(test,g,start,th,eps):
	test1 = test[int(start*10):]
	res=[]
	for i in range(0,len(test1)-50,50):
		s=0
		for j in range(50):
			s=s+val(test1[i+j],g)
		res.append(s/50)
	ret=[]
	for r in res:
		if (th*(1-eps))<r<(th*(1+eps)):
			ret.append(1)
		else:
			ret.append(0)
	return ret
	
	
vector = map(int, "1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1".split(','))

with open(sys.argv[1],"r") as f:
	train = f.readlines()
	train = train[1:-1]
with open(sys.argv[2],"r") as f:
	test = f.readlines()
	test = test[1:-1]
if len(sys.argv)>3:
	start = float(sys.argv[3])
else:
	start=0

max_ = 0,0,0
for e1 in np.arange(0.2,0.8,0.01):
	os.system('clear')
	print >> sys.stderr, 'analyzing %d%%' % int(((e1-0.2)/0.6)*100)
	ans1 = naiv_check(test,1,start,get_avg(train,1,start),e1)[:36]
	for e2 in np.arange(0.2,0.8,0.01):
		ans2 = naiv_check(test,2,start,get_avg(train,2,start),e2)[:36]
		c=0
		for i in range(0,len(ans1)):
			if ans1[i]==ans2[i]:
				c=c+1
		if max_[0]<c:
			max_=c,e1,e2
print max_

res1 = naiv_check(test,1,start,get_avg(train,1,start),max_[1])[:36]
res2 = naiv_check(test,2,start,get_avg(train,2,start),max_[2])[:36]
vec=[]
for i in range(0,36):
	try:
		if res1[i]==res2[i]:
			vec.append(res1[i])
		else:
			vec.append('?')
	except IndexError:
		print 'Incomplete vector'
		break
print res1
print res2
print vec
print vector
