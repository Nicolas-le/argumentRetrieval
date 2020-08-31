from elasticsearch import Elasticsearch
from connect_to_elasticsearch import connect_to_elasticsearch
from indices import * 


def delete_indices( index_object, index_name, appx_start, appx_end ): 
    """
    Deletes a given index by its name and the possibility to get rid of its iterations at the same time, if the appendixis are numbers
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  main name of the index which will get deleted
    :param appx_start:  number where the iteration of the indexname should start the annihilation process
    :param appx_end:    number where the iteration annihilation should stop
    :return:             
    """
    if index_object.indices.exists( index_name ):
            index_object.indices.delete( index=index_name )
            print( index_name + ' successfully deleted' )
    else:
        print( 'no index ' + index_name + ' exists' )

    for i in range( appx_start, appx_end+1 ):
        index = index_name + str(i)
        if index_object.indices.exists( index ):
            index_object.indices.delete( index=index )
            print( index_name + str(i) + ' successfully deleted' )
        else:
            print( 'no index ' + index_name + str(i) + ' exists' )


"""
index_object = connect_to_elasticsearch()
index_name = 'testindex'
appendixnr_start = 0
appendixnr_end = 0
delete_indices( index_object, index_name, appendixnr_start, appendixnr_end )
"""








"""
delets indices based on the given indices names  
"""

def deleteAllindicies( indicies, index_object ):

    for index in indicies:
        if index_object.indices.exists( index ):
           index_object.indices.delete (index )
           print( index + ' has been succefally deleted!' )
 
        else:
            print( index + ' does not exist!' )


index_object = connect_to_elasticsearch()
indicies = getAllIndiciesNames()
deleteAllindicies( indicies, index_object )

