import json
from elasticsearch import Elasticsearch

from connect_to_elasticsearch import connect_to_elasticsearch
from tokenizer import tokenize, stopword_removal
from bias_detection import bias_score
from stylometric_analysis import main_stylo
from topic_signal_modeling import ts_mod


def indexing( filepath, es_object, index_name ):
    documents = process_jsonfile( filepath )
    for doc in documents:
        document = process_document( doc )
        indexing_document( es_object, index_name, document )
    print( 'file successfully indexed' )


def process_jsonfile( filepath ):
    try:
        with open( filepath ) as json_file:
            documents = json.load( json_file )
        return documents
    except Exception as ex:
        print( 'Error loading file' )
        print( str(ex) )


def process_document( dict_object ):
    _conclusion = dict_object['conclusion']
    _premise = dict_object['premises'][0]['text']
    _stance = True
    if dict_object['premises'][0]['stance'] == 'CON':
        _stance = False
    if 'discussionTitle' in dict_object:
        _discussionTitle = dict_object['context']['discussionTitle']
    else: 
        _discussionTitle = dict_object['context']['topic']
    _sourceDomain = dict_object['context']['sourceDomain']
    if 'sourceUrl' in dict_object:
        _sourceUrl = dict_object['context']['sourceUrl']
    else:
        _sourceUrl = 'no url'

    tokens = tokenize( _premise )
    tokens_without_stopwords = stopword_removal( tokens )

    _bias_score = bias_score( _premise )
    _stylo_scores = main_stylo( tokens )
    _topics = ts_mod( tokens_without_stopwords )
    
    document = {
        'conclusion': _conclusion,
        'premise': _premise,
        'stance': _stance,
        'discussionTitle': _discussionTitle,
        'sourceDomain': _sourceDomain,
        'sourceUrl': _sourceUrl,
        'custom_scores' : {
            'bias_score' : _bias_score,
            'stylo_scores' : {
                'vocab_richness' : _stylo_scores[ 'vocab_richness' ],
                'hepax_legomena' : _stylo_scores[ 'hepax_legomena' ],
                'readability_measures' : {
                    'average_wordlength' : _stylo_scores[ 'readability_measures' ]['average_wordlength'],
                    'average_sentlength' : _stylo_scores[ 'readability_measures' ]['average_sentlength']
                },
                'spelling_errors' : _stylo_scores[ 'spelling_errors' ]
            },
            'topics' : _topics
        }   
    }
    return document


# function to finally index a given dict object in a given index
def indexing_document( es_object, index_name, document ):
    try:
        es_object.index( index=index_name, doc_type='_doc', body=document )
        print( 'document successfully indexed' )
    except Exception as ex:
        print( 'Error indexing data' )
        print( str(ex) )


"""
index_name = 'testindex'
document_filepath = 'documents/parliamentary/parliamentary'
es_object = connect_to_elasticsearch()
for i in range(1,2):
    filepath = document_filepath + str(i) + '.json'
    indexing( filepath, es_object, index_name )
"""