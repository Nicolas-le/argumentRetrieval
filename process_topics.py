from xml.dom import minidom
import os 
from search_index import * 

def process_xml(es_object, index_name, inputDataSet,outputDir):

   print("start processing the topics")
   print("LOADING TOPICS")

   mydoc = minidom.parse(os.path.join(inputDataSet,'topics.xml'))

   topics = mydoc.getElementsByTagName('topic')

   print('\nAll item data: ')


   for topic in topics:

       number = topic.getElementsByTagName('number')[0]

       print("topic Number:",number.childNodes[0].data)

       title = topic.getElementsByTagName('title')[0]

       print("title:",title.childNodes[0].data)

       search_and_display( es_object, index_name, title.childNodes[0].data, number.childNodes[0].data, outputDir )
       

