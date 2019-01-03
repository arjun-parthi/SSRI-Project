import pandas as pd
import numpy as np

file1 = '../data/MEDICATIONS3.xlsx'
x1 = pd.ExcelFile(file1)
meds = x1.parse('Sheet1')
print(meds.shape) 
print(meds.iloc[0:1])
print(meds.dtypes)

meds = meds.drop(['ORDER_STATUS','CLASSIFICATION'], axis=1)

meds1 = meds.dropna(subset=['THERA_CLASS_NAME'])
print(meds1.shape)
print(meds1.iloc[0:1])
print(meds1.dtypes)

meds2 = meds1.pivot_table('COUNT', ['PAT_DEID'], 'THERA_CLASS_NAME')
print(meds2.shape)
print(meds2.iloc[0:5])
print(meds2.dtypes)
meds2 = meds2.fillna(0)
writer = pd.ExcelWriter('../data/MEDICATIONS4.xlsx')
meds2.to_excel(writer,'Sheet1')
writer.save()
