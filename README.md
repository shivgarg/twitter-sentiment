#Twiiter Sentiment Analysis

Twiiter Sentiment analysis tool written in Python using Scikit for running the machine learning models. The sentiment considered here is binary (0 or 4). 0 meaning negative sentiment of tweet and 4 meaning positive sentiment of tweet. 

sklearn package should be installed and path variable should be confgiured correctly so that the 
## Repo Structure
1. add_features.py :- It parses the raw data file and cleans the data and add feaures to each tweet. It outputs a clean file which can be used to train a scikit model. 
2. train.py :- This uses the cleaned up file and trains the scikit model. The experiments with various models can be run in this file by changing the models. It dumps the model in the models folder alongwith the vectorizer which acts the dictionary for the model.
3. test.py :- This file takes unlabelled data and outputs sentiment labels. 
4. data:- folder contained the orginal data set plus the cleaned up datset.
5. model :- Contains the learnt model.
6. vector.zip :- Containes the vectorizer outputed by the tf-idf vectorizewr of scikit.
7. misc :- Some miscellaneous files used for developing the features.

## Running the Code.
1. python add_features.py <tweet_file>.
	It would output a <tweet_file>_twt file.
2. python train.py <cleaned tweet file> <label file for each tweet>
3. python test.py <cleaned twee file> <output file name>
It gives out the sentiment labels in output file.



