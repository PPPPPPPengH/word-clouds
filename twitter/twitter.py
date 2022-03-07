import random 
from dateutil.parser import parser
import pandas as pd
import requests
import os
import json
import time
import credentials
import re


#x = os.getcwd() #get working directory
bearer_token = credentials.bearer_token
headers = credentials.headers
search_url = credentials.search_url

def get_tweets(lan,search, start_time, end_time):
    
    mytext=[]
    
    query = f"lang:{lan} ({search}) -is:retweet"
    start_time_param = start_time
    end_time_param = end_time

    x = 0
    for iteration in range(0,15):

        time.sleep(3)
    
        if x == 0:
            query_params = {'query': query,
                        
                        'start_time': {start_time_param},
                        'end_time': {end_time_param},
                        'max_results': 500,
                        'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                        'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                        'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                        'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                        'next_token': {}}    
            x = 1
        
        else:
            query_params = {'query': query,
                        
                        'start_time': {start_time_param},
                        'end_time': {},
                        'max_results': 500,
                        'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                        'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                        'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                        'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                        'next_token':{},
                        'until_id': r["meta"]["oldest_id"]}
            
        response = requests.request("GET", search_url, headers=headers, params=query_params)
    
        if response.status_code == 429:
            time.sleep(60)
            response = requests.request("GET", search_url, headers=headers, params=query_params)

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        r = response.json()
        
        for e in r["data"]:
            mytext.append(e["text"])

        print("Tweets collected")

        return mytext