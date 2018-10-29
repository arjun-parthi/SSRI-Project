import pandas as pd
import numpy as np

file1 = 'data_ml/PATIENT_FINAL.xlsx'
x1 = pd.ExcelFile(file1)
patient_demog = x1.parse('Sheet1')
print(patient_demog.shape) #(5127, 11)


file2 = 'data_ml/ICD9_final_features.xlsx'
x2 = pd.ExcelFile(file2)
icd9 = x2.parse('Sheet1')
print(icd9.shape) #(1560, 19)


file3 = 'data_ml/MEDICATIONS4.xlsx'
x3 = pd.ExcelFile(file3)
meds = x3.parse('Sheet1')
print(meds.shape) #(2503, 32)


file4 = 'data_ml/VITALS_BP1.xlsx'
x4 = pd.ExcelFile(file4)
bp = x4.parse('Sheet1')
print(bp.shape) #(26858, 10)


######
bp = bp.dropna(subset=['START_DATE'])
bp['RECORDED_TIME'] = bp['RECORDED_TIME'].str[0:7] + '20' + bp['RECORDED_TIME'].str[7:]
bp['START_DATE'] = bp['START_DATE'].str[0:7] + '20' + bp['START_DATE'].str[7:]
bp['RECORDED_TIME'] = pd.to_datetime(bp['RECORDED_TIME'])
bp['START_DATE'] = pd.to_datetime(bp['START_DATE'])
bp['Difference'] = bp['START_DATE'].sub(bp['RECORDED_TIME'], axis=0)
bp['DAYS_BEFORE_SURGERY'] = bp['Difference'] / np.timedelta64(1, 'D')
bp['DAYS_BEFORE_SURGERY'] = bp['DAYS_BEFORE_SURGERY'].astype(int)
bp['x'] = bp.groupby('PAT_DEID')['DAYS_BEFORE_SURGERY'].transform('min')
bp1 = bp.loc[(bp['x']  == bp['DAYS_BEFORE_SURGERY'])]
bp1['y'] = bp1.groupby('PAT_DEID')['ABS_1'].transform('max')
bp1 = bp1.loc[(bp1['y']  == bp1['CHANGE_SYSTOLIC'].abs())]
bp1 = bp1.drop_duplicates(['PAT_DEID'], keep='last')
######
bp = bp1[['PAT_DEID','CHANGE_SYSTOLIC','CHANGE_DIASTOLIC']]
print(bp.shape) #(1466, 3)

file5 = 'data_ml/VITALS_HEART_RATE.xlsx'
x5 = pd.ExcelFile(file5)
heart = x5.parse('Sheet1')
print(heart.shape) #(44684, 7)

######
heart = heart.dropna(subset=['START_DATE'])
heart['RECORDED_TIME'] = heart['RECORDED_TIME'].str[0:7] + '20' + heart['RECORDED_TIME'].str[7:]
heart['START_DATE'] = heart['START_DATE'].str[0:7] + '20' + heart['START_DATE'].str[7:]
heart['RECORDED_TIME'] = pd.to_datetime(heart['RECORDED_TIME'])
heart['START_DATE'] = pd.to_datetime(heart['START_DATE'])
heart['Difference'] = heart['START_DATE'].sub(heart['RECORDED_TIME'], axis=0)
heart['DAYS_BEFORE_SURGERY'] = heart['Difference'] / np.timedelta64(1, 'D')
heart['DAYS_BEFORE_SURGERY'] = heart['DAYS_BEFORE_SURGERY'].astype(int)
heart['x'] = heart.groupby('PAT_DEID')['DAYS_BEFORE_SURGERY'].transform('min')
heart1 = heart.loc[(heart['x']  == heart['DAYS_BEFORE_SURGERY'])]
heart1 = heart1.drop_duplicates(['PAT_DEID'], keep='last')
print(heart1.shape) #(389, 10)
######
heart = heart1[['PAT_DEID','HR_NORMAL_ABNORMAL']]
print(heart.shape) #(389, 2)

file6 = 'data_ml/VITALS_TEMP.xlsx'
x6 = pd.ExcelFile(file6)
temp = x6.parse('Sheet1')
print(temp.shape) #(27426, 6)

