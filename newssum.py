import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
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
			if sentence not in sent2score.keys():
				sent2score[sentence] = word2count[word]
			else:
				sent2score[sentence] += word2count[word]


for sentence,score in sent2score.items():
	sent2score[sentence] = score/len(sentence)
					

sent2idx = {}
i=0
for sentence in sentences:
	sent2idx[sentence] = i
	i += 1
					
best_sentences = heapq.nlargest(5,sent2score,key = sent2score.get)

bestsent2idx = {}
for sentence in best_sentences:
	bestsent2idx[sentence] = sent2idx[sentence]

best_sentences = heapq.nsmallest(5,bestsent2idx,key = bestsent2idx.get)

summary = ""

for sentence in best_sentences:
	summary += str(sentence)

print('Article: ',article)
print('Summary: ',summary)			

			

	

	