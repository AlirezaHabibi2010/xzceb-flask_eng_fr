"""Translatior"""
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-11-04',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """english To French"""

    french_text = language_translator.translate(
            text = english_text,
            model_id='en-fr'
            ).get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """french To English"""
    english_text = language_translator.translate(
            text = french_text,
            model_id='fr-en'
            ).get_result()
    return english_text.get("translations")[0].get("translation")

if __name__=='__main__':
    print(english_to_french('Hello'))
    print(french_to_english('Bonjour'))
