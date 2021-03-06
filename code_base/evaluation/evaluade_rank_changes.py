from extract_notable_docs import extract_notable_docs


def rank_changes( documents, min_jump_distance ):
    """
    Investigates rank changes by how big a rank change might be, the maximum rank jumps in both directions, the tendency in which direction most of the rank jumps happens and looks up all documents wich overcome a given jump threshold and gives back a tuple with all the data.
    :param documents:           list of documents to evaluate
    :param min_jump_distance:   minimum jump threshold value to extract notable documents which jumped ranks bigger than that number
    :return:                    tuple with all the evaluated data
    """
    
    count_changes = 0
    max_rank_distance_up = 0
    max_rank_distance_down = 0
    count_rank_up = 0
    count_rank_down = 0

    for doc in documents:
        rank_distance = doc['old_rank'] - doc['new_rank']

        count_changes += abs( rank_distance )

        if rank_distance > max_rank_distance_up:
            max_rank_distance_up = rank_distance
        elif rank_distance < max_rank_distance_down:
            max_rank_distance_down = rank_distance

        if rank_distance > 0:
            count_rank_up += 1
        elif rank_distance < 0:
            count_rank_down += 1

    average_rank_changes = count_changes / len( documents )
    max_rank_changes_up = max_rank_distance_up
    max_rank_changes_down = abs( max_rank_distance_down )
    tendency = 0
    if count_rank_up > count_rank_down and count_rank_down != 0:
        tendency = count_rank_up / count_rank_down
    elif count_rank_down > count_rank_up and count_rank_up != 0:
        tendency = count_rank_down / count_rank_up
    elif count_rank_up > count_rank_down and count_rank_down == 0:
        tendency = count_rank_up
    elif count_rank_down > count_rank_up and count_rank_up == 0:
        tendency = count_rank_down

    notable_docs = extract_notable_docs( documents, min_jump_distance )

    ranking_tuple = ( average_rank_changes, max_rank_changes_up, max_rank_changes_down, tendency, notable_docs, count_rank_up, count_rank_down )
    return ranking_tuple