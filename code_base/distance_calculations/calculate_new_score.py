
def calculate_new_score( old_score, bias_distance, stylo_distance, topic_match_count ):
    """
    Function to calculate a new ranking score based on the old ranking score of the document, the bias distance, stylometric distance and the number of topics that matches between the document and the search query. 
    :param old_score:           original ranking score of the retrieved document calculated by elasticsearch
    :param bias_distance:       distance between the bias score of the document and the search query
    :param stylo_distance:      distance between the stylometric scores of the document and the search query
    :param topic_match_count:   number of empath topics that matches between the document and the search query
    :return:                    new score based on a calculation of the old ranking score and the nlp scores
    """
    new_score = old_score - (bias_distance * 10) - (stylo_distance * 0.05) + ( topic_match_count * 0.1 )
    return new_score
