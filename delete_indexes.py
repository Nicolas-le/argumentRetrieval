from elasticsearch import Elasticsearch

from connect_to_elasticsearch import connect_to_elasticsearch


def deleteIndexes( index_object, index_name, appx_start, appx_end ): 
    for i in range( appx_start, appx_end+1 ):
        index = index_name + str(i)
        if index_object.indices.exists( index ):
            index_object.indices.delete( index=index )
            print( index_name + ' successfully deleted' )
        else:
            print( 'no index ' + index_name + ' exists' )


#index_object = connect_to_elasticsearch()
#index_name = 'testindex'
#appendixnr_start = 1
#appendixnr_end = 2
#deleteIndexes( index_object, index_name, appendixnr_start, appendixnr_end )

# is working