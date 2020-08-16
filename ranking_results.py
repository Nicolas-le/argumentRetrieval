from operator import itemgetter

from distances import bias_distance, stylo_distance
from compare_topics import topic_match_count
from calculate_new_score import calculate_new_score


def ranking_results( list_of_results, query_scores ):
    """
    Reranks the search results by 
    :param list_of_results:    list of search results with custom scores, ranked by elasticsearch
    :query_scores:             custom scores of search query
    :return:                   list of search results, ranked by custom score matches with search query 
    """
    
    query_bias_score = query_scores[ 'custom_scores' ][ 'bias_score' ]
    query_stylo_scores = query_scores[ 'custom_scores' ][ 'stylo_scores' ]
    query_topics = query_scores[ 'topics' ]

    for doc in list_of_results:
        doc_bias_score = doc[ 'custom_scores' ][ 'bias_score' ]
        doc_stylo_scores = doc[ 'custom_scores' ][ 'stylo_scores' ]
        doc_topics = doc[ 'topics' ]

        bias_distance = bias_distance( query_bias_score, doc_bias_score )
        stylo_distance = stylo_distance( query_stylo_scores, doc_stylo_scores )
        topic_match_count = topic_match_count( query_topics, doc_topics )

        new_doc_score = calculate_new_score( bias_distance, stylo_distance, topic_match_count )
        doc[ 'new_doc_score' ] = float( new_doc_score )

    ranked_list_of_results = sorted( list_of_results, key=itemgetter( 'new_doc_score' ) )
    
    return ranked_list_of_results

