# Stroke-Prediction-Analysis
### Web application for Stroke prediction using Machine learning Model based upon certain user features  
### Goal (Why Stroke Analysis?):
Stroke is the second leading cause of death worldwide. The aftermath is devastating, with victims experiencing a wide range of disabling symptoms including sudden paralysis, speech loss or blindness due to blood flow interruption in the brain. It is estimated that 60 to 80% of strokes could be prevented through healthy lifestyle changes like losing weight, smoking cessation, and controlling high cholesterol and blood pressure levels [6].
So, in this analysis we have created an app to predict the risk for stroke, based on the user input parameters like gender, age, various diseases, and smoking status. 
### Dataset:
The Stroke prediction dataset was retrieved from Kaggle. 
Stroke Prediction Dataset | Kaggle
### Attribute Information
1)	id: unique identifier
2) gender: "Male", "Female" or "Other"
3) age: age of the patient
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6) ever_married: "No" or "Yes"
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8) Residence_type: "Rural" or "Urban"
9) avg_glucose_level: average glucose level in blood
10) bmi: body mass index
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
12) stroke: 1 if the patient had a stroke or 0 if not
*Note: "Unknown" in smoking_status means that the information is unavailable for this patient

### Dependencies		

|  Pandas       |Matplotlib     | Path  | 
| ------------- |:-------------:| -----:|
| Logistic Regression     | RandomForestClassifier| train_test_split |  
| sklearn     | Standard scaler  |   Confusion_matrix |
| Accuracy score | Tensorflow     |   OneHotEncoder |
| Make_classification	 | Classification_report	PCA    |

### Methods and Results:
#### Data Cleaning:
- ID column was removed considering it an irrelevant feature for the data. 
- All the columns were renamed for better visualisation. 
- All the NaN values were dropped, there were 201 in the BMI column. 
- The clean data was extracted in a separate csv file to make the rest of analysis go smooth. 
#### Univariate Analysis of Features:

|  Feature       |Analysis   | 
| ------------- |:-------------:| 
|Age     |Evenly distributed between 0-100|
| Gender     | Slightly more Female  |   
| WorkType | More Private than others     |  
| Residence	 | Equal between Urban and Rural    |
| Marriage_Status | Slightly more Married  |

<img width="431" alt="image" src="https://user-images.githubusercontent.com/94877067/171478782-06f2cd40-6f7a-4db1-b258-f84711c1e0cd.png">

#### Bivariate Analysis with respect to Stroke:

<img width="383" alt="image" src="https://user-images.githubusercontent.com/94877067/171479042-5080d5f3-04b4-4358-b0c3-3cf236b4a3d4.png">

#### Preprocessing data for Machine Learning
- One Hot Encoding is used to transform all the categorical variable list. 
- Using standard scaler, we standardized the functionality of our inputs, in other words it is used to create less bias in the data before moving to the machine learning model. 
- Oversampling is performed to compensate the imbalance present in the data. 

#### Machine Learning Model: Supervised Machine Learning!


|  Model Type     |Accuracy Score  | Level of Accuracy  | 
| ------------- |:-------------:| -----:|
| Logistic Regression     | 0.762 | High |  
| RandomForestClassifier   | 0.054 |   Low|
| Decision Tree | 0.90 |   Very High(Selected for Webapp) |
| PCA | 0.763| High |
| Neural network |0.841 | High |

#### Web application for “Stroke Prediction” using FLASK! 
- Template created using index.html.
- Predictions created using predictions.html.
- Machine learning algorithm used the Decision Tree Model due to high accuracy. 

#### Final Look

<img width="425" alt="image" src="https://user-images.githubusercontent.com/94877067/171480946-06b501ee-9337-420c-9bd9-cfa750de9d38.png">










