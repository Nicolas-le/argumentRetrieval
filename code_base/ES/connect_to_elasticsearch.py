from elasticsearch import Elasticsearch


def connect_to_elasticsearch():
    """
    Tests the connection to the elasticsearch cluster and returns it inside an elasticsearch object 
    :return:    elasticsearch object which contains the connection values to the cluster
    """
    es_object = Elasticsearch( [ { 'host': 'localhost', 'port': 9200 } ] ) # create ES object
    if es_object.ping(): # tests connection
        print( 'Connection established' ) 
        return es_object
    else:
        print( 'No connection' )