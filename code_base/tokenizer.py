import nltk
from nltk.corpus import stopwords

def tokenize( text ):
    """
    Tokenize a given text.
    :param text:    the text which will get tokenized
    :return:        list of tokens        
    """
    tokens = nltk.word_tokenize( text )
    return tokens


def stopword_removal( tokens ):
    """
    Tokenize a given text and remove the stopwords.
    :param text:    the text which will get tokenized
    :return:        list of tokens without stopwords        
    """
    tokens_without_stopwords = [ token for token in tokens if not token in stopwords.words() ]
    return tokens_without_stopwords