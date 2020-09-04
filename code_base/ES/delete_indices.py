from elasticsearch import Elasticsearch
from connect_to_elasticsearch import connect_to_elasticsearch
from indices import * 


"""
Deletes indices based on the given indices names.
:param indicies:        list of indicies to delete
:param index_object:    connection to the elastic search cluster
"""
def delete_indicies( indicies, index_object ):

    for index in indicies:
        if index_object.indices.exists( index ):
           index_object.indices.delete (index )
           print( index + ' has been succefally deleted!' )
        else:
            print( index + ' does not exist!' )


index_object = connect_to_elasticsearch()
indicies = getAllIndiciesNames()
delete_indicies( indicies, index_object )

