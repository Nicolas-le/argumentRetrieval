from nlp_analysis import *

"""
processes the given results_list , which is a list of dictionaries given back by the search function 
then we process each dictionary and extract the premise out of it in order to be able to analyze it 
and then we append the scores dictionary to the original dictionary and in this way we could analyse each 
retrieved argument based on out approach and add append the resulted values with the orginal result.

"""

def process_results( results_list ):
    rl = []
    count = 0
    for result in results_list:
        scores= analyze( result['_source']['premise'] )
        new_dic = dict( result, **scores )

       # for keys,values in new_dic.items():
        #    print(keys)
         #   print(values)
        rl.append( new_dic )
        count= count+1 
        print( count )
        
    return rl 
