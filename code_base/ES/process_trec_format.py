import csv
import pandas as pd
import os
import numpy as np


def write_into_trec( ranked_results, topicNumber, outputDir ):
    """
    writes trec-formatted results into the outputDir.
    convert the given dict-results into a Dataframe using Pandas.
    :param ranked_results:  list of retrieved and ranked documents
    :param topicNumber:     the number of the processed topic for the search query
    :param outputDir:       path to the output directory (usually base_code/run)
    :return:
    """
    results = dict()
    for hit in ranked_results:
        results[hit['_source']['argsMeID']] = hit['new_score']
    
    #CONVERT DICTIONARY TO TREC-STYLE DATAFRAME
    final_ranks = pd.DataFrame(list(results.items()), columns=['arg_ids', 'new_doc_score'])
    final_ranks = final_ranks.sort_values(by='new_doc_score', ascending=False)
    final_ranks['rank'] = np.arange(len(final_ranks)) + 1
    final_ranks['method'] = 'bias_detection'
    final_ranks['Q0'] = "Q0"
    final_ranks['topic_number'] = topicNumber
    
    #APPEND CURRENT DATAFRAME TO OUTPUT FILE
    with open(f'{outputDir}/run.txt', 'a+') as f:
         final_ranks[['topic_number', 'Q0', 'arg_ids', 'rank', 'new_doc_score', 'method']].to_csv(f, sep=' ', header=False, index=False)
   
   #LOOK AT WHAT WAS ACTUALLY WRITTEN TO FILE
    print(final_ranks)


def generate_results( output_dir ):
    text = open(os.path.join(output_dir, "run.csv"), "r")
    text = ''.join([i for i in text]) \
        .replace(" ", "    ")
    x = open(os.path.join(output_dir, "run1.csv"),"w")
    x.writelines(text)
    x.close()






   






