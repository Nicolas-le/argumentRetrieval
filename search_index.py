import json
from elasticsearch import Elasticsearch

from connect_to_elasticsearch import connect_to_elasticsearch
from tokenizer import tokenize, stopword_removal
from bias_detection import bias_score
from stylometric_analysis import main_stylo
from topic_signal_modeling import ts_mod
from ranking_results import ranking_results


def search_index( es_object, index_name, query ):
    """
    Searches a given index by a given query and presents the retrieved documents ranked by custom nlp scores. 
    :param es_object:    connection to the elasticsearch cluster
    :param index_name:   name of the index which will get searched
    :param query:        the query by which the index will get searched
    :return:             list of retrieved documents ranked by custom nlp scores
    """
    search_query = multi_match_search( query )
    search_results = es_object.search( index=index_name, body=search_query, size=100 )
    print( 'Total of %d documents retrieved\n' % search_results['hits']['total']['value'] )

    list_of_results = [ doc for doc in search_results['hits']['hits'] ]
    
    query_scores = analyze( query )
    search_query['custom_scores'] = query_scores
    with open( 'results/query.json', 'w' ) as file:
        json.dump( search_query, file, indent=4 )

    ranked_results = ranking_results( list_of_results, query_scores )
    return ranked_results


# for multi-field full text search with the query analyzed in the same way as the idexed documents got analyzed
def multi_match_search( query ):
    """
    Defining the search process by which fields should be searched and how acurate the query should match.
    :param query:   input search query
    :return:        a dictionary which helds a defined search query for processing an index search
    """
    search_query = {
        'query': {
            'multi_match': {
                'query' : query,
                'fields' : [ 'conclusion', 'premise', 'discussionTitle' ],
                'fuzziness' : 'AUTO',
                'tie_breaker' : 0.3
            }
        }
    }
    return search_query


def analyze( text ):
    """
    Analyzes a given text for bias, stylometrics and hidden topics and returns an object with all the scores.
    :param text:    a given text which will get analyzed
    :return:        a dictionary with all the nlp scores
    """
    tokens = tokenize( text )
    tokens_no_stopwords = stopword_removal( tokens )
    
    bias = bias_score( text )
    stylo_scores = main_stylo( tokens )
    topics = ts_mod( tokens_no_stopwords )
    
    scores = {
        'bias_score' : bias,
        'stylo_scores' : {
            'vocab_richness' : stylo_scores[ 'vocab_richness' ],
            'hepax_legomena' : stylo_scores[ 'hepax_legomena' ],
            'readability_measures' : {
                'average_wordlength' : stylo_scores[ 'readability_measures' ]['average_wordlength'],
                'average_sentlength' : stylo_scores[ 'readability_measures' ]['average_sentlength']
            },
            'spelling_errors' : stylo_scores[ 'spelling_errors' ]
        },
        'topics' : topics
    }   
    return scores


def search_and_display( es_object, index_name, query ):
    """
    Entry function for an index search. Takes in all the user input an displays the search results. 
    :param es_object:    connection to the elasticsearch cluster
    :param index_name:   name of the index which will get searched
    :param query:        the input query by which the index will get searched
    """
    ranked_results = search_index( es_object, index_name, query )

    print( 'Query: %s' % query )
    print( '\nDocuments reranked by the comparisson of bias detection, stylometrics and hidden topics :\n' )
    for doc in ranked_results:
        print( 'New score: %f' % doc['new_doc_score'] )
        print( 'Original score: %f' % doc['_score'] )
        print( 'Title: %s' % doc['_source']['discussionTitle'] )
        print( 'Conclusion: %s' % doc['_source']['conclusion'] )
        print( 'Premise: %s' % doc['_source']['premise'] )
        print( 'Source: %s\n' % doc['_source']['sourceUrl'] )



"""
es_object = connect_to_elasticsearch()
index_name = 'testindex'
query = 'is war in some cases necessary'
search_and_display( es_object, index_name, query )
"""