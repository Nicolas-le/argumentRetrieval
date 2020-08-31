from nlp_analysis import analyze
from tokenizer import * 



"""
Subfunction to extract specific data out of a dictionary and form it into a dictionary which fits the mapping of the index.
:param dict_object:     dictionary with raw data
:return:                dictionary with structured data fitting the mapping of the indey
"""
def get_document_structure( dict_object ):
    
    _id = dict_object['id']
    _conclusion = dict_object['conclusion']
    _premise = dict_object['premises'][0]['text']
    _stance = True
    if dict_object['premises'][0]['stance'] == 'CON':
        _stance = False
    if 'discussionTitle' in dict_object['context']:
        _discussionTitle = dict_object['context']['discussionTitle']
    elif 'topic' in dict_object['context']: 
        _discussionTitle = dict_object['context']['topic']
    else:
         _discussionTitle = 'none'

    #custom_scores = analyze( _premise )

    document = {
        'id': _id,
        'discussionTitle': _discussionTitle,
        'conclusion':  _conclusion,
        'premise':     _premise,
        'stance': _stance
    }
    return document






