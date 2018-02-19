#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:34:13 2018

@author: Sundar Gsv
"""

# Word2Vec - Word Embeddings

# Importing libraries
import pandas as pd
import nltk
# nltk.download('punkt')
import gensim
from gensim import corpora, models, similarities

# Getting dataframe
dataFrame = pd.read_csv('jokes.csv');


# Seperating Q & A as two different vectors - Unused
x = dataFrame['Question'].values.tolist()
y = dataFrame['Answer'].values.tolist()

corpus = x + y
  
# Tokenizing the words list from the Q & A sentences
tokenizedWords = [nltk.word_tokenize(sent) for sent in corpus]
       
# Performing our word2Vec model
# Where min_count is the minimum occurence of the word in the corpus     
model = gensim.models.Word2Vec(tokenizedWords, min_count = 1, size = 32)

# Save the model for future purpose
model.save('word2VecModel')

# To load the saved model from the working directory
modelFrom = gensim.models.Word2Vec.load('word2VecModel')

# To check the similarities and word vectors
modelFrom.most_similar('hey')
model['hey']
