from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", 'POST'])
def index():
    return render_template("index.html") 


@app.route("/predict", methods=["GET", 'POST'])
def predict():
    output = "Your value here!"
    #If you have the user submit a form
    if request.method == 'POST': 

        model= joblib.load('models/test1.joblib')
        
        age=request.json.get("age")
        Smoking_Status=request.json.get("Smoking_Status")
        BMI=request.json.get("BMI")
        Heart_Disease=request.json.get("Heart_Disease")
        Hyper_Tension=request.json.get("Hyper_Tension")
        Work_Type=request.json.get("Work_Type")
        Residence=request.json.get("Residence")
        Gender=request.json.get("Gender")
        Avg_Glucose=request.json.get("Avg Glucose")
        Married=request.json.get("Married")
        
        columns = ['age', 'Smoking_Status', 'BMI', 'Heart_Disease', 'Hyper_Tension', 'Work_Type', 'Residence', 'Gender', 'Avg_Glucose', 'Married']
        
        test_data = pd.DataFrame([['age', 'Smoking_Status', 'BMI', 'Heart_Disease', 'Hyper_Tension', 'Work_Type', 'Residence', 'Gender', 'Avg_Glucose', 'Married']], columns=columns)
        pred=model.predict(test_data)

        print(test_data)
        print(pred)
        # return render_template('predictions.html', output=output)
        return {"Prediction": pred[0]}
        
    return render_template('predictions.html', output=output)

if __name__=="__main__":
    app.run(debug=True)
    

