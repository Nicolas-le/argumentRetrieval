import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from pattern.en import lemma
import sent_analysis
import topic_signal_modeling


def bias_score(tokens):
    """
    Sent Analysis + bias lex + empath
    :param tokens:
    :return:
    """
    bias = {}
    bias["bias_word_count"] = bias_lexicon(tokens,"bias-lexicon.txt")
    bias["sentiment_subjectivity"] = sent_analysis.textblob(TreebankWordDetokenizer().detokenize(tokens)).subjectivity
    empath_to_bias(tokens)


    print(bias)

def bias_lexicon(tokens,lexicon):
    """
    Implements the bias word lexicon of Marta Recasens, Cristian Danescu-Niculescu-Mizil, Dan Jurafsky.
    https://web.stanford.edu/~jurafsky/pubs/neutrality.pdf
    :param tokens:
    :return:            a counter of how many words appearing in the lexicon were used in the input tokens
    """
    lexiconFile = open(lexicon,"r")
    lexicon_list = []
    used_bias_words = []

    for i in lexiconFile:
        lexicon_list.append(i.replace("\n",""))

    for token in tokens:
        #lemmatize one time with the pattern lemmatizer, pattern is important!
        token_lemmatized = lemma(token)
        for bias_word in lexicon_list:
            if bias_word == token_lemmatized:
                used_bias_words.append((token,token_lemmatized))

    return len(used_bias_words)

def empath_to_bias(tokens):
    empath_values = topic_signal_modeling.ts_mod(tokens)

    if not empath_values:
        return 0
    print(empath_values)






sentence = "I want to got swimming"
tokens = nltk.word_tokenize(sentence)
bias_score(tokens)