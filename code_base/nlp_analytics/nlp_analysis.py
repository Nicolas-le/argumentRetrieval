from tokenizer import tokenize, stopword_removal
from bias_detection import bias_score
from stylometric_analysis import main_stylo
from topic_signal_modeling import ts_mod
from ranking_results import ranking_results


def analyze( text ):
    """
    Analyzes a given text for bias, stylometrics and hidden topics and returns an dictionary with all the scores.
    :param text:    text which will get analyzed
    :return:        dictionary with all the nlp scores
    """
    tokens = tokenize( text )
    tokens_no_stopwords = stopword_removal( tokens )
    
    bias = bias_score( text )
    stylo_scores = main_stylo( tokens )
    topics = ts_mod( tokens_no_stopwords )
    
    scores = {
        'bias_score' : bias,
        'stylo_scores' : {
            'vocab_richness' : stylo_scores['vocab_richness'],
            'hepax_legomena' : stylo_scores['hepax_legomena'],
            'readability_measures' : {
                'average_wordlength' : stylo_scores['readability_measures']['average_wordlength'],
                'average_sentlength' : stylo_scores['readability_measures']['average_sentlength']
            },
            'spelling_errors' : stylo_scores['spelling_errors']
        },
        'topics' : topics
    }
    return scores