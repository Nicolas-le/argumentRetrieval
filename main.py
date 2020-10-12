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


"""
construct the argument parse and parse the arguments
"""
ap = argparse.ArgumentParser( description='Index the corus and generates runs!' )


"""
the input directory should contain the (debateorg.json, debatepedia.json, debatewise.json,idebate.json, 
parliamentary.json and the topics.xml file) 
"""
ap.add_argument( "-i", "--input-dir", required=True, help='corpus-dir' )


"""
We will create a standard trec run file in $outputDir/run.txt
"""
ap.add_argument( "-o", "--output-dir", required=True, help='topics-dir' )


"""
turn the parsed command line arguments into a Python dictionary
"""
args = vars( ap.parse_args() )


"""
check if the given files exist
"""
if os.path.exists( args["output_dir"] ) & os.path.exists( args["input_dir"] ):
       print( "input and outputfiles exist" )
else:
    print( "File does not exist!" )


"""
path variables for input and output directory
"""
inputDataSet = args["input_dir"]
outputDir = args["output_dir"]


"""
establish connection to the elastic search cluster
"""
es_obj = connect_to_elasticsearch()


"""
create an index
"""
index_name = "local_index_v1.0"
indexObj = create_index( es_obj, index_name )


"""
start extracting and indexing the corpus
"""
#extractdataSetToIndex( inputDataSet, es_obj, index_name  )


"""
process the topics.xml and search them motherfuckin' topics in the air
"""
process_xml( es_obj, index_name, inputDataSet, outputDir, )
