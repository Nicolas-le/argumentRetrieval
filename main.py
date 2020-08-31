#import the necessary packages
import argparse
import sys
sys.path.append('./code_base/nlp_analytics')
sys.path.append('./code_base/ES')
sys.path.append('./code_base/distance_calculations')

from connect_to_elasticsearch import *
from create_index import *
from process_topics import *
from extract_dataSet_toIndex import *
from process_topics import * 
from process_trec_format import *
import csv
#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description='Index the corus and generates runs!')

"""
the input directroy should contain the  ( debateorg.json, debatepedia.json, debatewise.json,idebate.json, 
parliamentary.json and the topics.xml file. 
"""
ap.add_argument("-i", "--input-dir" , required=True ,help='corpus-dir')

"""
We will create a standard trec run file in $outputDir/run.txt
"""
ap.add_argument("-o", "--output-dir", required=True ,help='topics-dir')
#turn the parsed command line arguments into a Python dictionary 
args = vars(ap.parse_args())

# check if the given files are exist 
if os.path.exists(args["output_dir"]) & os.path.exists(args["input_dir"]) :
       print("input and outputfiles exist")
else:
    print("File does not exist!")
inputDataSet = args["input_dir"]

outputDir = args["output_dir"]

#elastic_search object
es_obj = connect_to_elasticsearch()

#create an Index_object
index_name = "local_index_v1.0"

indexObj = create_index( es_obj, index_name )

#start extracting and indexing the corpus 
#extractdataSetToIndex( inputDataSet, es_obj, index_name  )

"""
processing the xml_topics and searching them

the function will be called twice:  !) to retrieve arguments

where the stance is pro and 2) to retrieve arguments , where the stance is con
"""

process_xml( es_obj, index_name,inputDataSet,outputDir,True )
process_xml( es_obj, index_name,inputDataSet,outputDir,False)
