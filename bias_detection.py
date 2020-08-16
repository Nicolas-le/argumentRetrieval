from bsdetector import bias

def bias_score(sentence):
    return bias.compute_bias(sentence)

#sentence = "I hate yellow boats."
#print(bias_score(sentence))