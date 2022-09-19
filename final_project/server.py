from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('Hello, where are you going to')
    translation = lt.translate(
        text = textToTranslate,
        model_id = 'en-fr').get_result()
    french_text = json.dumps(translation, indent=2, ensure_ascii=False)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('Bonjour, où vas-tu')
    translation = lt.translate(
        text = textToTranslate,
        model_id = 'fr-en').get_result()
    english_text = json.dumps(translation, indent=2, ensure_ascii=False)
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
