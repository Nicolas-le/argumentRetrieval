from bsdetector import bias


def bias_score(sentence):
    """
    Sent Analysis + bias lex + empath
    :param tokens:
    :return:
    """

    return bias.compute_bias(sentence)

"""
sentence = "I hate yellow boats."
print(bias_score(sentence))
"""