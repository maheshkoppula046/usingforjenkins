from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from audio_record import record_audio, audio_to_text
app = Flask(__name__)


@app.route("/")
def home():
    
    return render_template("home.html")

@app.route('/submit', methods=['POST'])
def submit():   
    file_name = record_audio()
    text = audio_to_text(file_name)

    print("Button clicked! Action performed.")
    return render_template('text.html',text=text)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)