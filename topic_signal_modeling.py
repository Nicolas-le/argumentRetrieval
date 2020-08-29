from empath import Empath
import nltk
import json

def ts_mod(tokens):
    """
    This function implements the topic signal approach of Empath. Empath uses a trained (Neuronal Networks) word category list with the aim to detect topic signals in tokenized text. It then sorts the topics by value and shortlist it to the 10 highest ranked topics.
    :param tokens:  tokenized list of words f.ex.: ["cheese","fighting","dog","cold","man","war"]
    :return:        dictionary (created by empath) shortlist of the 10 highest ranked topics - key: detected topic / value: calculated value of importance
    """
    lexicon = Empath()
    lexicon = lexicon.analyze(tokens,normalize=True)

    #check if there are detected topics, if not return
    if lexicon == None:
        return

    topics = threshold_filter(lexicon)
    topics_sorted = sort_topics_by_value( topics )
    topics_shortlist = shortlist_topics( topics_sorted )

    return topics_shortlist


def threshold_filter(lexicon):
    """
    Implements a threshold for empath values and filters all detected topics below the threshold value. Used to filter irrelevant topics.
    :param lexicon:     dictionary created with empath
    :return:            the filtered dictionary lexicon
    """
    threshold = 0.001 #hardcoded for now
    lexicon = { k: v for k,v in lexicon.items() if v >= threshold }
    return lexicon


def sort_topics_by_value( lexicon ):
    """
    Sorts the dictionary of topics descending by their value.
    :param lexicon:     filtered dictionary of topics created with empath
    :return:            sorted dictionary of them topics
    """
    lexicon_sorted = { k: v for k, v in sorted( lexicon.items(), key=lambda item: item[1], reverse=True) }
    return lexicon_sorted


def shortlist_topics( lexicon ):
    """
    Creates a shortlist of the 10 most important topics of a dictionary of sorted topics.
    :param lexicon:     sorted dictionary of topics created with empath
    :return:            shortlist dictionary of the 10 most important topics
    """
    lexicon_shortlist = dict( list( lexicon.items() )[:10] )
    return lexicon_shortlist


"""
sentence = "Ernest Hemingway said about bullfighting that it is \"a decadent art in every way [...] if it were permanent it could be one of the major arts.\"(9) Bullfighting should thus not be understood as simply a 'bloodsport' with some cultural connotations but rather as an inherently cultural art form. The poet Garcia Lorca said in the 1930s that bullfighting is \"the last serious thing in the modern world\".(10) In many ways the seriousness of watching a life-and-death struggle in the arena is nothing short of poetic and this significance is perceived not only by the audience and the bullfighting community but in the wider culture of the nations which currently permit bullfighting. Robert Elms argued in 2010 that, in nations which do not practice bullfighting, \u201cOur squeamishness means that we prefer death which is mechanical and invisible, while the Spanish understand that it is part of a cycle.[...] It is a public celebration of death (a subject we prefer to hide from in Britain) which, when it is done well, becomes a celebration of life. The man charged with the task of delivering a fine end to this fierce and powerful creature will dance with it along the way, laying his own life on the line to create a swirling symbiosis.\"(10) Hemmingway echoed this, arguing that bullfighting promoted an understanding of violent death: \"The only place where you could see life and death, i. e., violent death now that the wars were over, was in the bull ring and I wanted very much to go to Spain where I could study it. I was trying to learn to write, commencing with the simplest things, and one of the simplest things of all and the most fundamental is violent death.\"(9) This is why Madrid and other places have protected and recognized bullfighting as an art form, not just a sport.(1) The understanding and cultural value in the bullfighting nations stems from their long history of the practice. Bullfighting traces its roots to prehistoric bull worship and sacrifice. The killing of the sacred bull (tauroctony) is the essential central iconic act of Mithras, which was commemorated in the mithraeum wherever Roman soldiers were stationed. The oldest representation of what seems to be a man facing a bull is on the celtiberian tombstone from Clunia and the cave painting \"El toro de hachos\", both found in Spain.(8) The continuity of the modern bullfights with these ancient commemorations is shown by the fact that in Spain, many youth idealize bull fighters for their strength, grace, and wit in outmaneuvering bulls.(10) This is valuable in inspiring and compelling success in future generations. Bullfighting is a genuinely popular and enjoyed cultural art form in many nations: Spanish bullrings are not kept alive by tourists. Rather, despite the economic recession which has hit Spain especially hard, the bullfights are still thriving, its top practitioners are huge stars, and its fan are intensely devoted, because it is still the very soul of this dark and complex country. Bullfighting thrives because its local fans are dedicated, and they are dedicated because they perceive its poetry and value to the culture.(10) Thus bullfighting has a cultural value which trumps misplaced concerns regarding 'animal rights', especially as 'animal rights' are simply a concept created by each culture and defined in different ways. Culturally, it is acceptable in the West to eat meat, and so this is legal even though it causes cows to suffer and die. Similarly, the culture of the bullfighting countries places a value upon the bullfight, thus privileging it above the 'rights' of the animal. To allow the moral qualms of other non-bullfighting cultures to dictate cultural practices in Spain or Mexico would be to privilege these other cultures' values above those of bullfighting nations, and deprive them of part of their uniqueness. As Robert Elms argues, if the bullfight dies out due to the pressure of other cultures' moral qualms, bullfighting nations will become \"more like everywhere else, dominated by gaudy globalism and neutered by the homogenising forces of technology and accepted taste.\"(10)"
tokens = nltk.word_tokenize(sentence)
print(ts_mod(tokens))
"""