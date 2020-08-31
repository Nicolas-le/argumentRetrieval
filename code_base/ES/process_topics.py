from xml.dom import minidom
import os 
from search_index import * 
from process_trec_format import * 



"""
processes the topics in the topics.xml file and extracts the
query, which has to be searched.
this ia an iterative process: it will be iterated over the list topics 
and search each one of them at a time. 
"""
def process_xml(es_object, index_name, inputDataSet, outputDir, value):

   print("start processing the topics")
   print("LOADING TOPICS")
   
   # parses the xml file , so we can processe it.
   mydoc = minidom.parse(os.path.join(inputDataSet,'topics.xml'))

   topics = mydoc.getElementsByTagName('topic')

   print('\nAll item data: ')


   for i in range( 3 ):
       number = topics[i].getElementsByTagName('number')[0]
       print("topic Number:", number.childNodes[0].data)
       title = topic[i].getElementsByTagName('title')[0]
       print("title:",title.childNodes[0].data)
       search_and_display( es_object, index_name, title.childNodes[0].data, number.childNodes[0].data, outputDir, value)
       
       

