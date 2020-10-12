from xml.dom import minidom
import os 
from search_index import * 
from process_trec_format import * 


def process_xml( es_object, index_name, inputDataSet, outputDir ):
    """
    Processes the topics in the topics.xml file and extracts the query, which has to be searched.
    This ia an iterative process: it will be iterated over the topics.xml (or a similar one) in base_code/coprus and search each one of them at a time. 
    :param es_object:       connection to the elasticsearch cluster
    :param index_name:      name of the index
    :param inputDataSet:    path to the xml file (usually base_code/corpus)
    :param outputDir:       path to an output directory (usually base_code/run)
    :return:
    """
    print( "start processing the topics" )
    print( "LOADING TOPICS" )
    # parses the xml file , so we can processe it.
    mydoc = minidom.parse( os.path.join(inputDataSet,'topics.xml') )
    topics = mydoc.getElementsByTagName( 'topic' )

    print( '\nAll item data: ' )
    for i in range(0, 50 ):
        number = topics[i].getElementsByTagName('number')[0]
        print( "topic Number:", number.childNodes[0].data )
        title = topics[i].getElementsByTagName('title')[0]
        print( "title:", title.childNodes[0].data )
        search_and_display( es_object, index_name, title.childNodes[0].data, number.childNodes[0].data, outputDir )
       
       

