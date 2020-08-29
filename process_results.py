from nlp_analysis import *


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
