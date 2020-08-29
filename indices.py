from connect_to_elasticsearch import *


def getAllIndiciesNames():  
    indicies = set()
    for index in connect_to_elasticsearch().indices.get_alias( "*" ):
        indicies.add( index )
        print( index )
    return indicies     


getAllIndiciesNames()
