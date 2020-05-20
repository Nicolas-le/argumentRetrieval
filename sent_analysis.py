from textblob import TextBlob as tb

def sent_analysis(text):
    """
    Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1
    means a negative statement. Subjective sentences generally refer to personal opinion,
    emotion or judgment whereas objective refers to factual information. Subjectivity is
    also a float which lies in the range of [0,1].
    :param source: Untokenized String f.ex.: "Hello my sweet little search engine"
    :return:       blob.sentiment as Sentiment(polarity=x, subjectivity=y) Access: blob.sentiment.polarity
    """

    blob = tb(text)

    return blob.sentiment
