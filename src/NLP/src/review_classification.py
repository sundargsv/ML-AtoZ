#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:04:36 2018

@author: Sundar Gsv
"""

import nltk
import random
from nltk.corpus import movie_reviews

"""documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]"""

# nltk.download('movie_reviews')
# dataset = movie_reviews.words
documents = []
categoryList = []
fileList = []
for category in movie_reviews.categories():
    categoryList.append(category)
    for fileid in movie_reviews.fileids(category):
        fileList.append(fileid)
        documents.append((list(movie_reviews.words(fileid)), category))
        
random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(10))
# print(all_words["stupid"])

word_features = list(all_words.keys())[: 3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featureSets = [(find_features(rev)) for (rev, category) in documents]
"""for (rev, category) in documents:
    featureSets.append(find_features(rev), category)
print(featureSets[0]['plot'])
print(len(featureSets[0]))"""

# print(len(featureSets[0]))