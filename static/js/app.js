// Add console.log to check to see if our code is working.
console.log("app.js");
function make_pred(){
    console.log("make_pred");
    let age= document.getElementById("age").value;
    let Smoking_Status= document.getElementById("Smoking_Status").value;
    let BMI= document.getElementById("BMI").value;
    let Heart_Disease= document.getElementById("Heart_Disease").value;
    let Hyper_Tension= document.getElementById("Hyper_Tension").value;
    let Work_Type= document.getElementById("Work_Type").value;
    let Residence= document.getElementById("Residence").value;
    let Gender= document.getElementById("Gender").value;
    let Avg_Glucose= document.getElementById("Avg_Glucose").value;
    let Married= document.getElementById("Married").value;
    
    console.log("age",age); 
    console.log("Smoking_Status",Smoking_Status);
    console.log("BMI",BMI);
    console.log("Heart_Disease",Heart_Disease);
    console.log("Hyper_Tension",Hyper_Tension);
    console.log("Work_Type",Work_Type);
    console.log("Residence",Residence);
    console.log("Gender",Gender);
    console.log("Avg_Glucose",Avg_Glucose);
    console.log("Married",Married);
        
    fetch("/predict",{
        method: "POST", 
        body: JSON.stringify({
            age: age,
            Smoking_Status: Smoking_Status,
            BMI: BMI,
            Heart_Disease: Heart_Disease,
            Hyper_Tension: Hyper_Tension,
            Work_Type: Work_Type,
            Residence: Residence,
            Gender: Gender,
            Avg_Glucose: Avg_Glucose, 
            Married: Married       

        }),
        headers:{
            "Content-type":"application/json;charset=UTF-8"

        }

    }).then(resp=>{
        return resp.json()
    }).then(resp=>{
        console.log(resp)
        document.getElementById("prediction").innerHTML=resp.Prediction
        console.log(resp.Prediction);
        if (resp.Prediction==0){
            document.getElementById("dummy").src= "/static/images/High_Risk.png" 
        }
        else if (resp.Prediction==1){
            document.getElementById("dummy").src="/static/images/Low_Risk.png"
        }
    })
}