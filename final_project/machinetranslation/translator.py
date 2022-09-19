import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2022-09-12',
    authenticator=authenticator
)
lt.set_service_url(url)


def english_to_french(input):
    translation = lt.translate(
    text = input('Enter a text here: '),
    model_id = 'en-fr').get_result()
    french_text = json.dumps(translation, indent=2, ensure_ascii=False)
    return french_text

english_to_french(input)

def french_to_english(input):
    translation = lt.translate(
    text = input('Entrez un texte ici: '),
    model_id = 'fr-en').get_result()
    english_text = json.dumps(translation, indent=2, ensure_ascii=False)
    return english_text

french_to_english(input)