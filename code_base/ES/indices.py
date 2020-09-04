from connect_to_elasticsearch import *


# returns the name of all indices in the elasticsearch server 
def getAllIndiciesNames():  
    indicies = set()
    for index in connect_to_elasticsearch().indices.get_alias( "*" ):
        indicies.add( index )
        print( index )
    return indicies
