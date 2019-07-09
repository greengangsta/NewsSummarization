import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import spacy
import re
import bs4 as bs
import urllib.request
import os
import heapq

nltk.download('stopwords')


# Code for scraping an article from a webpage
"""

source = urllib.request.urlopen('https://www.bbc.com/news/world-asia-india-48705022').read()
soup = bs.BeautifulSoup(source)
text = ""
for paragraph in soup.find_all('p'):
	text += paragraph.text
	
"""


article = ""
with open(os.path.join("articles/entertainment_a/001.txt"),encoding="utf-8") as f:
	for line in f:
		article += str(line)
		
article = re.sub(r'\[[0-9]*\]','',article)
article = re.sub(r'\s+',' ',article)

clean_article = re.sub(r'\W',' ',article)
clean_article = re.sub(r'\d',' ',clean_article)
clean_article = re.sub(r'\s+',' ',clean_article)

spacy_nlp = spacy.load('en_core_web_sm')
document = spacy_nlp(article)

print(type(document))

entities = ""
for element in document.ents:
	print('Type: %s, Value: %s' % (element.label_, element))
	entities += str(element) + " "

stop_words = nltk.corpus.stopwords.words('english')
	
ner = []
for entity in nltk.word_tokenize(entities):
	if entity not in stop_words:
		ner.append(entity.lower())


sentences = nltk.sent_tokenize(article)	

"""
sent2score  = {}
for sentence in sentences:
	for word in nltk.word_tokenize(sentence.lower()):
		if word in ner:
			if len(sentence.split(' ')) < 25:
				if sentence not in sent2score.keys():
					sent2score[sentence] = 1
				else:
					sent2score[sentence] += 1
					
"""
	
sent2score2  = {}
for sentence in sentences:
	for word in nltk.word_tokenize(sentence.lower()):
		if word in ner:
			if sentence not in sent2score2.keys():
				sent2score2[sentence] = 1
			else:
				sent2score2[sentence] += 1

for sentence,score in sent2score2.items():
	sent2score2[sentence] = score/len(sentence)

sent2idx = {}
i=0
for sentence in sentences:
	sent2idx[sentence] = i
	i += 1
	 

best_sentences = heapq.nlargest(5,sent2score2,key = sent2score.get)

bestsent2idx = {}
for sentence in best_sentences:
	bestsent2idx[sentence] = sent2idx[sentence]


best_sentences = heapq.nsmallest(5,bestsent2idx,key = bestsent2idx.get)

summary = ""

for sentence in best_sentences:
	summary += str(sentence)


				

			

	

	