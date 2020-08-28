import ijson
from elasticsearch import  helpers
from get_doc_structure import * 




'''
this function opens a file and returns its
contents as a list of json items
'''
def process_jsonfile( filepath ):
    """
    Subfunction to open a JSON document and return it as a dictionary.
    :param filepath:    filepath to the JSON file
    :return:            dictionary with the structure of the JSON file               
    """
    try:
        json_file = open(filepath, encoding= 'utf-8')
        documents = ijson.items( json_file, 'arguments.item' )
        return documents
    except Exception as ex:
        print( 'Error loading file' )
        print( str(ex) )





"""
generator to push bulk data from a JSON
file into an Elasticsearch index
"""
def bulk_json_data( json_file ,index_name ):
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
     
"""
index the given file  
"""
def indexing( filePath, index_name, index_object ):

   gen = bulk_json_data( filePath, index_name )
   print("Now indexing...")
   helpers.bulk(index_object, gen)
   print("Done indexing.")
       






