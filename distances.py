import numpy
import hectic


def bias_distance(bias_val_one, bias_val_two):
    """
    Simple distance value between two bias values.
    :param bias_val_one:    bias value of query
    :param bias_val_two:    bias value of argument
    :return:                difference as an absolute
    """

    bias_val_one_round = round(bias_val_one,3)
    bias_val_two_round = round(bias_val_two,3)

    return abs(bias_val_one_round-bias_val_two_round)

def stylo_distance(stylo_dict_one, stylo_dict_two):
    """
    Creates the vectors out of the dictionaries created by the nlp analysis.
    returns the euclidean distance between the vectors including the influence of spelling errors to the average sentence length
    :param stylo_dict_one:  Calculated dictionary containing stylometric values one
    :param stylo_dict_two:  Calculated dictionary containing stylometric values two
    :return:                a distance value of these two dictionaries (space vector model)
    """
    vector_one = create_vector(stylo_dict_one)
    vector_two = create_vector(stylo_dict_two)

    euclid_dist = euclidean_distance(vector_one,vector_two)
    spelling_error_influence = hectic.distance(stylo_dict_one["spelling_errors"],stylo_dict_two["readability_measures"]["average_sentlength"])

    if spelling_error_influence == 0:
        distance = euclid_dist
    else:
        distance = euclid_dist*spelling_error_influence

    return distance


def create_vector(style_dict):
    """
    Creates a vector out of one stylometric dictionary
    :param style_dict:      stylometric dictionary
    :return:                an array containing the wanted dimension values --> vector
    """
    vector = [0,0,0,0]

    vector[0] = style_dict["vocab_richeness"]
    vector[1] = style_dict["hepax_legomena"]
    vector[2] = style_dict["readability_measures"]["average_wordlength"]
    vector[3] = style_dict["readability_measures"]["average_sentlength"]

    return vector

def euclidean_distance(vector_one, vector_two):
    """
    Calculates the euclidean distance in a space vector model of two vectors.
    :param vector_one:      first vector
    :param vector_two:      second vector
    :return:                multidimensional distance value
    """
    a = numpy.array(vector_one)
    b = numpy.array(vector_two)

    dist = numpy.linalg.norm(a-b)

    return dist

"""
#Test functionality
sample_dict_query = {'vocab_richeness': 0.9090909090909091, 'hepax_legomena': 0.8181818181818182, 'readability_measures': {'average_wordlength': 3.727272727272727, 'average_sentlength': 27.555555555555557}, 'spelling_errors': 0}
sample_dict_argument = {'vocab_richeness': 0.5483870967741935, 'hepax_legomena': 0.375, 'readability_measures': {'average_wordlength': 5.032258064516129, 'average_sentlength': 5.5}, 'spelling_errors': 0.004032258064516129}

print(stylo_distance(sample_dict_query,sample_dict_argument))
"""