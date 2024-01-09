#!/usr/bin/python3
from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('0-index.html')
