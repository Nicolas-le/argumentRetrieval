import json


def get_data( filepath_query, filepath_results ):
    """
    Loads and returns the data of the query and the data of the retrieved documents from files
    :param filepath_query:      filepath to the query data
    :param filepath_results:    filepath to the data of the retrieved documents
    :return:                    a tuple of the query data and the list of rerieved documents
    """
    with open( filepath_query, 'r' ) as query_file:
        query = json.load( query_file )
    
    query_text = query['query']['multi_match']['query']
    query_scores = query['nlp_scores']
    query_data = {
        'query_text' : query_text,
        'bias_score' : query_scores['bias_score'],
        'vocab_richness' : query_scores['stylo_scores']['vocab_richness'],
        'hapax_legomena' : query_scores['stylo_scores']['hepax_legomena'],
        'wordlength' : query_scores['stylo_scores']['readability_measures']['average_wordlength'],
        'sentlength' : query_scores['stylo_scores']['readability_measures']['average_sentlength'],
        'spelling_errors' : query_scores['stylo_scores']['spelling_errors'],
        'topics' : query_scores['topics']
    }

    with open( filepath_results ) as results_file:
        results = json.load( results_file )
    
    results_data = []
    for doc in results:
        argID = doc['_source']['argsMeID']
        premise = doc['_source']['premise']
        average_wordlength = doc['nlp_scores']['stylo_scores']['readability_measures']['average_wordlength']
        average_sentlength = doc['nlp_scores']['stylo_scores']['readability_measures']['average_sentlength']
        bias_score = doc['nlp_scores']['bias_score']
        bias_distance = doc['bias_distance']
        stylo_distance = doc['stylo_distance']
        topic_match_count = doc['topic_match_count']
        old_score  = doc['old_score']
        new_score = doc['new_score']
        scoring_distance = doc['scoring_distance']
        old_rank = doc['old_rank']
        new_rank = doc['new_rank']
        
        doc_data = {
            'argID' : argID,
            'premise' : premise,
            'wordlength' : average_wordlength,
            'sentlength' : average_sentlength,
            'bias_score' : bias_score,
            'bias_distance' : bias_distance,
            'stylo_distance' : stylo_distance,
            'topic_match_count' : topic_match_count,
            'old_score' : old_score,
            'new_score' : new_score,
            'scoring_distance' : scoring_distance,
            'old_rank' : old_rank,
            'new_rank' : new_rank
        }
        results_data.append( doc_data )

    data_tuple = ( query_data, results_data )
    return data_tuple


def get_just_results_data( filepath ):
    with open( filepath ) as results_file:
        results = json.load( results_file )
    
    results_data = []
    for doc in results:
        argID = doc['_source']['argsMeID']
        premise = doc['_source']['premise']
        average_wordlength = doc['nlp_scores']['stylo_scores']['readability_measures']['average_wordlength']
        average_sentlength = doc['nlp_scores']['stylo_scores']['readability_measures']['average_sentlength']
        bias_score = doc['nlp_scores']['bias_score']
        bias_distance = doc['bias_distance']
        stylo_distance = doc['stylo_distance']
        topic_match_count = doc['topic_match_count']
        old_score  = doc['old_score']
        new_score = doc['new_score']
        scoring_distance = doc['scoring_distance']
        old_rank = doc['old_rank']
        new_rank = doc['new_rank']
            
        doc_data = {
            'argID' : argID,
            'premise' : premise,
            'wordlength' : average_wordlength,
            'sentlength' : average_sentlength,
            'bias_score' : bias_score,
            'bias_distance' : bias_distance,
            'stylo_distance' : stylo_distance,
            'topic_match_count' : topic_match_count,
            'old_score' : old_score,
            'new_score' : new_score,
            'scoring_distance' : scoring_distance,
            'old_rank' : old_rank,
            'new_rank' : new_rank
        }
        results_data.append( doc_data )

    return results_data