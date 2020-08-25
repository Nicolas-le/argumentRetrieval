import json
import ijson
from elasticsearch import Elasticsearch
from connect_to_elasticsearch import connect_to_elasticsearch
from nlp_analysis import analyze


def indexing( filepath, es_object, index_name ):
    """
    Main function to organize the whole indexing process of a JSON file.
    :param filepath:    filepath to the JSON file
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  name of the index in which the document will be indexed
    :return:             
    """
    documents = process_jsonfile( filepath )
    print( len(documents) )
    counter = 0
    for doc in documents:
        document = process_document( doc )
        indexing_document( es_object, index_name, document )
        counter += 1
        print( counter )
    print( 'file successfully indexed' )


def process_jsonfile( filepath ):
    """
    Subfunction to open a JSON document and return it as a dictionary.
    :param filepath:    filepath to the JSON file
    :return:            dictionary with the structure of the JSON file               
    """
    try:
        with open( filepath ) as json_file:
            objects = ijson.items( json_file, 'arguments.item' )
            documents = list( objects )
        return documents
    except Exception as ex:
        print( 'Error loading file' )
        print( str(ex) )


def process_document( dict_object ):
    """
    Subfunction to extract specific data out of a dictionary and form it into a dictionary which fits the mapping of the index.
    :param dict_object:     dictionary with raw data
    :return:                dictionary with structured data fitting the mapping of the index
    """

    _conclusion = dict_object['conclusion']
    _premise = dict_object['premises'][0]['text']
    _stance = True
    _argsMeID = dict_object['id']
    if dict_object['premises'][0]['stance'] == 'CON':
        _stance = False
    if 'discussionTitle' in dict_object['context']:
        _discussionTitle = dict_object['context']['discussionTitle']
    elif 'topic' in dict_object['context']: 
        _discussionTitle = dict_object['context']['topic']
    else:
         _discussionTitle = 'none'
    _sourceDomain = dict_object['context']['sourceDomain']
    if 'sourceUrl' in dict_object['context']:
        _sourceUrl = dict_object['context']['sourceUrl']
    else:
        _sourceUrl = 'no url'

    custom_scores = analyze( _premise )

    document = {
        'conclusion': _conclusion,
        'premise': _premise,
        'stance': _stance,
        'argsMeID': _argsMeID,
        'discussionTitle': _discussionTitle,
        'sourceDomain': _sourceDomain,
        'sourceUrl': _sourceUrl,
        'custom_scores' : {
            'bias_score' : custom_scores[ 'bias_score' ],
            'stylo_scores' : {
                'vocab_richness' : custom_scores[ 'stylo_scores' ][ 'vocab_richness' ],
                'hepax_legomena' : custom_scores[ 'stylo_scores' ][ 'hepax_legomena' ],
                'readability_measures' : {
                    'average_wordlength' : custom_scores[ 'stylo_scores' ][ 'readability_measures' ]['average_wordlength'],
                    'average_sentlength' : custom_scores[ 'stylo_scores' ][ 'readability_measures' ]['average_sentlength']
                },
                'spelling_errors' : custom_scores[ 'stylo_scores' ][ 'spelling_errors' ]
            },
            'topics' : custom_scores[ 'topics' ]
        }   
    }
    return document


# function to finally index a given dict object in a given index
def indexing_document( es_object, index_name, document ):
    """
    Subfunction to finally index a well formed document.
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  name of the index in which the document will be indexed
    :param document:    soon to be indexed document as a well formed dictionary 
    :return:             
    """
    try:
        es_object.index( index=index_name, doc_type='_doc', body=document )
        print( 'document successfully indexed' )
    except Exception as ex:
        print( 'Error indexing data' )
        print( str(ex) )


index_name = 'testindex3'
document_filepath = 'documents/parliamentary/parliamentary'
es_object = connect_to_elasticsearch()
for i in range(1,2):
    filepath = document_filepath + str(i) + '.json'
    indexing( filepath, es_object, index_name )

