import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import re
import bs4 as bs
import os
import heapq
nltk.download('stopwords')

article = ""
with open(os.path.join("entertainment/001.txt"),encoding="utf-8") as f:
	for line in f:
		article += str(line)
		
article = re.sub(r'\[[0-9]*\]','',article)
article = re.sub(r'\s+',' ',article)

clean_article = re.sub(r'\W',' ',article)
clean_article = re.sub(r'\d',' ',clean_article)
clean_article = re.sub(r'\s+',' ',clean_article)


sentences = nltk.sent_tokenize(article)

stop_words = nltk.corpus.stopwords.words('english')

word2count = {}

for word in nltk.word_tokenize(clean_article):
	if word not in stop_words:
		if word not in word2count.keys():
			word2count[word] = 1
		else:
			word2count[word] += 1
			
for key in word2count.keys():
	word2count[key] = word2count[key]/max(word2count.values())
	
sent2score  = {}
for sentence in sentences:
	for word in nltk.word_tokenize(sentence.lower()):
		if word in word2count.keys():
			if len(sentence.split(' ')) < 25:
				if sentence not in sent2score.keys():
					sent2score[sentence] = word2count[word]
				else:
					sent2score[sentence] += word2count[word]
					
best_sentences = heapq.nlargest(3,sent2score,key = sent2score.get)

summary = ""

for sentence in best_sentences:
	summary += str(sentence)


				

			

	

	