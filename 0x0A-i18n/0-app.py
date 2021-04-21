#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    """Template for 0-index with title and header"""
    return render_template('0-index.html',
                           title='Welcome to Holberton',
                           header='Hello world')
