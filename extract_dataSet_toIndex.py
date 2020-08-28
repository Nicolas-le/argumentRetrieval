import os

from indexing import *



"""
extracts every json file from the given directory
and then index it. 
"""
def extractdataSetToIndex( inputDataSet,es_object, index_name ):

    for filename in os.listdir(inputDataSet):

        if filename.endswith(".json"):
           
           indexing( os.path.join( inputDataSet,filename ),index_name, es_object )
            
           




             
