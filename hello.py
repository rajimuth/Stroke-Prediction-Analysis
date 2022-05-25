from flask import Flask

app = Flask(__name__)

@app.route("/")
def stroke():
    return "<p>Stroke prediction analysis</p>"

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Stroke Analysis API!
    Available Routes:
    /api/v1.0/Stroke Description
    /api/v1.0/User Stroke Prediction
    /api/v1.0/Results
    ''')