# word-clouds
Automatisation de la creation des ''word clouds'' a partir des tweets.

Our tool automates the creation of word clouds from tweets on Twitter. With our tool, we can create the word cloud, by searching the words and filtering the tweets by language and date. 

Word Cloud is a data visualization technique used for representing text data, in which the size of each word indicates its frequency or importance. It’s useful for companies to analyze the feedback from their customers. To collect the data from Twitter, we used the API. API, or Application Programming Interface, is a software intermediary that allows two applications to talk to each other.

Important definition: Stopwords are the commonly occurring words in different languages such as “the”, “a”, “an”, “in”… that don’t add much meaning to a sentence. In our case, we have three lists of stopwords for three languages: English, French, and  Spanish. These words are ignored in natural language processing tasks. So we add stopwords list, so they won’t appear in the word cloud.

For this purpose, the Twitter API is used to get access to the endpoint where tweets are searched. Then library wordclouds is used to build the graphical representation. Also the library PyQt5 is used to create the UI from which the user gets access to all functions. 

To use this program it is necessary to download the folder "Twitter" and save it on any machine where python has access. An installation of python 3+ is required. Additional libraries are required such as: PyQt5 and wordcloud. 
Once installed the file "UI.py" must be executed by the python interpreter, there the usual interface will appear giving the user the options to search for any given word. The program will query the twitter API and will create a wordcloud in the output/wordclouds directory. 

Files:
- UI.py. In this file there is the code to create the UI of the tool. PyQt5 is used to create all elements of the UI.
- Twitter.py. The code in this file defines a function that, given a word to search, language, starting date and ending date, will query the Twitter API in search of the tweets. In return the function will return a string variable including all the text information from the tweets. THe credentials to twitter development account are needed. 
- Text_processing.py. This code several functions are defined, the general purpose is to handle the tweets that are received.
- Wordcloud.py. The code here allows for a creation of a worcloud given a text, in this case it is defined to get text from the tweets and also use the definition of different stopwords for the different laguages. The stopwords included in the NLTK module are also included. The wordcloud created by the function defined is saved in the output/wordclouds directory.
- credentials.py. The credentials to access the Twitter API are defined here.
- \stopwords. Inside the directory 3 files with stopwords are found, one file for stopwords for each language supported at the moment: French, Spanish and English.
- \output. Inside the folder the text from the tweets are saved for further future study. 
- \output\stopwords. Folder where the stopwords created are saved. 

Structure:
General flow diagram is found describing in detail the flow of the information on the project. Broadly speaking, the user can provide a search word, language and dates by using the UI. There the UI calls on the functions defined on the other files. First the function get_tweets() is called in order to query the API and retrieve the tweets. Then, by using the functions defined in text_processing.py, the tweets are processed and then saved in the folder output. Right after, the function create_wordcloud on wordcloud.py is called and given the text processed, insided it, the function get_stopwords is used to load the stopwords for the language used, thereafter creating the wordcloud and saving it to the folder output/wordclouds.
