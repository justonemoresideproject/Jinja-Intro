from flask import Flask, request, render_template
from random import randint, choice, sample

app = Flask(__name__)

@app.route('/hello')
def index():
    """Shows Hello Page"""
    return render_template('hello.html')

@app.route('/lucky')
def lucky_number():
    num = randint(1, 20)
    return render_template('lucky.html', lucky_num=num, msg='You are so lucky!')

@app.route('/form')
def show_form():
    return render_template('form.html')

COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)

@app.route('/form-2')
def show_form_2():
    return render_template('form2.html')

@app.route('/greet-2')
def get_greeting2():
    username = request.args["username"]
    wants_compliments = request.args.get["wants_compliments"]
    nice_thing = sample(COMPLIMENTS, 3)
    return render_template('greet2.html', username=username, wants_compliments=wants_compliments, compliment=nice_thing)

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)