from elasticsearch import Elasticsearch


def connect_to_elasticsearch():
    es_object = Elasticsearch( [ { 'host': 'localhost', 'port': 9200 } ] ) # create ES object
    if es_object.ping(): # tests connection
        print( 'Connection established' ) 
        return es_object
    else:
        print( 'No connection' )
        

# connect_to_elasticsearch()
# is working