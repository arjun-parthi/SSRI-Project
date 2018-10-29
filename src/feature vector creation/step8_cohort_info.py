import pandas as pd
import numpy as np
file1 = 'data_ml/FINAL_FEATURE_VECTOR2.xlsx'
x1 = pd.ExcelFile(file1)
feature = x1.parse('Sheet1')
print(feature.shape) #(5127, 64)

file2 = 'data_ml/AP_SSRI_PD_PAIN.xlsx'
x2 = pd.ExcelFile(file2)
cohort1 = x2.parse('Sheet1')
print(cohort1.shape) #(1021, 13)
cohort1 = cohort1.drop(['CLASSIFICATION'], axis=1)
cohort1 = cohort1.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort1.shape) #(607, 12)

file3 = 'data_ml/AP_SSRI_NPD_PAIN.xlsx'
x3 = pd.ExcelFile(file3)
cohort2 = x3.parse('Sheet1')
print(cohort2.shape) #(1739, 13)
cohort2 = cohort2.drop(['CLASSIFICATION'], axis=1)
cohort2 = cohort2.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort2.shape) #(1286, 12)

file4 = 'data_ml/AP_NOSSRI_PD_PAIN.xlsx'
x4 = pd.ExcelFile(file4)
cohort3 = x4.parse('Sheet1')
print(cohort3.shape) #(1429, 13)
cohort3 = cohort3.drop(['CLASSIFICATION'], axis=1)
cohort3 = cohort3.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort3.shape) #(803, 12)

file5 = 'data_ml/AP_NOSSRI_NPD_PAIN.xlsx'
x5 = pd.ExcelFile(file5)
cohort4 = x5.parse('Sheet1')
print(cohort4.shape) #(2404, 13)
cohort4 = cohort4.drop(['CLASSIFICATION'], axis=1)
cohort4 = cohort4.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort4.shape) #(1614, 12)

cohorts = pd.concat([cohort1,cohort2,cohort3,cohort4])
print(cohorts.shape) #(4310, 12)
feature4 = pd.merge(feature, cohorts, on='PAT_DEID', how='outer')
print(feature4.shape) #(5127, 75)
feature4 = feature4.dropna(subset=['COHORT'])
print(feature4.shape) #(4310, 75)

feature4.to_pickle("data_ml/FEATURE_VEC.pkl")
writer = pd.ExcelWriter('data_ml/FEATURE_VEC.xlsx')
feature4.to_excel(writer,'Sheet1')
writer.save()
