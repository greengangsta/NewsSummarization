# NewsSummarization
Creating a machine learning model which takes news articles as input and produces their summaries as output.
<br>
Approach 1 : Using word frequency to score the sentences.(newssum.py)
<br>
Approach 2 : Using ner words to score the sentences.(newssumNER.py)
<br>
<h2>Dependencies</h2>:
<ul>
<li>Python</li>
<li>numpy</li>
<li>pandas</li>
<li>heapq</li>
<li>spacy</li> 
<li>nltk</li>
<li>matplotlib</li>
<li>beutiful soup</li>
<li>re</li>
<li>urllib.request</li>
</ul>
Note : Some of the dependencies might already be fulfilled if you are using anaconda environment.
<br>
Members Group 1939 <br>
1.acc.surajtripathi@gmail.com(Representative)<br>
2.sonivaibhav939@gmail.com<br>
3.vidyanamde1995@gmail.com<br>
<br>
<h2>Instructions for running </h2> No model training is required for these two approaches as they are both extractive methods of text summarization. To run the solution on your article modify the path in the section with loading the article. You can also scrape the article from a webpage by providing the link, but make sure that the article is contained in the paragraph tag of HTML. Please install the required dependencies mentioned above before running the files. Dataset provided in the repository is non-significant  for these two approaches. For getting the summaries with a specific lenght choice(no of sentences) all you have to do is modify the value of n in heapq.nlargest and heapq.nsmallest function which is currently set to 5 sentences.
