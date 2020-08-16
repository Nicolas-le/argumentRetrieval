import math

def distance(spelling_errors,average_sentlength):
    """
    Calculates an error value of the wanted linear relation between spelling errors and average sentence length.
    :return: transformed error/distance value
    """
    # f(x)= -x+10 --> function of which the error value is calculated of, assumed/wanted linear model
    y = -spelling_errors+10

    #the distance/error is the absolute value between the estimated average sentence length and the measured one
    dist = abs(y-average_sentlength)

    #reducing the influence by using the transformation method square root twice (https://fmwww.bc.edu/repec/bocode/t/transint.html)
    return math.sqrt(math.sqrt(dist))

