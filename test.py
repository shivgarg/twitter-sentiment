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
import nltk
import cPickle


with open('model/vector/vector.pkl','r') as v:
	vectorizer = cPickle.load(v)
f=open(str(sys.argv[1])+'_twt')
g=open(str(sys.argv[2]),'w') ## Output File for labels
x=vectorizer.transform(f)
f.close()
with open('model/binary_lin.pkl','r') as v:
	svm_train=cPickle.load(v)
pred = svm_train.predict(x)
for a in pred:
	g.write(str(a)+'\n')
g.close()
