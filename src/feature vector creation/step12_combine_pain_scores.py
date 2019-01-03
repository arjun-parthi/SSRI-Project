import pandas as pd
import numpy as np

file1 = '../data/F9.xlsx'
x1 = pd.ExcelFile(file1)
feature = x1.parse('Sheet1')
print(feature.shape)
feature = feature.drop(['\'DAY_OF_DISCHARGE\''], axis=1)
feature = feature.drop(['\'FOLLOW_UP_3WEEKS\''], axis=1)
feature = feature.drop(['\'FOLLOW_UP_8WEEKS\''], axis=1)
feature = feature.drop(['PREOP_PAIN'], axis=1)
feature = feature.drop(['CHANGE_DISCHARGE'], axis=1)
feature = feature.drop(['CHANGE_FOLLOWUP_3'], axis=1)
feature = feature.drop(['CHANGE_FOLLOWUP_8'], axis=1)
print(feature.shape)

file2 = '../data/PAIN_SCORES.xlsx'
x2 = pd.ExcelFile(file2)
feature2 = x2.parse('Sheet1')
print(feature2.shape)

feature2 = feature2[['PAT_DEID','DAY_OF_DISCHARGE','FOLLOW_UP_3WEEKS','FOLLOW_UP_8WEEKS','PREOP_PAIN','CHANGE_DISCHARGE','CHANGE_FOLLOWUP_3','CHANGE_FOLLOWUP_8','DAY_OF_DISCHARGE1','FOLLOW_UP_3WEEKS1','FOLLOW_UP_8WEEKS1']]

pat = pd.merge(feature, feature2, on='PAT_DEID', how='outer')
print(pat.shape)

writer = pd.ExcelWriter('../data/FINAL_FEATURE_VECTOR.xlsx')
pat.to_excel(writer,'Sheet1')
writer.save()
pat.to_csv('../data/FINAL_FEATURE_VECTOR.csv', encoding='utf-8')