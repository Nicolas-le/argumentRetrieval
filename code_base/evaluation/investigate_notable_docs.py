def investigate_notable_docs( documents ):

    rank_up = []
    rank_down = []
    
    for doc in documents:
        rank = doc['new_rank']
        jump = doc['remarks']['jump_distance']
        bias = doc['bias_distance']
        stylo = doc['stylo_distance']
        print( f'rank: {rank} \tjump distance: {jump} \tbias distance: {bias:.2f} \tstylo distance: {stylo:.2f}' )

        if doc['remarks']['jump']:
            rank_up.append( doc )
        else:
            rank_down.append( doc )

    count_bias_rank_up = 0
    max_bias_rank_up = 0
    count_stylo_rank_up = 0
    max_stylo_rank_up = 0
    print( '\nup ranked documents:' )

    for doc in rank_up:    
        rank = doc['new_rank']
        jump = doc['remarks']['jump_distance']
        bias = doc['bias_distance']
        stylo = doc['stylo_distance']
        print( f'rank: {rank} \tjump distance: {jump} \tbias distance: {bias:.2f} \tstylo distance: {stylo:.2f}' )

        count_bias_rank_up += doc['bias_distance']
        if doc['bias_distance'] > max_bias_rank_up:
            max_bias_rank_up = doc['bias_distance']

        count_stylo_rank_up += doc['stylo_distance']
        if doc['stylo_distance'] > max_stylo_rank_up:
            max_stylo_rank_up = doc['stylo_distance']

    average_bias_rank_up = ( count_bias_rank_up - max_bias_rank_up ) / ( len( rank_up ) - 1 )
    average_stylo_rank_up = ( count_stylo_rank_up - max_stylo_rank_up ) / ( len( rank_up ) - 1 )
    print( f'\naverage bias distance: {average_bias_rank_up:.2f} \taverage stylo distance: {average_stylo_rank_up:.2f}' )

    count_bias_rank_down = 0
    min_bias_rank_down = 0
    count_stylo_rank_down = 0
    min_stylo_rank_down = 0
    print( '\ndown ranked documents:' )

    for doc in rank_down:
        rank = doc['new_rank']
        jump = doc['remarks']['jump_distance']
        bias = doc['bias_distance']
        stylo = doc['stylo_distance']
        print( f'rank: {rank} \tjump distance: {jump} \tbias distance: {bias:.2f} \tstylo distance: {stylo:.2f}' )

        count_bias_rank_down += doc['bias_distance']
        if doc['bias_distance'] < min_bias_rank_down:
            min_bias_rank_down = doc['bias_distance']
        
        count_stylo_rank_down += doc['stylo_distance']
        if doc['stylo_distance'] > min_stylo_rank_down:
            min_stylo_rank_down = doc['stylo_distance']
    
    average_bias_rank_down = ( count_bias_rank_down - min_bias_rank_down ) / ( len( rank_down ) - 1 )
    average_stylo_rank_down = ( count_stylo_rank_down - min_stylo_rank_down ) / ( len( rank_down ) -1 )
    print( f'\naverage bias distance: {average_bias_rank_down:.2f} \taverage stylo distance: {average_stylo_rank_down:.2f}' )

    notable_documents_analysis = ( average_bias_rank_up, average_stylo_rank_up, average_bias_rank_down, average_stylo_rank_down )
    return notable_documents_analysis