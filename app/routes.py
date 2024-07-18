from app import app
from flask import render_template, url_for, request, jsonify
import pandas as pd
import json
import plotly as pl
import plotly_express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

train = pd.read_csv('./app/data/processed_data/ccao_train_cleaned.csv').drop('Unnamed: 0', axis=1)

@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/build-a-model')
def model1():
    data_preview = train.head().to_html(classes='table table-striped table-bordered', index=False)
    return render_template('model1.html', title = 'Build-A-Model', data = data_preview, data_columns = train.columns.to_list())

@app.route('/train', methods=['POST'])
def train_model():
    data = request.json
    selected_features = data['features']

    X = train[selected_features]
    y = train['Sale Price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)
 
    return jsonify({'rmse' : rmse})

@app.route('/spam-vs-ham')
def model2():
    return render_template('model2.html', title = 'Spam vs. Ham')

@app.route('/natural-disaster-classifier')
def model3():
    return render_template('model3.html', title = 'Natural Disaster Classifier')