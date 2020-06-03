from empath import Empath
import nltk

def ts_mod(tokens):
    """
    This function implements the topic signal approach of Empath. Empath uses a trained (Neuronal Networks)
    word category list with the aim to detect topic signals in tokenized text.
    :param tokens:  tokenized list of words f.ex.: ["cheese","fighting","dog","cold","man","war"]
    :return:        dictionary (created by empath) key: detected topic / value: calculated value of importance
    """
    lexicon = Empath()
    lexicon = lexicon.analyze(tokens,normalize=True)

    #check if there are detected topics, if not return
    if lexicon == None:
        return

    topicDict = threshold_filter(lexicon)

    return topicDict


def threshold_filter(lexicon):
    """
    Implements a threshold for empath values and filters all detected topics below the
    threshold value. Used to filter irrelevant topics.
    :param lexicon:     dictionary created with empath
    :return:            the filtered dictionary lexicon
    """
    threshold = 0.001 #hardcoded for now
    lexicon = { k: v for k,v in lexicon.items() if v >= threshold }

    return lexicon

"""
sentence = "Hello my friend, i hope that you are doing well. I am really happy right now."
tokens = nltk.word_tokenize(sentence)
print(ts_mod(tokens))
"""
