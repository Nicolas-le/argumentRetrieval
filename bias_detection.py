from bsdetector import bias



def bias_score(sentence):
    """
    Main function calling the bsdetector.
    :param sentence: Sentence, the bias should be calculated for.
    :return: a bias value between -3 and 3
    """

    return bias.compute_bias(sentence)

