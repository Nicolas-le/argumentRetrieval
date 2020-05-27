from collections import defaultdict
import nltk


def main_stylo(tokens):

    feature_Dict = defaultdict(dict)

    feature_Dict['vocab_richeness'] = vocab_richness(tokens)
    feature_Dict['hepax_legomena'] = hepax_legomena(tokens)

    print(feature_Dict)


def vocab_richness(tokens):

    distinct_words = len(set(tokens))
    total_words = len(tokens)

    if distinct_words == 0:
        return

    return total_words/distinct_words

def hepax_legomena(tokens):

    all_words = set()
    duplicates = set()

    for token in tokens:
        if token in all_words:
            duplicates.add(token)
        all_words.add(token)

    words_appearing_once = len(all_words-duplicates)
    total_words = len(tokens)

    return total_words/words_appearing_once



sentence = "I would like to got to the my beach, sir"

tokens = nltk.word_tokenize(sentence)
main_stylo(tokens)