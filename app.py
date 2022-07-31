#import relevant libraries for flask, html rendering and loading the ML model

from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd
import joblib

app = Flask(__name__)


#model = pickle.load(open("model.pkl","rb"))
#scale = pickle.load(open("scale.pkl","rb"))

scale = joblib.load("scale.pkl")
model = joblib.load("model.pkl")

@app.route("/")
def landingPage():
    return render_template('index.html')