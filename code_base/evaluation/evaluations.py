from load_data import get_data
from setter import *
from evaluade_rank_changes import rank_changes
from extract_notable_docs import extract_notable_docs
from investigate_notable_docs import investigate_notable_docs


filepath_query = 'results\query_topic2.json'
filepath_results = 'results\\results_custom_topic2.json'

data_tuple = get_data( filepath_query, filepath_results )

r5 = first_5_documents( data_tuple[1] )
r10 = first_10_documents( data_tuple[1] )
r20 = first_20_documents( data_tuple[1] )
r50 = first_50_documents( data_tuple[1] )
r100 = data_tuple[1]

rank_tuple = rank_changes( r100, 10 )
notable_docs = rank_tuple[4] 

print( 'Rank changes:' )
rank_changes( r5, 10 )
rank_changes( r10, 10 )
rank_changes( r20, 10 )
rank_changes( r50, 10 )
rank_changes( r100, 10 )

print( '\n' + str( len(rank_tuple[4]) ) + ' notable documents:' )
investigate_notable_docs( rank_tuple[4] )




