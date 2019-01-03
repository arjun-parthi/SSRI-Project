import pandas as pd
import numpy as np

file1 = '../data/ICD9_final1.xlsx'
x1 = pd.ExcelFile(file1)
icd9list = x1.parse('Sheet1')
print(icd9list.shape)

file2 = '../data/CHARLSON_POINTS.xlsx'
x2 = pd.ExcelFile(file2)
charlson = x2.parse('Sheet1')
print(charlson.shape)

points = pd.merge(icd9list, charlson, on='ICD9_LIST', how='inner')
print(points.shape)
points1 = points.drop(['ICD9_LIST'], axis=1)
print(points1.shape)

points1 = points1.sort_values('POINTS').drop_duplicates(subset=['PAT_DEID', 'COMORBIDITY'], keep='last')
print(points1.shape)
points2 = points1.drop(['COMORBIDITY'], axis=1)
print(points2.shape)
points3 = points2.groupby(['PAT_DEID']).sum()

print(points3.shape)
writer = pd.ExcelWriter('../data/CHARLSON_FINAL.xlsx')
points3.to_excel(writer,'Sheet1')
writer.save()
