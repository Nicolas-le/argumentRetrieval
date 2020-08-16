import nltk
from nltk.corpus import stopwords

def tokenize( text ):
    tokens = nltk.word_tokenize( text )
    return tokens

def stopword_removal( tokens ): 
    tokens_without_stopwords = [ token for token in tokens if not token in stopwords.words() ]
    return tokens_without_stopwords