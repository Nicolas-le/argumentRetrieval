#import the necessary packages
import argparse

#from create_index_object import *



from process_topics import *

import sys 
print(sys.path)






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

if os.path.exists(args["output_dir"]):
       print("File exist")
else:
    print("File does not exist!")



inputDataSet = args["input-dir"]
outputDir = args["output_dir"]

#elastic_search object
#es = create_index_object()


process_xml(topics_dir)


