from flask import Flask, render_template, request, redirect, url_for
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



@app.route("/englishToFrench", methods=['POST', 'GET'])
def nglishToFrench():
    #textToTranslate = request.args.get(text)
    if request.method == 'POST':
        text = request.form.get('text')
        translator = lt.translate(
            text = text,
            model_id = 'en-fr').get_result()
        french_text = json.dumps(translator, indent=2, ensure_ascii=False)
    return french_text


@app.route("/frenchToEnglish")
def frenchToEnglish():
    #textToTranslate = request.args.get()
    translator = lt.translate(
        text = request.form.get('text'),
        model_id = 'fr-en').get_result()
    english_text = json.dumps(translator, indent=2, ensure_ascii=False)
    return english_text




@app.route("/", methods=['POST', 'GET'])
def renderIndexPage():
    def englishToFrench():
    #textToTranslate = request.args.get(text)
        if request.method == 'POST':
            text = request.form.get('text')
            translator = lt.translate(
                text = text,
                model_id = 'en-fr').get_result()
            french_text = json.dumps(translator, indent=2, ensure_ascii=False)
        return french_text
    
    def frenchToEnglish():
        if request.method == 'POST':
            text = request.form.get('text')
    #textToTranslate = request.args.get()
            translator = lt.translate(
                text = text,
                model_id = 'fr-en').get_result()
            english_text = json.dumps(translator, indent=2, ensure_ascii=False)
        return english_text
    
    return render_template('index.html', text=englishToFrench(), text2=frenchToEnglish())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)