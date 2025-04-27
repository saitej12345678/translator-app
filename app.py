from googletrans import Translator, LANGUAGES
from flask import Flask, render_template, request
app = Flask(__name__)
translator = Translator()
@app.route('/')
def home():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    Input_text = request.form['text']
    dest_lang = request.form['language']
    translated_text = translator.translate(text=Input_text, dest=dest_lang).text
    return render_template('index.html', translated_text=translated_text, languages=LANGUAGES,input_text=Input_text,
        selected_lang=dest_lang)
if __name__ == '__main__':
    app.run(debug=True)
