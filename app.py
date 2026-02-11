from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

translator_en_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
translator_fr_en = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["lang"]
        
        if lang == "en_fr":
            result = translator_en_fr(text)
        else:
            result = translator_fr_en(text)
        translation = result[0]['translation_text']
    
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)