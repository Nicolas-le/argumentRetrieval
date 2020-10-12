from bsdetector import bias
import nltk


def bias_score( text ):
    """
    Main function calling the bsdetector.
    :param sentence: Sentence, the bias should be calculated for.
    :return: a bias value between 0 and 3
    """
    #text = text + "a"
    sentences = nltk.sent_tokenize( text )
    total_bias = 0

    for sentence in sentences:
        if len( sentence ) < 2:
            total_bias = total_bias
        else:
            total_bias += bias.compute_bias( sentence )

    if len( sentences ) != 0:
        total_bias = total_bias/len( sentences )

    return total_bias
