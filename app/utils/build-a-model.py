import plotly.express as px
from jinja2 import Template
import pandas as pd
import os

train_data = pd.read_csv('../data/ccao_data/cook_county_train.csv')
print(train_data.head())