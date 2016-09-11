import pickle
f=open('inquirerbasic.csv')

f.readline()
polarity={}
for lines in f:
	lines=lines.split(',')
	if lines[1]!='' :
		a=lines[0].lower()
		if a.find('#')==-1:
			polarity[a]=lines[1]
		else:
			polarity[a[:a.find('#')]]=lines[1]

p=open('polarity.pickle','wb')
pickle.dump(polarity, p)
p.close()
p=open('polarity.pickle','r')
l=pickle.load(p)
print polarity
print polarity==l
