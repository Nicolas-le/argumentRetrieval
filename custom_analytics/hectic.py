"""
Calculates a distance value out of the mean squarred error of the wanted linear relation between spelling errors and average sentence length.
"""
import numpy as np

def distance(spelling_errors,average_sentlength):
    """
    :return:
    """
    Y_true = [1,2,3,4,5]  # Y_true = Y (original values)

    # Calculated values
    Y_pred = [3,5]  # Y_pred = Y'

    # Mean Squared Error
    MSE = np.square(np.subtract(Y_true,Y_pred)).mean()

    return MSE

print(distance(1,5))
