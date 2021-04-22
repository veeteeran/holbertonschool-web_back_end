#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """Template for 0-index with title and header"""
    return render_template('0-index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=True)
