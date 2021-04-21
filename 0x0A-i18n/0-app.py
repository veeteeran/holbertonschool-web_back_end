#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('0-index.html',
                           title='Welcome to Holberton',
                           header='Hello world')
