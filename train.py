import sys
import re
from nltk.corpus import stopwords
import string
import operator
import random
from sklearn import svm
from nltk.stem import *
import pickle
from sklearn.externals import joblib
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.cross_validation import ShuffleSplit
import numpy as np
from sklearn.metrics import *
from nltk.stem.porter import *
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from nltk.stem.snowball import SnowballStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
#reload(sys)  
#sys.setdefaultencoding('utf-8')
import nltk



#filter(lambda a: a not in ['not','no','none'],stopwords.words('english'))
vectorizer = TfidfVectorizer(stop_words=None,decode_error='ignore',min_df=5, max_df = 0.8,use_idf=True,ngram_range=(1,3),norm='l2')
#vectorizer = CountVectorizer(stop_words=None,decode_error='ignore',min_df=5, max_df = 0.8,ngram_range=(1,3),binary=True)
#vectorizer=TfidfVectorizer(decode_error='ignore',ngram_range=(1,2),use_idf=True,norm='l2')
#train_vectors = vectorizer.fit_transform(train_data)
f=open(str(sys.argv[1]))## Tweet file
g=open(str(sys.argv[2]))## labels file 
#vectorizer = HashingVectorizer(stop_words='english', decode_error='ignore',binary=True,analyzer=tok)
x=vectorizer.fit_transform(f)
y=np.array([int(lines) for lines in g])
f.close()
g.close()
cross=ShuffleSplit(x.shape[0],n_iter=10,test_size=0.2)
#svm_train=LogisticRegression(penalty='l2',solver='sag',n_jobs=10)
svm_train=svm.LinearSVC(loss='hinge')
#svm_train=RandomForestClassifier(n_estimators=10, criterion='entropy',n_jobs=20)
#svm_train=MultinomialNB()
for s,t in cross:
	print "Training"
	svm_train.fit(x[s],y[s])
	joblib.dump(svm_train,'binary_lin.pkl')
	print" Predicting"
	pred = svm_train.predict(x[t])
	print "Confusion Matrix"
	score = confusion_matrix(y[t], pred)
	print score
	print "F1 Score"
	score=f1_score(y[t],pred,pos_label=4)
	print score
	print "Accuracy"
	score=accuracy_score(y[t],pred)
#	for i in xrange(len(t)):
#		if y[t[i]]!=pred[i]:
#			print t[i]
	print score
