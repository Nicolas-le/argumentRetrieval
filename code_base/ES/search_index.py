import json
from elasticsearch import Elasticsearch
from connect_to_elasticsearch import connect_to_elasticsearch
from nlp_analysis import analyze
from ranking_results import ranking_results
from process_results import * 
from process_trec_format import * 


def search_index( es_object, index_name, topic_query,value ):
    """
    Searches a given index by a given query and presents the retrieved documents ranked by custom nlp scores. 
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  name of the index which will get searched
    :param query:       the query by which the index will get searched
    :return:            list of retrieved documents ranked by custom nlp scores
    """
    search_query = multi_match_search( topic_query,value )
    search_results = es_object.search( index=index_name, body=search_query, size=50,request_timeout=300 )
    print( 'Total of %d documents retrieved\n' % search_results['hits']['total']['value'] )

    list_of_results = [ doc for doc in search_results['hits']['hits'] ]
    
    results_scors= process_results( list_of_results ) 
    query_scores = analyze( topic_query )
    search_query['custom_scores'] = query_scores
    with open( './results/query.json', 'w' ) as file:
          json.dump( search_query, file, indent=4 )
    
    ranked_results = ranking_results( results_scors, query_scores )
    with open( './results/results.json', 'w' ) as file:
          json.dump( ranked_results, file, indent=4 )
    return list_of_results


# for multi-field full text search with the query analyzed in the same way as the idexed documents got analyzed
def multi_match_search( query, value ):
    """
    Defining the search process e.g. which fields should be searched and how acurate the query should match.
    :param query:   input search query
    :return:        dictionary which helds a defined search query for processing an index search
    """
    #search_query = {
        # 'query': {
           #  'multi_match': {
          #       'query' : query,
         #        'fields' : [ 'conclusion', 'premise', 'discussionTitle' ],
        #         'fuzziness' : 'AUTO',
       #          'tie_breaker' : 0.3
      #       }
     #    }
    # }
    
     
    search_query = {
           'query': {
               'bool': {
                  'must': {
                     'multi_match': {
                                       'fields': [
                                                       'conclusion',
                                                       'premise',
                                                       'discussionTitle',
                                                 ],
                                       'query' : query,
                                       'fuzziness' : 'AUTO',
                                       'tie_breaker' : 0.3


 
                                    }
               },
               'filter': {
                   'terms': {
                        'stance': [value] 
                   }
               }
          }
       }
   }




    return search_query


def search_and_display( es_object, index_name, topic_query, topic_number, outputDir, value ):
    """
    Entry function for an index search. Takes in the input query an displays the search results. 
    :param es_object:   connection to the elasticsearch cluster
    :param index_name:  name of the index which will get searched
    :param query:       the input query by which the index will get searched
    """
    ranked_results = search_index( es_object, index_name, topic_query,value )
    print( '\nDocuments reranked by the comparisson of bias detection, stylometrics and hidden topics :\n' )
    print("topic_number,  Q0,  arg_ids,  score,  method "+"\n")
    #for doc in ranked_results:
    write_into_trec(ranked_results, topic_number,outputDir )
    
      #  print( 'New score: %f' % doc['new_doc_score'] )
      #  print( 'Original score: %f' % doc['_score'] )
      #  print( 'Title: %s' % doc['_source']['discussionTitle'] )
      #  print( 'Conclusion: %s' % doc['_source']['conclusion'] )
      #  print( 'Premise: %s' % doc['_source']['premise'] )
    





















