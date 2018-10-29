import pandas as pd
import numpy as np

file1 = 'data_ml/F8.csv'
feature = pd.read_csv(file1)
print(feature.shape) #(4306, 65)

feature1 = feature[['PAT_DEID']]

file2 = 'data_ml/INS_TYPE.xlsx'
x2 = pd.ExcelFile(file2)
ins = x2.parse('Sheet1')
print(ins.shape) #(53267, 3)
ins = ins.drop_duplicates(['PAT_DEID'], keep='last')
print(ins.shape) #(53266, 3)
ins = ins[['PAT_DEID','INSURANCE_TYPE']]
print(ins.shape) #(53266, 2)
ins = pd.merge(feature1, ins, on='PAT_DEID', how='inner')
print(ins.shape) #(4306, 2)

file3 = 'data_ml/prior_opioid_pat.xlsx'
x3 = pd.ExcelFile(file3)
op = x3.parse('Sheet1')
print(op.shape) #(20522, 18)
op = op[['PAT_DEID','OPIOID_TOLERANT']]
print(op.shape) #(20522, 2)
op = op.drop_duplicates(['PAT_DEID'], keep='last')
print(op.shape) #(1836, 2)
op = pd.merge(feature1, op, on='PAT_DEID', how='inner')
print(op.shape) #(1836, 2)

file4 = 'data_ml/CHARLSON_FINAL.xlsx'
x4 = pd.ExcelFile(file4)
charlson = x4.parse('Sheet1')
print(charlson.shape) #(1195, 2)
charlson = charlson.drop_duplicates(['PAT_DEID'], keep='last')
print(charlson.shape) #(1195, 2)
charlson = pd.merge(feature1, charlson, on='PAT_DEID', how='inner')
print(charlson.shape) #(965, 2)

pat = pd.merge(feature, ins, on='PAT_DEID', how='outer')
print(pat.shape) #(4306, 66)
pat = pd.merge(pat, op, on='PAT_DEID', how='outer')
print(pat.shape) #(4306, 67)
pat = pd.merge(pat, charlson, on='PAT_DEID', how='outer')
print(pat.shape) #(4306, 68)
pat.to_pickle("data_ml/F9.pkl")

writer = pd.ExcelWriter('data_ml/F9.xlsx')
pat.to_excel(writer,'Sheet1')
writer.save()
