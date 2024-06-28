from app import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly as pl
import plotly_express as px

@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

