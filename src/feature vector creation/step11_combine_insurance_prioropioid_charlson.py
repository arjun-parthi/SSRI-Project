import pandas as pd
import numpy as np

file1 = '../data/FV3.xlsx'
x1 = pd.ExcelFile(file1)
feature = x1.parse('Sheet1')
print(feature.shape)

feature1 = feature[['PAT_DEID']]

file2 = '../data/INS_TYPE.xlsx'
x2 = pd.ExcelFile(file2)
ins = x2.parse('Sheet1')
print(ins.shape)
ins = ins.drop_duplicates(['PAT_DEID'], keep='last')
print(ins.shape)
ins = ins[['PAT_DEID','INSURANCE_TYPE']]
print(ins.shape)
ins = pd.merge(feature1, ins, on='PAT_DEID', how='inner')
print(ins.shape)

file3 = '../data/prior_opioid_pat.xlsx'
x3 = pd.ExcelFile(file3)
op = x3.parse('Sheet1')
print(op.shape)
op = op[['PAT_DEID','OPIOID_TOLERANT']]
print(op.shape)
op = op.drop_duplicates(['PAT_DEID'], keep='last')
print(op.shape)
op = pd.merge(feature1, op, on='PAT_DEID', how='inner')
print(op.shape)

file4 = '../data/CHARLSON_FINAL.xlsx'
x4 = pd.ExcelFile(file4)
charlson = x4.parse('Sheet1')
print(charlson.shape)
charlson = charlson.drop_duplicates(['PAT_DEID'], keep='last')
print(charlson.shape)
charlson.columns = ['PAT_DEID', 'CHARLSON_SCORE']
charlson = pd.merge(feature1, charlson, on='PAT_DEID', how='inner')
print(charlson.shape)

pat = pd.merge(feature, ins, on='PAT_DEID', how='outer')
print(pat.shape)
pat = pd.merge(pat, op, on='PAT_DEID', how='outer')
print(pat.shape)
pat = pd.merge(pat, charlson, on='PAT_DEID', how='outer')
print(pat.shape)
pat = pat.drop(['ETHNICITY'], axis=1)
pat = pat.drop(['INSURANCE_PAYOR_NAME'], axis=1)
pat = pat.drop(['ANXIETY'], axis=1)

print(pat.shape)

writer = pd.ExcelWriter('../data/F9.xlsx')
pat.to_excel(writer,'Sheet1')
writer.save()
