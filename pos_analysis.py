import nltk
from collections import Counter

def main(tokens):
    """
    Taggs the words for ther part of speech using the nltk pos tagger. Then counts each pos occurence
    to later answer question f.ex. conerning the use of adjectives, verbes, etc.
    :param tokens:  a tokenized list of strings
    :return:        a dictionary with at the moment only one entry
    """

    pos_analysis_dict = {}

    tagged_list = nltk.pos_tag(tokens)
    counts = Counter(tag for word,tag in tagged_list)

    pos_analysis_dict['pos_counters'] = counts

    return pos_analysis_dict



