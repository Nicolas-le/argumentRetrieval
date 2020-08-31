from bsdetector import bias
import nltk



def bias_score(text):
    """
    Main function calling the bsdetector.
    :param sentence: Sentence, the bias should be calculated for.
    :return: a bias value between 0 and 3
    """
    sentences = nltk.sent_tokenize(text)
    total_bias = 0
    for sentence in sentences:
        total_bias += bias.compute_bias(sentence)

    return total_bias/len(sentences)

