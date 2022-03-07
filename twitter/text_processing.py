import re 
import pandas as pd
import datetime

def tweet_to_words(tweet):
    REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\¿)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

    words = re.sub("(?P<url>https?://[^\s]+)"," ",tweet)
    words = re.sub("_","",words)
    words = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z_À-ÿ \t])|(\w+:\/\/\S+)","",words)

    words = REPLACE_NO_SPACE.sub("", words.lower())
    words = REPLACE_WITH_SPACE.sub(" ", words)
    words = str(words)
    return words
    
def tweets_dataframe(tw_dataframe):
    tw_dataframe["text2"] = tw_dataframe["text"].apply(tweet_to_words)
    tw_dataframe.to_excel("output/tweets_df.xlsx")

def tweets_text_list(mytext):
    with open('output/tweets_text_list.txt', 'w',encoding="utf-8") as f:
           for element in mytext:
                element = tweet_to_words(element)
                f.write(element + "\n")

def tweets_text(mytext,searched_word,lan):
    
    searched_word = re.sub(" ","-",searched_word)
    text = str()
    for element in mytext:
        element = tweet_to_words(element)
        text = text + " " + element
    path_save_tweets = f'output/{searched_word}_{lan}.txt'
    with open(path_save_tweets, 'w',encoding="utf-8") as f:
                f.write(text)


def compare_dates(day_start,month_start,year_start,day_end,month_end,year_end):
    date_start = datetime.datetime(year_start,month_start,day_start)
    date_end = datetime.datetime(year_end,month_end,day_end)
    if date_start>date_end or date_end>datetime.datetime.now():
        return False
    else:
        return True

def dates_to_string(day_start,month_start,year_start,day_end,month_end,year_end):
    sub_string_date = str("T00:00:00.000Z")
    date_start_str = f"{year_start}-{month_start}-{day_start}"+sub_string_date
    date_end_str = f"{year_end}-{month_end}-{day_end}"+sub_string_date
    return [date_start_str,date_end_str]