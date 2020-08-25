from xml.dom import minidom
import os 

def process_xml(topics_xml):

   print("start processing the topics")
   print("LOADING TOPICS")


   mydoc = minidom.parse(os.path.join(topics_xml,'topics.xml'))

   topics = mydoc.getElementsByTagName('topic')

   print('\nAll item data: ')

   topic_dic= []

   for topic in topics:

       number = topic.getElementsByTagName('number')[0]

       print("topic Number:",number.childNodes[0].data)

       title = topic.getElementsByTagName('title')[0]

       print("title:",title.childNodes[0].data)

       single_topic_dic = {"topic_number" : number.childNodes[0].data, "topic_query": title.childNodes[0].data }

       topic_dic.append(single_topic_dic)