######
temp = temp.dropna(subset=['START_DATE'])
temp['RECORDED_TIME'] = temp['RECORDED_TIME'].str[0:7] + '20' + temp['RECORDED_TIME'].str[7:]
temp['START_DATE'] = temp['START_DATE'].str[0:7] + '20' + temp['START_DATE'].str[7:]
temp['RECORDED_TIME'] = pd.to_datetime(temp['RECORDED_TIME'])
temp['START_DATE'] = pd.to_datetime(temp['START_DATE'])
temp['Difference'] = temp['START_DATE'].sub(temp['RECORDED_TIME'], axis=0)
temp['DAYS_BEFORE_SURGERY'] = temp['Difference'] / np.timedelta64(1, 'D')
temp['DAYS_BEFORE_SURGERY'] = temp['DAYS_BEFORE_SURGERY'].astype(int)
temp['x'] = temp.groupby('PAT_DEID')['DAYS_BEFORE_SURGERY'].transform('min')
temp = temp.loc[(temp['x']  == temp['DAYS_BEFORE_SURGERY'])]
temp['y'] = temp.groupby('PAT_DEID')['ABS_1'].transform('max')
temp = temp.loc[(temp['y']  == temp['CHANGE_TEMP'].abs())]
temp = temp.drop_duplicates(['PAT_DEID'], keep='last')
######
temp = temp[['PAT_DEID','CHANGE_TEMP']]
print(temp.shape) #(1471, 2)

file7 = 'data_ml/VITALS_ANXIETY.xlsx'
x7 = pd.ExcelFile(file7)
anxiety = x7.parse('Sheet1')
print(anxiety.shape) #(40035, 5)

######
anxiety = anxiety.dropna(subset=['START_DATE'])
anxiety['RECORDED_TIME'] = anxiety['RECORDED_TIME'].str[0:7] + '20' + anxiety['RECORDED_TIME'].str[7:]
anxiety['START_DATE'] = anxiety['START_DATE'].str[0:7] + '20' + anxiety['START_DATE'].str[7:]
anxiety['RECORDED_TIME'] = pd.to_datetime(anxiety['RECORDED_TIME'])
anxiety['START_DATE'] = pd.to_datetime(anxiety['START_DATE'])
anxiety['Difference'] = anxiety['START_DATE'].sub(anxiety['RECORDED_TIME'], axis=0)
anxiety['DAYS_BEFORE_SURGERY'] = anxiety['Difference'] / np.timedelta64(1, 'D')
anxiety['DAYS_BEFORE_SURGERY'] = anxiety['DAYS_BEFORE_SURGERY'].astype(int)
anxiety['x'] = anxiety.groupby('PAT_DEID')['DAYS_BEFORE_SURGERY'].transform('min')
anxiety = anxiety.loc[(anxiety['x']  == anxiety['DAYS_BEFORE_SURGERY'])]
anxiety = anxiety.drop_duplicates(['PAT_DEID'], keep='last')
print(anxiety.shape) #(875, 8)
######
anxiety = anxiety[['PAT_DEID','ANXIETY']]
print(anxiety.shape) #(875, 2)

pat_icd9 = pd.merge(patient_demog, icd9, on='PAT_DEID', how='outer')
print(pat_icd9.shape) #(5127, 29)
pat_icd9_meds = pd.merge(pat_icd9, meds, on='PAT_DEID', how='outer')
print(pat_icd9_meds.shape) #(5127, 60)
pat_icd9_meds_b = pd.merge(pat_icd9_meds, bp, on='PAT_DEID', how='outer')
print(pat_icd9_meds_b.shape) #(5127, 62)
pat_icd9_meds_bh = pd.merge(pat_icd9_meds_b, heart, on='PAT_DEID', how='outer')
print(pat_icd9_meds_bh.shape) #(5127, 63)
pat_icd9_meds_bht = pd.merge(pat_icd9_meds_bh, temp, on='PAT_DEID', how='outer')
print(pat_icd9_meds_bht.shape) #(5127, 64)
pat_icd9_meds_bhta = pd.merge(pat_icd9_meds_bht, anxiety, on='PAT_DEID', how='outer')
print(pat_icd9_meds_bhta.shape) #(5127, 65)

pat_icd9_meds_bhta.to_pickle("data_ml/FINAL_FEATURE_VECTOR.pkl")
writer = pd.ExcelWriter('data_ml/FINAL_FEATURE_VECTOR.xlsx')
pat_icd9_meds_bhta.to_excel(writer,'Sheet1')
writer.save()
