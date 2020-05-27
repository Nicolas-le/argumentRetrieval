from collections import defaultdict
import readability_measures
import nltk


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

    print(feature_Dict)


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



#test the functionality
sentence = "I would like to got to the my beach, sir. And it would be very nice, thanks."
tokens = nltk.word_tokenize(sentence)
main_stylo(tokens)