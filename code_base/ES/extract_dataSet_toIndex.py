import os
from indexing import *


def extractdataSetToIndex( inputDataSet, es_object, index_name ):
    """
    extracts every json file from the given directory (usually base_code/corpus) and then indexes it.
    :param inputDataSet:    path to the directory
    :param es_object:       connection to elastic search cluster
    :param index_name:      name of the index
    :return: 
    """
    for filename in os.listdir( inputDataSet ):
        if filename.endswith( ".json" ):
           indexing( os.path.join( inputDataSet, filename ), index_name, es_object )
            
           




             
