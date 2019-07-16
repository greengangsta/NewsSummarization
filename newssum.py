"""
Members
1.acc.surajtripathi@gmail.com(Representative)
2.sonivaibhav939@gmail.com
3.vidyanamde1995@gmail.com

"""

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
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
		article += str(line)# article contains all the sentences of the corresponding text files.
		

#Cleaning the article using regular expression		
article = re.sub(r'\[[0-9]*\]','',article)
article = re.sub(r'\s+',' ',article)
clean_article = re.sub(r'\W',' ',article)
clean_article = re.sub(r'\d',' ',clean_article)
clean_article = re.sub(r'\s+',' ',clean_article)

# Tokenizing the article into sentences
sentences = nltk.sent_tokenize(article)

# Loading the stop words from nltk library
stop_words = nltk.corpus.stopwords.words('english')

#Dictionary which will contain the key as the word and the frequency of the word as the value.
word2count = {}

# Finding the frequency of each word in the article
for word in nltk.word_tokenize(clean_article):
	if word not in stop_words:
		if word not in word2count.keys():
			word2count[word] = 1
		else:
			word2count[word] += 1

# Dividing the frequency by the max value of frequency(Term Frequency- Inverse Document Frequency )
# based approach			
for key in word2count.keys():
	word2count[key] = word2count[key]/max(word2count.values())

# Dictionary to contain the score of the sentences
sent2score  = {}
# Finding the score of each sentence 
for sentence in sentences:
	for word in nltk.word_tokenize(sentence.lower()):
		if word in word2count.keys():
			if sentence not in sent2score.keys():
				sent2score[sentence] = word2count[word] 
			else:
				sent2score[sentence] += word2count[word] #For each word in the sentence we add the frequency as the score.

# Penalizing the sentences by their length. As larger sentences are expected to have more
# words and therefore more NER's. Hence the will hinder the selection of sentences of smaller lengths.
for sentence,score in sent2score.items():
	sent2score[sentence] = score/len(sentence)
					


# Creating a dictionary to store the order of occurene of each sentence. 
# Later this order would be used to sort the summary in the original temporal order.
sent2idx = {}
i=0
for sentence in sentences:
	sent2idx[sentence] = i
	i += 1

# Picking 'n' sentences with highest scores usign heapq					
best_sentences = heapq.nlargest(5,sent2score,key = sent2score.get)

# Creating a dictionary to get the index of the best sentences from set2idx dictionary.
bestsent2idx = {}
for sentence in best_sentences:
	bestsent2idx[sentence] = sent2idx[sentence]
	
# Sorting the best sentences in their original temporal order
best_sentences = heapq.nsmallest(5,bestsent2idx,key = bestsent2idx.get)

# Adding the best sentences to the summary
summary = "".
for sentence in best_sentences:
	summary += str(sentence)

# Printing the article and the summary
print('Article: ',article)
print('Summary: ',summary)			

			

	

	