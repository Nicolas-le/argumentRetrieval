import readability_measures
from collections import defaultdict
import nltk
from spellchecker import SpellChecker as sc



def main_stylo(tokens):
    """
    Main functionality of the stylometric analysis. Creates the dictionary of the calculated
    values.
    :param tokens:  a tokenized list of strings
    :return:        dictionary key: calculated feature | value: value of the feature
    """

    feature_Dict = defaultdict(dict)

    feature_Dict['vocab_richeness'] = vocab_richness(tokens)
    feature_Dict['hepax_legomena'] = hepax_legomena(tokens)
    feature_Dict['readability_measures'] = readability_measures.main(tokens)
    feature_Dict['spelling_erros'] = spelling_errors(tokens)

    return feature_Dict


def vocab_richness(tokens):
    """
    Calculates the ratio of the number of distinct words to the number of total words.
    :param tokens:  a tokenized list of strings
    :return:        the calculated ratio
    """
    distinct_words = len(set(tokens))
    total_words = len(tokens)

    #prevent dividing by 0
    if total_words == 0:
        return

    return distinct_words/total_words

def hepax_legomena(tokens):
    """
    Hepax Legomena is the ratio of the numbers of words occurring once to the total number
    of words.
    :param tokens:  a tokenized list of strings
    :return:        the calculated ratio
    """

    all_words = set()
    duplicates = set()

    for token in tokens:
        if token in all_words:
            duplicates.add(token)
        all_words.add(token)

    words_appearing_once = len(all_words-duplicates)
    total_words = len(tokens)

    return words_appearing_once/total_words

def spelling_errors(tokens):
    """
    Counts the spelling errors of a tokenized list (english). Possible value to measure tiredness
    or hecticness of users.(
    :param tokens:  a tokenized list of strings
    :return:        counter for spelling errors
    """
    spell = sc()
    misspelled = spell.unknown(tokens)

    #spelling error in relation to the length of the input tokens
    return len(misspelled)/len(tokens)






