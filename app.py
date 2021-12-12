from flask import Flask
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np
import pickle
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

if __name__ == '__main__':
   app.run(debug = True)