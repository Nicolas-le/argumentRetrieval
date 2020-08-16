"""
Calculates a error value of the wanted linear relation between spelling errors and average sentence length.
"""
import math

def distance(spelling_errors,average_sentlength):
    """
    :return:
    """
    # f(x)= -x+5

    # if there are no spelling errors the distance is always 0 because its not relevant
    y = -spelling_errors+10


    dist = abs(y-average_sentlength)

    return math.sqrt(math.sqrt(dist))

