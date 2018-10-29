import pandas as pd
import numpy as np

file1 = 'data_ml/F9.csv'
feature = pd.read_csv(file1)
print(feature.shape) #(4306, 68)

file2 = 'data_ml/F5.csv'
feature2 = pd.read_csv(file2)
print(feature2.shape) #(4306, 74)

feature2 = feature2[['PAT_DEID','CHANGE_DISCHARGE','CHANGE_FOLLOWUP_3','CHANGE_FOLLOWUP_8']]

pat = pd.merge(feature, feature2, on='PAT_DEID', how='outer')
print(pat.shape) #(4306, 71)

writer = pd.ExcelWriter('data_ml/F10.xlsx')
pat.to_excel(writer,'Sheet1')
writer.save()
