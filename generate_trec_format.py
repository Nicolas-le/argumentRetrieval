import csv
import pandas as pd






def write_into_trec( doc, topicNumber ):


     with open('./run/run.csv', 'a', newline='') as csvfile:
        fieldnames = ['topic_number', 'Q0', 'arg_ids', 'score', 'method']
        writer = csv.DictWriter(csvfile, delimiter =' ',fieldnames=fieldnames)
        writer.writerow( {'topic_number':topicNumber, 'Q0':'Q0' ,'arg_ids':doc['_source']['id'], 'score':doc['new_doc_score'], 'method':'bias_detection' } )
       



def write_header( outputDir ):

    with open(f'{outputDir}/run.csv', 'a', newline='') as csvfile:
        fieldnames = ['topic_number', 'Q0', 'arg_ids', 'score', 'method']
        writer = csv.DictWriter(csvfile, delimiter =' ',fieldnames=fieldnames)
        writer.writeheader()










   






