# Predicting Inadequate Postoperative Pain Management in Depressed Patients: A Machine Learning Approach
This code for this project is primarily divided into three stages:
1. Identification of depressed patients and related information
2. Creation of the feature vector
3. Development of models for predicting the increase or decrease in the postoperative pain score across three time points

### Identification of depressed patients and related information
This has been divided into multiple steps:
* Tokenizing the clinical notes into sentences and then searching for depression terms in them
* Apply Negex algorithm to detect presence or absence of depression from the text snippet
* Apply majority algorithm to detect presence or absence of depression at note level
* Filtering surgery patients who were tagged as depressed within one year prior to surgery
* Combining patients identified as depressed using ICD9 codes
* Identification of patients on selective serotonin reuptake inhibitors (SSRIs) from clinical text and medications
* Identification of patients of interest (Surgery patients on opioids who are also tagged as depressed patients prescribed SSRIs) 

### Creation of feature vector
The feature vector was created by considering the following:
* Patient characteristics (age at surgery, gender, race/ethnicity, marital status, insurance type, charlson comorbidity index, body mass index)
* Diagnosis information (based on ICD9 codes)
* Patient vital information (blood pressure, heart rate, body temperature,.etc)
* Preoperative pain
* Medications represented as binary vector
* Pain medications - Oral morphine equivalent
* Opioid classes - prodrugs and non-prodrugs
* Antidepressants and Depression related information (eg.SSRI use)

### Developement of models for prediction
The increase or decrease in postoperative pain is predicted using ElasticNet, SVM, RandomForest regressor and classifer models. Hyperparameter tuning is also performed. The performance of the models is evaluated on the basis of mean ROC using 10-fold cross validation.

