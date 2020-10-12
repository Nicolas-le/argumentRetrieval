from load_data import get_data, get_just_results_data
from setter import *
from evaluade_rank_changes import rank_changes
from extract_notable_docs import extract_notable_docs
from investigate_notable_docs import investigate_notable_docs
import os


def print_evaluation( doclist ):
    """
    Presents the data evaluation of a given list of documents. 
    :param documents:           list of documents to evaluate
    :return:                    
    """
    for doc in doclist:
        rank = doc['new_rank']
        argID = doc['argID']
        bias_score = doc['bias_score']
        bias_dist = doc['bias_distance']
        stylo_dist = doc['stylo_distance']
        old_rank = doc['old_rank']
        print( f'Rank: {rank} ID: {argID} Bias score: {bias_score:.2f} Bias distance: {bias_dist:.2f} Stylo distance: {stylo_dist:.2f} Rank before: {old_rank} ' )


def print_average_changes( data_tuple, first_x_docs, jump_threshold ):
    """
    Initiates an evaluation of average values of a set of documents as well as notable documents, which changed ranks above a given threshold value  
    :param documents:           list of documents 
    :param jump_threshold:      threshold value
    :return:                    
    """
    doclist = data_tuple[1]
    if first_x_docs == 5:
        doclist = first_5_documents( doclist )
    elif first_x_docs == 10:
        doclist = first_10_documents( doclist )
    elif first_x_docs == 20:
        doclist = first_20_documents( doclist )
    elif first_x_docs == 50:
        doclist = first_50_documents( doclist )
    query_topic = data_tuple[0]['query_text']
    query_bias = data_tuple[0]['bias_score']
    doc_count = len(doclist)
    rank_tuple = rank_changes( doclist, jump_threshold )
    average_changes = rank_tuple[0]
    max_change_up = rank_tuple[1]
    max_change_down = rank_tuple[2]
    tendency = rank_tuple[3]
    notable_docs = rank_tuple[4]
    count_rank_up = rank_tuple[5]
    count_rank_down = rank_tuple[6]
    changes_per_docs = ( count_rank_up + count_rank_down ) / len(doclist)


    with open( 'evaluation_results\\topic_evaluations.txt', 'a' ) as file:
        file.write( f'Topic: {query_topic} Bias: {query_bias}\nFirst {doc_count} documents\nDocuments ranked up: {count_rank_up}\nDocuments ranked down: {count_rank_down}\nAverage rank changes per doc in documentlist: {changes_per_docs:.2f}\nAverage rank change by: {average_changes:.2f}\nMaximum rank jump up: {max_change_up}\nMaximum rank jump down: {max_change_down}\nTendency of direcion: {tendency:.2f}\n\n' )
    print(len(notable_docs))
    investigate_notable_docs( notable_docs )


def print_average_changes_of_corpus( corpus, first_x_docs ):
    average_changes_sum = 0
    max_change_up_sum = 0
    max_change_down_sum = 0
    tendency_sum = 0
    count_rank_up_sum = 0
    count_rank_down_sum = 0
    changes_per_docs_sum = 0
    doclist_count = len(corpus)

    for doclist in corpus:
        rank_tuple = rank_changes( doclist, first_x_docs )
        average_changes_sum += rank_tuple[0]
        max_change_up_sum += rank_tuple[1]
        max_change_down_sum += rank_tuple[2]
        tendency_sum += rank_tuple[3]
        count_rank_up_sum += rank_tuple[5]
        count_rank_down_sum += rank_tuple[6]
        changes_per_docs_sum += ( rank_tuple[5] + rank_tuple[6] ) / len(doclist)
    
    average_changes = average_changes_sum / doclist_count
    max_change_up = max_change_up_sum / doclist_count
    max_change_down = max_change_down_sum / doclist_count
    tendency = tendency_sum / doclist_count
    count_rank_up = count_rank_up_sum / doclist_count
    count_rank_down = count_rank_down_sum / doclist_count
    changes_per_docs = changes_per_docs_sum / doclist_count

    with open( 'evaluation_results\corpus_evaluations.txt', 'a' ) as file:
        file.write( f'Corpus of {doclist_count} documentlists (queries)\nFirst {first_x_docs} documents of each list\nAverage of documents ranked up: {count_rank_up}\nAverage of documents ranked down: {count_rank_down}\nAverage rank changes per doc of documentlist: {changes_per_docs:.2f}\nAverage rank change by: {average_changes:.2f} ranks\nAverage maximum rank jump up: {max_change_up:.2f}\nAverage maximum rank jump down: {max_change_down:.2f}\nAverage tendency of direction: {tendency:.2f}\n\n' )   


filepath_query = 'search_results\query_topic25.json'
filepath_results = 'search_results\\results_custom_topic25.json'
data_tuple = get_data( filepath_query, filepath_results )

doclist = data_tuple[1]
jump_threshold = 5

listo = [5, 10, 20, 50, 100]
for nr in listo:
    print_average_changes( data_tuple, nr, jump_threshold )


"""
location = 'search_results\\'
filepaths = []

for root, directories, files in os.walk( location ):
    for item in files:
        if 'results' in item:
            filepaths.append( os.path.join( root, item ) )
corpus = []
for filepath in filepaths:
    all_data = get_just_results_data( filepath )
    #selected_data = first_50_documents( all_data )
    corpus.append( all_data )

print_average_changes_of_corpus( corpus, 100 )
"""