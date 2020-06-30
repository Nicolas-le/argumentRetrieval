import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions,EmotionOptions,KeywordsOptions,ConceptsOptions,SentimentOptions, CategoriesOptions
import config

authenticator = IAMAuthenticator(config.api_key)

def analyze(tokens):

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator)

    natural_language_understanding.set_service_url(config.api_url)
    """
    #simple request
    response = natural_language_understanding.analyze(
        text=tokens,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True),
            keywords=KeywordsOptions(emotion=True, sentiment=True))).get_result()
    """
    response = natural_language_understanding.analyze(
        text=tokens,
        features=Features(
            entities=EntitiesOptions(
                emotion=True,
                sentiment=True,
                limit=15),
            emotion=EmotionOptions(
                targets= ['keyword1','keyword2']),
            keywords=KeywordsOptions(
                emotion=True,
                sentiment=True,
                limit=2),
            concepts=ConceptsOptions(
                limit=5),
            sentiment=SentimentOptions(
                targets=['stocks']),
            categories=CategoriesOptions())).get_result()

    print(json.dumps(response, indent=2))


sentence = "Well I had this weird dream. I thought that I might be an alien from outer space. What do you think about it?"
analyze(sentence)