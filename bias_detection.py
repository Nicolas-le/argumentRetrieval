from bsdetector import bias
import csv


def bias_score(sentence):
    """
    Sent Analysis + bias lex + empath
    :param tokens:
    :return:
    """

    return bias.compute_bias(sentence)


file = csv.DictReader(open("topics.csv","r"))

for i in file:
	print(i["Long Query"])
	print(bias_score(i["Long Query"]))

	print(i["Short Query"])
	print(bias_score(i["Short Query"]))

	print()

	

	

"""
sentence = "I hate yellow boats."
print(bias_score(sentence))
"""
