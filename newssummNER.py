# Importing the libraries
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

# Downloading the stopword to remove words like(the , this ..)
nltk.download('stopwords')


# Code for scraping an article from a webpage
"""

source = urllib.request.urlopen('https://www.bbc.com/news/world-asia-india-48705022').read()
soup = bs.BeautifulSoup(source)
text = ""
for paragraph in soup.find_all('p'):
	text += paragraph.text
	
"""

# Loading an article from a text file located on the local disk
article = ""
with open(os.path.join("articles/entertainment_a/001.txt"),encoding="utf-8") as f:
	for line in f:
		article += str(line) # article contains all the sentences of the corresponding text files.
		

#Cleaning the article using regular expression
article = re.sub(r'\[[0-9]*\]','',article) # 
article = re.sub(r'\s+',' ',article)
clean_article = re.sub(r'\W',' ',article)
clean_article = re.sub(r'\d',' ',clean_article)
clean_article = re.sub(r'\s+',' ',clean_article)

# Performing NER(Named Entity Recognition) using the spacy library to find the words which are named entities like places, names, organizations etc in the article
spacy_nlp = spacy.load('en_core_web_sm')
document = spacy_nlp(article)

print(type(document))

# Getting the named entities words
entities = ""
for element in document.ents:
	print('Type: %s, Value: %s' % (element.label_, element))
	entities += str(element) + " "

# Loading the stop words from nltk library
stop_words = nltk.corpus.stopwords.words('english')

# creating a list that contains the NER words in lower case	
ner = []
for entity in nltk.word_tokenize(entities):
	if entity not in stop_words:
		ner.append(entity.lower())


# Tokenizing the article into sentences
sentences = nltk.sent_tokenize(article)	

# This method completely ignores the sentences with length above 25 words.
# Since someties those sentecnes could be useful I have also included this 
# approach to penalize the sentences. 
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

# Scoring the sentences based on the no of NER words the contain	
sent2score2  = {}
for sentence in sentences:
	for word in nltk.word_tokenize(sentence.lower()):
		if word in ner:
			if sentence not in sent2score2.keys():
				sent2score2[sentence] = 1
			else:
				sent2score2[sentence] += 1 # for each word of the sentence in ner give a score of +1 to that sentence.

# Penalizing the sentences by their length. As larger sentences are expected to have more
# words and therefore more NER's. Hence the will hinder the selection of sentences of smaller lengths.
for sentence,score in sent2score2.items():
	sent2score2[sentence] = score/len(sentence)

# Creating a dictionary to store the order of occurene of each sentence. 
# Later this order would be used to sort the summary in the original temporal order.
sent2idx = {}
i=0
for sentence in sentences:
	sent2idx[sentence] = i
	i += 1
	 
# Picking 'n' sentences with highest scores usign heapq
best_sentences = heapq.nlargest(5,sent2score2,key = sent2score2.get)

# Creating a dictionary to get the index of the best sentences from set2idx dictionary.
bestsent2idx = {}
for sentence in best_sentences:
	bestsent2idx[sentence] = sent2idx[sentence]

# Sorting the best sentences in their original temporal order
best_sentences = heapq.nsmallest(5,bestsent2idx,key = bestsent2idx.get)

summary = ""

# Adding the best sentences to the summary.
for sentence in best_sentences:
	summary += str(sentence)

# Printing the article and the summary
print('Article: ',article)
print('Summary: ',summary)	
				

			

	

	