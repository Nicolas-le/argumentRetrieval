from load_data import get_data
from setter import *
from evaluade_rank_changes import rank_changes
from extract_notable_docs import extract_notable_docs
from investigate_notable_docs import investigate_notable_docs


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


def print_average_changes( doclist, jump_threshold ):
    """
    Initiates an evaluation of average values of a set of documents as well as notable documents, which changed ranks above a given threshold value  
    :param documents:           list of documents 
    :param jump_threshold:      threshold value
    :return:                    
    """
    rank_tuple = rank_changes( doclist, jump_threshold )
    average_changes = rank_tuple[0]
    max_change_up = rank_tuple[1]
    max_change_down = rank_tuple[2]
    tendency = rank_tuple[3]
    notable_docs = rank_tuple[4]
    print( f'Average: {average_changes} Max rank up: {max_change_up} Max rank down: {max_change_down} Tendency: {tendency:.2f} ' )

    investigate_notable_docs( notable_docs )


filepath_query = 'results\query_topic1.json'
filepath_results = 'results\\results_custom_topic1.json'
data_tuple = get_data( filepath_query, filepath_results )

doclist = data_tuple[1]
jump_threshold = 10

print_average_changes( doclist, jump_threshold )




