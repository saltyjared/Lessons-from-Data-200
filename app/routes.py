from app import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly as pl
import plotly_express as px

@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/build-a-model')
def model1():
    return render_template('model1.html', title = 'Build-A-Model')

@app.route('/spam-vs-ham')
def model2():
    return render_template('model2.html', title = 'Spam vs. Ham')

@app.route('/natural-disaster-classifier')
def model3():
    return render_template('model3.html', title = 'Natural Disaster Classifier')