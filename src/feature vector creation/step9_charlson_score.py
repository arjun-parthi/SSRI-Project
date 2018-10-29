import pandas as pd
import numpy as np

file1 = 'data_ml/ICD9_final.xlsx'
x1 = pd.ExcelFile(file1)
icd9list = x1.parse('Sheet1')
print(icd9list.shape) #(534025, 2)

file2 = 'data_ml/CHARLSON_POINTS.xlsx'
x2 = pd.ExcelFile(file2)
charlson = x2.parse('Sheet1')
print(charlson.shape) #(4375, 3)

points = pd.merge(icd9list, charlson, on='ICD9_LIST', how='inner')
print(points.shape) #(65521, 4)
points1 = points.drop(['ICD9_LIST'], axis=1)
print(points1.shape) #(65521, 3)

points1 = points1.sort_values('POINTS').drop_duplicates(subset=['PAT_DEID', 'COMORBIDITY'], keep='last')
print(points1.shape)
points2 = points1.drop(['COMORBIDITY'], axis=1)
print(points2.shape) #(65521, 2)
points3 = points2.groupby(['PAT_DEID']).sum()
# df.groupby(['PAT_DEID'])['POINTS'].agg('sum')
print(points3.shape) #(1195, 1)
writer = pd.ExcelWriter('data_ml/CHARLSON_FINAL.xlsx')
points3.to_excel(writer,'Sheet1')
writer.save()
