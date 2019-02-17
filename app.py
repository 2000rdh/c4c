import os
from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('yikey.html')

@app.route('/about')
def about():
    return render_template('oof.html')

@app.route('/donate')
def donate():
    return render_template('charge.html')

@app.route('/email')
def email():
	return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)