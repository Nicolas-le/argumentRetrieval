from operator import itemgetter
from distances import bias_distance, stylo_distance
from compare_topics import topic_match_count
from calculate_new_score import calculate_new_score


def ranking_results( list_of_results, query_scores ):
    """
    Reranks search results by including bias score, stylometric scores and hidden topics.
    :param list_of_results:     list of search results already ranked by elasticsearch
    :query_scores:              custom scores of the search query
    :return:                    list of search results, ranked by their custom scores in relation to the custom scores of the search query 
    """
    query_bias_score = query_scores[ 'bias_score' ]
    query_stylo_scores = query_scores[ 'stylo_scores' ]
    query_topics = query_scores[ 'topics' ]

    old_rank = 0
    for doc in list_of_results:
        doc_bias_score = doc[ 'nlp_scores' ][ 'bias_score' ]
        doc_stylo_scores = doc[ 'nlp_scores' ][ 'stylo_scores' ]
        doc_topics = doc[ 'nlp_scores' ][ 'topics' ]
        
        old_score = doc[ '_score' ]
        bias = bias_distance( query_bias_score, doc_bias_score )
        stylo = stylo_distance( query_stylo_scores, doc_stylo_scores )
        topic_count = topic_match_count( query_topics, doc_topics )
        old_rank += 1

        new_score = calculate_new_score( old_score, bias, stylo, topic_count )
        doc[ 'bias_distance' ] = bias
        doc[ 'stylo_distance' ] = stylo
        doc[ 'topic_match_count' ] = topic_count
        doc[ 'old_score' ] = old_score
        doc[ 'new_score' ] = new_score
        doc[ 'scoring_distance' ] = float(doc[ 'new_score' ]) - float(doc[ 'old_score' ])
        doc[ 'old_rank' ] = old_rank

    ranked_list_of_results = sorted( list_of_results, key=itemgetter( 'new_score' ), reverse=True )
    
    new_rank = 0
    for doc in ranked_list_of_results:
        new_rank += 1
        doc[ 'new_rank' ] = new_rank

    return ranked_list_of_results

