# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:18:25 2021

@author: Hewlett-Packard
"""
# import pandas as pd
# import numpy as np
import re
import string
from nltk.corpus import stopwords 
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import TweetTokenizer
from google_trans_new import google_translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
from textblob import TextBlob

class PreprocessingLexicon:    
    def remove_pattern(input_txt, pattern):
        r = re.findall(pattern, input_txt)
        for i in r:
            input_txt = re.sub(i, '', input_txt)
        return input_txt
        
    def remove(tweet):
        # remove angka
        tweet = re.sub('[0-9]+', '', tweet)
    
        # remove stock market tickers like $GE
        tweet = re.sub(r'\$\w*', '', tweet)
        
        # remove redf "RT"
        tweet = re.sub(r'^RT[\s]+', '', tweet)
        
        # remove hashtags
        tweet = re.sub(r'#', '', tweet)
        return tweet
        
    def getEmoticons(self):
        # Happy Emoticons
        emoticons_happy = set([
            ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
            ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
            '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
            'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
            '<3'
            ])
        
        # Sad Emoticons
        emoticons_sad = set([
            ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
            ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
            ':c', ':{', '>:\\', ';('
            ])
        
        # all emoticons (happy + sad)
        self.emoticons = emoticons_happy.union(emoticons_sad)
        return self.emoticons
    
    def getStopwords(self):
        # stopword
        self.stopwords_indonesia = stopwords.words('indonesian')
        dataRemove = ['tidak','siap','baik','kurang','jangan']
        self.stopwords_indonesia = set(stopwords.words('indonesian')).difference(dataRemove)
        return self.stopwords_indonesia

    def getStemming(self):
        # stemming (sastrawi)
        factory = StemmerFactory()
        self.stemmer = factory.create_stemmer()
        return self.stemmer

    def cleanTweets(tweet,self):
        # remove stock market tickers like $GE
        tweet = re.sub(r'\$\w*', '', tweet)
 
        # remove old style retweet text "RT"
        tweet = re.sub(r'^RT[\s]+', '', tweet)
        
        # remove hyperlinks
        tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
        
        # remove hashtags
        # only removing the hash # sign from the word
        tweet = re.sub(r'#', '', tweet)
        
        #remove coma
        tweet = re.sub(r',','',tweet)
        
        #remove angka
        tweet = re.sub('[0-9]+', '', tweet)
        
        # tokenize tweets
        tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
        tweet_tokens = tokenizer.tokenize(tweet)
    
        # return tweets_clean
        tweets_clean = []    
        for word in tweet_tokens:
            if (word not in self.stopwords_indonesia and # remove stopwords
                word not in self.emoticons and # remove emoticons
                    word not in string.punctuation): # remove punctuation
                #tweets_clean.append(word)
                stem_word = self.stemmer.stem(word) # stemming word
                tweets_clean.append(stem_word)
                
        return tweets_clean
        
    def removePunct(text):
        text  = " ".join([char for char in text if char not in string.punctuation])
        return text
        
        
    def translateText(data):
        translator = google_translator()
        result = translator.translate(data, lang_tgt = 'en')
        # translator = translator.translate
        # df['Translate'] = df['Tweet'].apply(translator.translate, lang_tgt='en')
        return result
    
    def TranslateText2(data):
        translator = GoogleTranslator()
        trans = translator.translate(data, target='en')
        return trans
    
    def TranslateText3(data):
        translator = TextBlob(data)
        trans3 = translator.translate(from_lang='auto', to='en')
        return trans3
    
    
    def Labeling(data):
        # Vader leksikon
        analyzer = SentimentIntensityAnalyzer()
        score1 = analyzer.polarity_scores(data)
        return score1
    
    
    def Labeling2(data):
        analyzer = SentimentIntensityAnalyzer()
        score2 = analyzer.polarity_scores(data)
        return score2
        
    # def countPolarity():
        