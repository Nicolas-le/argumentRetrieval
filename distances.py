import numpy


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
    returns the euclidean distance between the vectors
    :param stylo_dict_one:
    :param stylo_dict_two:
    :return:
    """
    vector_one = create_vector(stylo_dict_one)
    vector_two = create_vector(stylo_dict_two)

    return euclidean_distance(vector_one,vector_two)


def create_vector(style_dict):
    #spelling errors zu länge eher,
    vector = [0,0,0,0,0]

    vector[0] = style_dict["vocab_richeness"]
    vector[1] = style_dict["hepax_legomena"]
    vector[2] = style_dict["readability_measures"]["average_wordlength"]
    vector[3] = style_dict["readability_measures"]["average_sentlength"]
    vector[4] = style_dict["spelling_errors"]

    return vector

def euclidean_distance(vector_one, vector_two):
    a = numpy.array(vector_one)
    b = numpy.array(vector_two)

    dist = numpy.linalg.norm(a-b)

    return dist

sample_dict_query = {'vocab_richeness': 0.9090909090909091, 'hepax_legomena': 0.8181818181818182, 'readability_measures': {'average_wordlength': 3.727272727272727, 'average_sentlength': 5.5}, 'spelling_errors': 0.0}
sample_dict_argument =

print(stylo_distance(sample_dict,sample_dict))