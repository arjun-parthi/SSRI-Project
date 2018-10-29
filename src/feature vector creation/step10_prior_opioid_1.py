import pandas as pd
import numpy as np

file1 = 'data_ml/F7.csv'
feature = pd.read_csv(file1)
print(feature.shape) #(4306, 65)

feature1 = feature[['PAT_DEID']]
print(feature1.shape) #(4306, 1)

file2 = 'data_ml/FOR_PRIOR_OPIOID1.xlsx'
x1 = pd.ExcelFile(file2)
meds = x1.parse('Sheet1')
print(meds.shape) #(972714, 13)

meds_req = pd.merge(feature1, meds, on='PAT_DEID', how='inner')
print(meds_req.shape) #(151751, 13)

writer = pd.ExcelWriter('data_ml/meds_req.xlsx')
meds_req.to_excel(writer,'Sheet1')
writer.save()
