from whoosh.fields import Schema, TEXT, NUMERIC , ID, STORED
from whoosh.analysis import StemmingAnalyzer
import os, os.path
from whoosh import index
from whoosh.query import Every
from whoosh.qparser import QueryParser
import csv
import time
from whoosh import scoring
start_time = time.time()

 #test 
def indexer():
   
    schema = Schema(topic_number=NUMERIC(stored=True),
                Q0= STORED,
                docID=ID(stored=True),
                DiscussionID =ID(stored=True), 
                content=TEXT(analyzer=StemmingAnalyzer()),
                )

    if not os.path.exists(r"C:\Users\User\Desktop\index"):
        os.mkdir(r"C:\Users\User\Desktop\index")
    if not index.exists_in(r"C:\Users\User\Desktop\index",indexname=None):  
         ix = index.create_in(r"C:\Users\User\Desktop\index", schema)
         writer = ix.writer()
         with open('arguments.csv', encoding="utf8", newline='') as csvfile:
              reader = csv.DictReader(csvfile) # read rows into a dictionary format
              for row in reader:
                  writer.add_document(topic_number = row['Topic ID'], Q0="Q0", docID = row['Argument ID'], DiscussionID = row['Discussion ID'],
                                content = row['Premise'] )
         writer.commit()
         searcher(ix)
   

    else:
        ix = index.open_dir(r"C:\Users\User\Desktop\index")
        searcher(ix)
        
        

   
   




 


def searcher(indexer):
    with indexer.searcher(weighting = scoring.BM25F) as searcher:
        qp = QueryParser("content", schema= indexer.schema)
        q = qp.parse(u"Minimum Wage")
        
        results = searcher.search(q)
        
        for result in results:
            print(result)

    print("My program took", time.time() - start_time, "to run")


 
indexer()





