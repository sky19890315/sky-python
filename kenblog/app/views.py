from flask import render_tmplate
from app import app


@app.route('/')
def index():
    return 'Hello world'