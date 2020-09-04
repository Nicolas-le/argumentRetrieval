import ijson
from elasticsearch import  helpers
from get_doc_structure import * 


def process_jsonfile( filepath ):
    """
    Subfunction to open a JSON document and return it as a python dictionary.
    :param filepath:    filepath to the JSON file
    :return:               
    """
    try:
        json_file = open(filepath, encoding= 'utf-8')
        documents = ijson.items( json_file, 'arguments.item' )
        return documents
    except Exception as ex:
        print( 'Error loading file' )
        print( str(ex) )


def bulk_json_data( json_file ,index_name ):
    """
    Generator to push bulk data from a JSON file into an Elasticsearch index.
    :param json_file:   the JSON file with the data to get indexed 
    :param index_name:  the name of the index to store the data
    :return:      
    """
    print("start Indexing "+ json_file )
    json_list = process_jsonfile( json_file )
    for doc in json_list:
        # use a `yield` generator so that the data
        # isn't loaded into memory
         yield {
                  "_index": index_name,
                  "_id": doc['id'],
                  "_source": get_document_structure( doc )
           }

    
def indexing( filePath, index_name, index_object ):
    """
    Indexes a given file.
    :param filePath:        the JSON file with the data to get indexed 
    :param index_name:      the name of the index to store the data
    :param index_object:    connection to the elasticsearch cluster
    :return:
    """
    gen = bulk_json_data( filePath, index_name )
    print("Now indexing...")
    helpers.bulk(index_object, gen)
    print("Done indexing.")
       






