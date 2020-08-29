import csv
import pandas as pd
import os 






def write_into_trec( doc, topicNumber,outputDir, rank  ):


      with open(f'{outputDir}/run.txt', 'a', newline='') as txtfile:
           txtfile.write( topicNumber+" "+"Q0"+" "+str(doc['_source']['id'])+" "+str(doc['new_doc_score'])+" "+ "bias_detection"+"\n" )




def write_header( outputDir ):

   with open(f'{outputDir}/run.txt', 'a', newline='') as txtfile:
        
        txtfile.write("topic_number,  Q0,  arg_ids,  score,  method "+"\n")





def generate_results( output_dir ):
    
    text = open(os.path.join(output_dir, "run.csv"), "r")
    text = ''.join([i for i in text]) \
        .replace(" ", "    ")
    x = open(os.path.join(output_dir, "run1.csv"),"w")
    x.writelines(text)
    x.close()






   






