import pandas as pd
import numpy as np

file1 = '../data/STRIDE_PATIENT.xlsx'
x1 = pd.ExcelFile(file1)
stride_patient = x1.parse('Sheet1')

file2 = '../data//SURGERY.xlsx'
x2 = pd.ExcelFile(file2)
surgery = x2.parse('Sheet1')

stride_patient_req = stride_patient
pat_surgery = pd.merge(stride_patient_req, surgery, on='PAT_DEID', how='inner')
pat_surgery['BIRTH_DATE'] = pat_surgery['BIRTH_DATE'].str[0:7] + '19' + pat_surgery['BIRTH_DATE'].str[7:]
pat_surgery['SURGERY_DATE'] = pat_surgery['SURGERY_DATE'].str[0:7] + '20' + pat_surgery['SURGERY_DATE'].str[7:]

pat_surgery['BIRTH_DATE'] = pd.to_datetime(pat_surgery['BIRTH_DATE'])
pat_surgery['SURGERY_DATE'] = pd.to_datetime(pat_surgery['SURGERY_DATE'])
print(pat_surgery.dtypes)

pat_surgery['Difference'] = pat_surgery['SURGERY_DATE'].sub(pat_surgery['BIRTH_DATE'], axis=0)
pat_surgery['AGE AT SURGERY'] = pat_surgery['Difference'] / np.timedelta64(365, 'D')
pat_surgery['AGE AT SURGERY'] = pat_surgery['AGE AT SURGERY'].astype(int)

pat_surgery = pat_surgery.drop(['BIRTH_DATE', 'SURGERY_DATE', 'Difference'], axis=1)
print(pat_surgery.dtypes)
writer = pd.ExcelWriter('../data/PATIENT_FINAL.xlsx')
pat_surgery.to_excel(writer,'Sheet1')
writer.save()
