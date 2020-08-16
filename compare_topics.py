
def topic_match_count( query_topics_dict, document_topics_dict ):
    """
    Compares the hidden topics of a query and a document and counts the matches.
    :query_topics_dict:     dictionary of the 10 highest ranked hidden query topics found by empath 
    :document_topics_dict:  dictionary of the 10 highest ranked hidden document topics found by empath
    :return:                the number of matches between these to lists of topics
    """
    counter = 0

    if query_topics_dict is not None and document_topics_dict is not None:
        query_topics = list( query_topics_dict.keys() )
        document_topics = list( document_topics_dict.keys() )
        for topic in query_topics:
            if topic in document_topics:
                counter += 1

    return counter