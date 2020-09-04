from load_data import get_data


def find_doc_by_id( doclist, docID ):
    """
    Searches for a document by its ID and presents it.
    :param doclist: list of documents to look through
    :param dicID:   the ID of the document to search for
    :return:                
    """
    for doc in doclist:
        argID = doc['argID']
        if argID == docID:
            print( doc['argID'] )
            print( doc['premise'] )