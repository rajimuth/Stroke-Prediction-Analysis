from flask import Flask, render_template, request
import joblib
import pandas as pd
import json




app = Flask(__name__)

model= joblib.load('models/dtree.joblib')

@app.route("/", methods=["GET", 'POST'])
def index():
    return render_template("index.html") 


@app.route("/predict", methods=["GET", 'POST'])
def predict():
    output = "Your value here!"
    #If you have the user submit a form
    if request.method == 'POST':    
        
        
        Age=request.json.get("age")
        Smoking_Status=request.json.get("Smoking_Status")
        BMI=request.json.get("BMI")
        Heart_Disease=request.json.get("Heart_Disease")
        Hyper_Tension=request.json.get("Hyper_Tension")
        Work_Type=request.json.get("Work_Type")
        Residence=request.json.get("Residence")
        Gender=request.json.get("Gender")
        Avg_Glucose=request.json.get("Avg_Glucose")
        Married=request.json.get("Married")

        Smoking_Status_neversmoked = 0
        Smoking_Status_formerlysmoked=0
        Smoking_Status_smokes =0
        Smoking_Status_Unknown=0
        Gender_Male=0
        Gender_Female=0
        Ever_Married_Yes=0
        Ever_Married_No=0
        Work_Type_Govt_job=0
        Work_Type_Private=0
        Work_Type_Self_employed=0
        Work_Type_Never_worked=0
        Work_Type_children=0
        Residence_Type_Rural=0
        Residence_Type_Urban=0
    
        if Smoking_Status == 1:
            Smoking_Status_neversmoked =  1 
        if Smoking_Status == 2:
            Smoking_Status_formerlysmoked =  2
        if Smoking_Status == 3:
            Smoking_Status_smokes =  3
        if Smoking_Status == 4:
            Smoking_Status_Unknown = 4
        if Gender == 1:
            Gender_Male =  1 
        if Gender == 2:
            Gender_Female =  2
        if Married == 1:
            Ever_Married_Yes =  1 
        if Married == 2:
            Ever_Married_No =  2
        if Work_Type == 1:
            Work_Type_Govt_job =  1 
        if Work_Type == 2:
            Work_Type_Private =  2
        if Work_Type == 3:
            Work_Type_Self_employed =  3
        if Work_Type == 4:
            Work_Type_Never_worked =  4
        if Work_Type == 5:
            Work_Type_children =  5
        if Residence == 1:
            Residence_Type_Rural =  1 
        if Residence == 2:
            Residence_Type_Urban =  2

        

         
        columns = ['Age', 'Hypertension','Heart_Disease','Average_Glucose','BMI','Gender_Female','Gender_Male','Ever_Married_No','Ever_Married_Yes','Work_Type_Govt_job','Work_Type_Never_worked','Work_Type_Private','Work_Type_Self_employed','Work_Type_children','Residence_Type_Rural','Residence_Type_Urban','Smoking_Status_Unknown','Smoking_Status_formerlysmoked','Smoking_Status_neversmoked','Smoking_Status_smokes']
        # test_data = pd.DataFrame([[70, 1,1,110,33,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1]], columns=columns)
        test_data = pd.DataFrame([[Age, Hyper_Tension,Heart_Disease,Avg_Glucose,BMI,Gender_Female,Gender_Male,Ever_Married_No,Ever_Married_Yes,Work_Type_Govt_job,Work_Type_Never_worked,Work_Type_Private,Work_Type_Self_employed,Work_Type_children,Residence_Type_Rural,Residence_Type_Urban,Smoking_Status_Unknown,Smoking_Status_formerlysmoked,Smoking_Status_neversmoked,Smoking_Status_smokes]], columns=columns)
        print("This is app3.py")        
        print(test_data)                  
       
        pred=model.predict(test_data)
        
        print("prediction",pred)
        pred =int(pred[0])
        print("pred1",pred)

        # return render_template('predictions.html', output=output)

        # if int(pred[0]) == 0:
        #     return {"Prediction": [0]}
        # else:
        #     return {"Prediction": [1]}  
        return {"Prediction": pred}
        
    
    return render_template('predictions.html', output=output)

if __name__=="__main__":
    app.run(debug=True)
    

