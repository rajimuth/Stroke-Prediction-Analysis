import joblib  #for importing your machine learning model
import numpy as np
import pandas as pd
# SQLALCHEMY SETUP
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, r_template, request, jsonify, make_response

#os allows you to call in environment variables
# we will set the remote environment variables in heroku 
from dotenv import load_dotenv
import os 

load_dotenv()

#################################################
# Database Setup
#################################################

url = 'postgresql://postgres:password@localhost:5432/Stroke-Prediction/StrokeDS'
# url=os.environ.get("URL")
engine = create_engine(url)
Base.prepare(engine, reflect=True)
session = Session(engine)
app = Flask(__name__)

@app.route("/")

# # #uncomment line below when you want to deploy to heroku
# # # url = os.environ.get("URL")