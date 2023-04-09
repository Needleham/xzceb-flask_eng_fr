import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(englishText):
    #Check for None input
    if englishText is None:
        return ""
    '''Translate English to French Text'''
    french_text = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    englishtranslation = french_text.get('translations')[0].get('translation')
    return englishtranslation


def french_to_english(frenchText):
    #Check for None input
    if frenchText is None:
        return ""
    '''Translate French to English Text'''
    english_text = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    frenchtranslation = english_text.get('translations')[0].get('translation')
    return frenchtranslation
