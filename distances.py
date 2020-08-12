import numpy


def bias_distance(bias_val_one, bias_val_two):

    bias_val_one_round = round(bias_val_one,3)
    bias_val_two_round = round(bias_val_two,3)

    return abs(bias_val_one_round-bias_val_two_round)

def stylo_distance(stylo_dict_one, stylo_dict_two):
    vector_one = create_vector(stylo_dict_one)




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