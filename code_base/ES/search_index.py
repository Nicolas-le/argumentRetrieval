import json
from elasticsearch import Elasticsearch
from connect_to_elasticsearch import connect_to_elasticsearch
from nlp_analysis import analyze
from ranking_results import ranking_results
from process_results import * 
from process_trec_format import * 


def multi_match_search( query ):
    """
    Defining the search process e.g. which fields should be searched and how acurate the query should match.
    :param query:   input search query
    :return:        dictionary which helds a defined search query for processing an index search
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


def search_index( es_object, index_name, query, search_nr ):
    """
    Searches a given index by a given query and returns the retrieved documents ranked by custom nlp scores. 
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  name of the index which will get searched
    :param query:       the query by which the index will get searched
    :param search_nr:   number of the attempted search for evaluation file
    :return:            list of retrieved documents ranked by custom nlp scores
    """
    search_query = multi_match_search( query )
    search_results = es_object.search( index=index_name, body=search_query, size=100  )
    print( 'Total of %d documents retrieved\n' % search_results['hits']['total']['value'] )
   
    list_of_results = [ doc for doc in search_results['hits']['hits'] ]
    results_custom_ranking = customize_ranking( list_of_results, query, search_nr )
    
    return results_custom_ranking


def customize_ranking( list_of_results, query, search_nr ):
    """
    Analyze a search query and the retrieved documents by NLP and reranks the retrieved documents on that basis. 
    :param list_of_results:     list of retrieved documents ranked inside Elastic Search with BM25
    :param query:               the query by which the index will get searched
    :param search_nr:           number of the attempted search for evaluation files
    :return:                    list of retrieved documents ranked by custom nlp scores
    """
    print('analyzing query...')
    query_scores = analyze( query )
    es_query = multi_match_search( query )
    es_query['nlp_scores'] = query_scores
    print('output query')
    with open( 'code_base/evaluation/search_results/query' + '_topic' + str(search_nr) + '.json', 'w' ) as file:
        json.dump( es_query, file, indent=4 )

    print('analyzing retrieved documents...')
    count = 0
    for doc in list_of_results:
        count += 1
        print( 'analyzing document ' + str(count) )
        nlp_scores = analyze( doc['_source']['premise'] )
        doc['nlp_scores'] = nlp_scores

    print('ranking retrieved documents...')
    results_custom_ranking = ranking_results( list_of_results, query_scores )
    print('output custom ranked documents')
    with open( 'code_base/evaluation/search_results/results_custom' + '_topic' + str(search_nr) + '.json', 'w' ) as file:
        json.dump( results_custom_ranking, file, indent=4 )
    
    return results_custom_ranking


def search_and_display( es_object, index_name, topic_query, topic_number, outputDir ):
    """
    Entry function for an index search. Takes in the input query an initilize an index search. 
    :param es_object:       connection to the elasticsearch cluster
    :param index_name:      name of the index which will get searched
    :param topic_query:     the input query by which the index will get searched
    :param topic_number:    number of the attempted search for evaluation files
    :param outputDir:       directory for output of trec record
    """
    print( 'topic_query: %s' % topic_query )
    print( 'topic_number: %s' % topic_number )
    
    ranked_results = search_index( es_object, index_name, topic_query, topic_number )
    write_into_trec( ranked_results, topic_number, outputDir )
    print( '\nDocuments reranked by the comparisson of bias detection, stylometrics and hidden topics.\n' )
    






















