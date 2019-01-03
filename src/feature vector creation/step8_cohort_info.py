import pandas as pd
import numpy as np
file1 = '../data/FV2.xlsx'
x1 = pd.ExcelFile(file1)
feature = x1.parse('Sheet1')
print(feature.shape)

file2 = '../data/AP_SSRI_PD_PAIN.xlsx'
x2 = pd.ExcelFile(file2)
cohort1 = x2.parse('Sheet1')
print(cohort1.shape)
cohort1 = cohort1.drop(['CLASSIFICATION'], axis=1)
cohort1 = cohort1.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort1.shape)

file3 = '../data/AP_SSRI_NPD_PAIN.xlsx'
x3 = pd.ExcelFile(file3)
cohort2 = x3.parse('Sheet1')
print(cohort2.shape)
cohort2 = cohort2.drop(['CLASSIFICATION'], axis=1)
cohort2 = cohort2.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort2.shape)

file4 = '../data/AP_NOSSRI_PD_PAIN.xlsx'
x4 = pd.ExcelFile(file4)
cohort3 = x4.parse('Sheet1')
print(cohort3.shape)
cohort3 = cohort3.drop(['CLASSIFICATION'], axis=1)
cohort3 = cohort3.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort3.shape)

file5 = '../data/AP_NOSSRI_NPD_PAIN.xlsx'
x5 = pd.ExcelFile(file5)
cohort4 = x5.parse('Sheet1')
print(cohort4.shape)
cohort4 = cohort4.drop(['CLASSIFICATION'], axis=1)
cohort4 = cohort4.drop_duplicates(['PAT_DEID'], keep='last')
print(cohort4.shape)

cohorts = pd.concat([cohort1,cohort2,cohort3,cohort4])
print(cohorts.shape)
feature4 = pd.merge(feature, cohorts, on='PAT_DEID', how='outer')
print(feature4.shape)
feature4 = feature4.dropna(subset=['COHORT'])
print(feature4.shape)

feature4 = feature4.drop(['PAIN_CAT_DISCHARGE'], axis=1)
feature4 = feature4.drop(['PAIN_CAT_FOLLOWUP_3'], axis=1)
feature4 = feature4.drop(['PAIN_CAT_FOLLOWUP_8'], axis=1)

writer = pd.ExcelWriter('../data/FV3.xlsx')
feature4.to_excel(writer,'Sheet1')
writer.save()
