Bias and Arguments
===
## Using Natural Language Processing Approaches to Influence the Ranking of an Argument Retrieval Model.

This git repository documents the code base used in a custom argument retrieval system. The whole documentation can be found in the paper as quoted underneath.
___
#### Abstract
>Relying on the background of document retrieval systems, this paper presents an argument retrieval system. It uses state of the art python libraries to automatically process a data set of arguments from the args.me corpus and store them in a custom index. The system can perform the process of ranking and ordering a list of relevant documents in response to a user's query by comparing the request to the produced index of documents. The special focus is on the use of several NLP-based analyses, including topic signal modeling, stylometric analysis, and primarily bias detection. These methods will be used to influence the ranking of the search engine.

#### Acknowledgements
>EN: This work was realized as part of the course "Information Retrieval" (summer semester 2020) under the supervision of Jun.-Prof. Dr. Martin Potthast, Lukas Gienapp and Christopher Akiki at the University of Leipzig.
>
>DE: Diese Arbeit wurde im Rahmen des Kurses "Information Retrieval" (Sommersemester 2020) unter der Leitung von Jun.-Prof. Dr. Martin Potthast, Lukas Gienapp und Christopher Akiki an der Universität Leipzig realisiert.
___

#### Use

`git clone https://github.com/Nicolas-le/argumentRetrieval.git`

`cd argumentRetrieval`

`python main.py --i <source> --o <output-file>`

**source:** Link to directory, has to be structured in the same way as the args.me corpus [https://webis.de/data/args-me-corpus.html]

**output-file:** Link to directory with run.txt file existing in it.

**example:** `python main.py --i ./corpus --o ./run`