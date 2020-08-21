import json
from elasticsearch import Elasticsearch
from connect_to_elasticsearch import connect_to_elasticsearch
from nlp_analysis import analyze
from ranking_results import ranking_results


def search_index( es_object, index_name, query ):
    """
    Searches a given index by a given query and presents the retrieved documents ranked by custom nlp scores. 
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  name of the index which will get searched
    :param query:       the query by which the index will get searched
    :return:            list of retrieved documents ranked by custom nlp scores
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
    with open( 'results/results.json', 'w' ) as file:
        json.dump( ranked_results, file, indent=4 )

    return ranked_results


# for multi-field full text search with the query analyzed in the same way as the idexed documents got analyzed
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


def search_and_display( es_object, index_name, query ):
    """
    Entry function for an index search. Takes in the input query an displays the search results. 
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  name of the index which will get searched
    :param query:       the input query by which the index will get searched
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


es_object = connect_to_elasticsearch()
index_name = 'testindex1'
query = 'is a strong police force good?'
search_and_display( es_object, index_name, query )
