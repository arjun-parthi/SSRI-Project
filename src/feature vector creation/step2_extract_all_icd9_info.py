import pandas as pd
import numpy as np

file1 = 'data_ml/ICD9.xlsx'
x1 = pd.ExcelFile(file1)
icd9 = x1.parse('Sheet1')
print(icd9.shape)
print(icd9.iloc[0:1])
print(icd9.dtypes)
file2 = 'data_ml/SURGERY.xlsx'
x2 = pd.ExcelFile(file2)
surgery = x2.parse('Sheet1')
surgery = surgery.drop(['SURGERY_TYPE'], axis=1)
print(surgery.shape) #(1048001, 3)
print(surgery.iloc[0:1])
print(surgery.dtypes) #(5127, 2)
icd9_surgery = pd.merge(icd9, surgery, on='PAT_DEID', how='inner')
icd9_surgery['START_DATE'] = icd9_surgery['START_DATE'].str[0:7] + '20' + icd9_surgery['START_DATE'].str[7:]
icd9_surgery['SURGERY_DATE'] = icd9_surgery['SURGERY_DATE'].str[0:7] + '20' + icd9_surgery['SURGERY_DATE'].str[7:]
print(icd9_surgery.shape) #(1048001, 4)

icd9_surgery1 = icd9_surgery.loc[(icd9_surgery['START_DATE']  <= icd9_surgery['SURGERY_DATE'])]
print(icd9_surgery1.shape) #(534025, 4)
print(icd9_surgery1.iloc[0:5])
icd9_surgery1 = icd9_surgery1.drop(['START_DATE','SURGERY_DATE'], axis=1)
print(icd9_surgery1.shape) #(534025, 2)
print(icd9_surgery1.dtypes)

icd9_surgery1.to_pickle("data_ml/ICD9_final.pkl")
icd9_surgery1['ICD9_LIST'] = icd9_surgery1['ICD9_LIST'].astype(str)
icd9_surgery2 = pd.DataFrame(icd9_surgery1.ICD9_LIST.str.split(',').tolist(), index=icd9_surgery1.PAT_DEID).stack()
icd9_surgery2 = icd9_surgery2.reset_index()[[0, 'PAT_DEID']] # var1 variable is currently labeled 0
icd9_surgery2.columns = ['ICD9', 'PAT_DEID']
print(icd9_surgery2.shape) #(541543, 2)
print(icd9_surgery2.dtypes)
print(icd9_surgery2.iloc[0:5])
writer = pd.ExcelWriter('data_ml/ICD9_final1.xlsx')
icd9_surgery2.to_excel(writer,'Sheet1')
writer.save()
