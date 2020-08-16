import json
from elasticsearch import Elasticsearch

from connect_to_elasticsearch import connect_to_elasticsearch


def create_index( es_object, index_name ):
    # sets the number of shards and a custom analyzer with selected tokenizer and filters
    settings = {
        'settings' : {
            'number_of_shards' : 1,
            'analysis' : {
                'analyzer' : {
                    'custom_analyzer' : {
                        'type' : 'custom',
                        'tokenizer' : 'standard',
                        'filter' : [
                            'asciifolding',
                            'classic',
                            'elision',
                            'lowercase',
                            'stop',
                            'kstem'
                        ]   
                    }
                },
            }
        },
        # creating the schema in form of mappings
        'mappings' : {
            'dynamic' : 'strict',
            'properties': {
                'discussionTitle' : { 
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer'
                },
                'conclusion' : { 
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer'
                },
                'premise' : { 
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer'
                },
                'stance' : { 
                    'type' : 'boolean', 
                    'index' : 'false' 
                },
                'sourceDomain' : { 
                    'type' : 'keyword', 
                    'index' : 'false' 
                },
                'sourceUrl' : { 
                    'type' : 'text', 
                    'index' : 'false' 
                }, 
                'custom_scores' : {
                    'dynamic' : 'strict',
                    'properties' : {
                        'bias_score' : {
                            'type' : 'double',
                            'index' : 'false'
                        },
                        'stylo_scores' : {
                            'dynamic' : 'strict',
                            'properties' : {
                                'vocab_richness' : {
                                    'type' : 'double',
                                    'index' : 'false'
                                },
                                'hepax_legomena' : {
                                    'type' : 'double',
                                    'index' : 'false'
                                },
                                'readability_measures' : {
                                    'dynamic' : 'strict',
                                    'properties' :{
                                        'average_wordlength' : {
                                            'type' : 'double',
                                            'index' : 'false'
                                        },
                                        'average_sentlength' : {
                                            'type' : 'double',
                                            'index' : 'false'
                                        }
                                    }
                                },
                                'spelling_errors' : {
                                    'type' : 'double',
                                    'index' : 'false'
                                }
                            }
                        },
                        'topics' : {
                            'type' : 'object',
                            'enabled' : 'false'
                        }
                    }
                }
            }
        }
    }  
    try:
        # tests if the index already exists
        if not es_object.indices.exists( index_name ):
            # creates the index
            index = es_object.indices.create( index=index_name, ignore=400, body=settings )
            print( index )
            print( 'Index created' )
        else:
            print( 'Index already exists' )
    except Exception as ex:
        print( str(ex) )

        
#index_object = connect_to_elasticsearch()
#index_name = 'testindex'
#create_index( index_object, index_name )

# is working