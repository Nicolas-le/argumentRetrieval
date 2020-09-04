from nlp_analysis import *


def process_results( results_list ):
    """
    Processes a list of retrieved documents and analyze the premise by NLP. Adds the NLP scores to each document.
    :param results_list:    list of retrieved documents by an index search
    :return:                list of retrieved documents with NLP scores for each document
    """
    rl = []
    count = 0
    for result in results_list:
        scores = analyze( result['_source']['premise'] )
        new_dic = dict( result, **scores )
        rl.append( new_dic )
        count= count+1 
        print( count )
        
    return rl 
