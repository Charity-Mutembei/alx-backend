#!/usr/bin/env python3
"""
test 1
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    task 1 function
    """
    return render_template('0-index.html')
