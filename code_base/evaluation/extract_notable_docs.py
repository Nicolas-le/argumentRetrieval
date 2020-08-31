def extract_notable_docs( documents, min_jump_distance ):
    notable_docs = []
    max_rank_distance_up = 0
    max_rank_distance_down = 0

    for doc in documents:
        rank_distance = doc['old_rank'] - doc['new_rank']

        if rank_distance > max_rank_distance_up:
            max_rank_distance_up = rank_distance
        elif rank_distance < max_rank_distance_down:
            max_rank_distance_down = rank_distance
        
        if abs( rank_distance ) > min_jump_distance:
            jump = True
            if rank_distance < 0:
                jump = False

            doc['remarks'] = {
                'jump' : jump,
                'jump_distance' : rank_distance,
                'max_jump' : 0
            }
            notable_docs.append( doc )

    for doc in notable_docs:
        if doc['remarks']['jump_distance'] == max_rank_distance_up:
            doc['remarks']['max_jump'] = 1
        elif doc['remarks']['jump_distance'] == max_rank_distance_down:
            doc['remarks']['max_jump'] = -1

    return notable_docs