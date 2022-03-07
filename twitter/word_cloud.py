import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from random import choice
import re


def get_stopwords():
    with open("stopwords/spanish.txt", "r",encoding = "utf-8") as f:
        stpw_spanish = f.readlines()
        stpw_spanish = str.split(stpw_spanish[0],",")

    with open("stopwords/french.txt", "r",encoding = "utf-8") as f:
        stpw_french = f.readlines()
        stpw_french = str.split(stpw_french[0],",")
        
    with open("stopwords/english.txt", "r",encoding = "utf-8") as f:
        stpw_english = f.readlines()
        stpw_english = str.split(stpw_english[0],",")

    stopwords_es = stopwords.words("spanish")
    stopwords_en = stopwords.words("english")
    stopwords_fr = stopwords.words("french")
    stopwords_spanish = stopwords_es+stpw_spanish
    stopwords_english = stopwords_en+stpw_english
    stopwords_french = stopwords_fr+stpw_french

    return stopwords_english, stopwords_french, stopwords_spanish

def add_stopwords_searched(searched_word):
    stopword = searched_word.split()
    return stopword

def get_text_tweets(searched_word,lan):
    
    searched_word = re.sub(" ","-",searched_word)
    tweets_path = f"output/{searched_word}_{lan}.txt"
    with open(tweets_path,"r",encoding="utf-8") as f:
        text = f.readlines()
        text = text[0]
    return text

def create_wordcloud(lan,text,name):
    stopwords_english, stopwords_french, stopwords_spanish = get_stopwords()
    stopwords = []
    
    if lan == "en":
        stopwords = stopwords_english
    elif lan == "fr":
        stopwords = stopwords_french
    else: 
        stopwords = stopwords_spanish
    
    stopwords = stopwords + add_stopwords_searched(name)

    colormap_list = ["CMRmap","ocean","gist_stern","gnuplot","cubehelix","nipy_spectral"]
    colormap = choice(colormap_list)
    
    word_cloud = WordCloud(background_color="white",colormap= colormap, width=3000, height=2000, max_words=300,stopwords = stopwords, collocations=False).generate(text)
    
    plt.figure(figsize=[15,10])
    plt.axis("off")
    plt.imshow(word_cloud,interpolation="bilinear")
    name = re.sub(" ","-",name)
    png_path = f"output/wordclouds/{name}_{lan}.png"
    plt.savefig(png_path)
