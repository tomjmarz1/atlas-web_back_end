#!/usr/bin/env python3
"""Simple flask app with index.html template"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """Route for `/`"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
