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
    train = pd.read_csv('./app/data/processed_data/ccao_train_cleaned.csv').drop('Unnamed: 0', axis=1)
    data_preview = train.head().to_html(classes='table table-striped table-bordered', index=False)
    return render_template('model1.html', title = 'Build-A-Model', data = data_preview)

@app.route('/spam-vs-ham')
def model2():
    return render_template('model2.html', title = 'Spam vs. Ham')

@app.route('/natural-disaster-classifier')
def model3():
    return render_template('model3.html', title = 'Natural Disaster Classifier')