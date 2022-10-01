from flask import Flask, render_template, request
import json
# import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
#from dotenv import load_dotenv

#load_dotenv()


app = Flask("Web Translator")

apikey = "Xa3MnyLFGi3PfYkMAJirHDC0B736-LeDgES7MOwXADLr"
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/dedee887-4197-49cd-a125-bf7e5a87586f"

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2022-09-12',
    authenticator=authenticator
)
lt.set_service_url(url)

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('Hello, where are you going to')
    translator = lt.translate(
        text = textToTranslate,
        model_id = 'en-fr').get_result()
    french_text = json.dumps(translator, indent=2, ensure_ascii=False)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get("Bonjour, où vas-tu")
    translator = lt.translate(
        text = textToTranslate,
        model_id = 'fr-en').get_result()
    english_text = json.dumps(translator, indent=2, ensure_ascii=False)
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)