#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:01:42 2019

@author: louislimnavong
"""

import stop_words
import re
from nltk.tokenize import word_tokenize

def string_to_token(raw_text) : 
    
    STOPWORDS = stop_words.get_stop_words(language='en')
    try: 
        clean_text = re.sub('[^A-Za-z]+',' ', raw_text).lower()
        clean_token = word_tokenize(clean_text)
        clean_token = [i for i in clean_token if i not in STOPWORDS]
        
    except TypeError:
        clean_token = ''
    
    
    return clean_token

def column_token(df, column) : 
    df['clean_text'] = df[column].apply(lambda x : string_to_token(x))
    df = df[~df['clean_text'].isnull()]
    df = df[~(df['clean_text']==' ')]
    df.reset_index(inplace=True, drop=True)
    return df 