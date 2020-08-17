import math

def distance(spelling_errors,average_sentlength):
    """
    Calculates an error value of the wanted linear relation between spelling errors and average sentence length.
    :param spelling_errors:     Count of spelling errors in the query.
    :param average_sentlength:  Average Sentence length of the retrieved argument
    :return:                    Influence value which can be multiplied.
    """

    # f(x)= -0.3x+10 --> function of which the error value is calculated of, assumed/wanted linear model
    y = -(0.3*average_sentlength)+10

    #the distance/error is the absolute value between the estimated average sentence length and the measured one
    dist = abs(y-spelling_errors)

    #reducing the influence by using the transformation method square root twice (https://fmwww.bc.edu/repec/bocode/t/transint.html)
    transformed_dist =  math.sqrt(math.sqrt(dist))

    #reduce or increase influence based on spelling errors
    influence_value = influence_reducer(spelling_errors)

    return transformed_dist*influence_value



def influence_reducer(spelling_errors):
    """
    If there are less spelling errors, the influence of the spelling errors to sentence length should get lower.
    If there are not spelling errors in th query a potential user can get short sentenced arguments as well as
    some with long sentences. There is less need of an influence.
    The function used to calculate the influence is a quadratic function, because the influence should
    hav ean quadratic increase if there are more
    :param spelling_errors:     Count of spelling errors in the query.
    :return:                    Influence value which can be multiplied
    """

    #Quadratic function (f(x) = 0.5x^2)
    influence_value = 0.5*spelling_errors**2

    transformed_influence_value = math.sqrt(math.sqrt(influence_value))

    return transformed_influence_value

