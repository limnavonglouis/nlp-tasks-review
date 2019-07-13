#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:33:44 2019

@author: louislimnavong

description: functions for NLP 
"""


import stop_words
import re
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

def cleaning_string(raw_text) : 
    
    STOPWORDS = stop_words.get_stop_words(language='en')
    stemmer = SnowballStemmer("english")
    try: 
        clean_text = re.sub('[^A-Za-z]+',' ', raw_text).lower()
        clean_token = word_tokenize(clean_text)
        clean_token = [i for i in clean_token if i not in STOPWORDS]
        word_list = [stemmer.stem(y) for y in clean_token]
        processed_text = ' '.join(word for word in word_list)
    except TypeError:
        processed_text = ''
    
    
    return processed_text

def cleaning_data(df, column) : 
    df['clean_text'] = df[column].apply(lambda x : cleaning_string(x))
    df = df[~df['clean_text'].isnull()]
    df = df[~(df['clean_text']==' ')]
    df.reset_index(inplace=True, drop=True)
    return df 

