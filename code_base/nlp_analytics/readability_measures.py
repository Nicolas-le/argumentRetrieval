from nltk.tokenize.treebank import TreebankWordDetokenizer
import nltk
from collections import defaultdict


def main( tokens ):
    """
    Creates a dictionary with of the readability measures average word length and the average
    sentence length.
    :param tokens: the tokenized list of words
    :return:        a dictionary with the two values
    """
    readability_measures_Dict = {}
    readability_measures_Dict['average_wordlength'] = average_wordlength(tokens)
    readability_measures_Dict['average_sentlength'] = average_sentlength(tokens)
    return readability_measures_Dict


def average_wordlength( tokens ):
    """
    Calculates the average word length.
    sum(len(token) for token in tokens) --> count the length of every token and builds the sum
    / len(tokens) -> number of tokens
    :param tokens:  the tokenized list of words
    :return:        all words lengths together divided through the word count
    """
    if len(tokens) != 0:
        return ( sum(len(token) for token in tokens) ) / len(tokens)
    else:
        return 0


def average_sentlength( tokens ):
    """
    Calculates the sentence word length.
    len(nltk.word_tokenize(sent)) -> length of each sentence, tokenized individually
    (sum(len(nltk.word_tokenize(sent)) for sent in sent_tokens)) -> sum of all sentence lengths
    :param tokens:  the tokenized list of words
    :return:        average sentence length
    """
    #detokenize the tokenized list --> rebuilding the sentences
    original_text = TreebankWordDetokenizer().detokenize( tokens )
    #use the sentence tokenizer
    sent_tokens = nltk.sent_tokenize( original_text )

    if len(sent_tokens) != 0:
        return ( sum(len(nltk.word_tokenize( sent )) for sent in sent_tokens) ) / len(sent_tokens)
    else: 
        return 0


