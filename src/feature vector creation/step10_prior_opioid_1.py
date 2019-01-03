import pandas as pd
import numpy as np

file1 = '../data/FEATURE_VECTOR_initial.xlsx'
x1 = pd.ExcelFile(file1)
feature = x1.parse('Sheet1')
print(feature.shape)

feature1 = feature[['PAT_DEID']]
print(feature1.shape)

file2 = '../data/FOR_PRIOR_OPIOID1.xlsx'
x1 = pd.ExcelFile(file2)
meds = x1.parse('Sheet1')
print(meds.shape)

meds_req = pd.merge(feature1, meds, on='PAT_DEID', how='inner')
print(meds_req.shape)

writer = pd.ExcelWriter('../data/meds_req.xlsx')
meds_req.to_excel(writer,'Sheet1')
writer.save()
