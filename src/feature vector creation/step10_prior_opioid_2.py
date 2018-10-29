import pandas as pd
import numpy as np
file1 = 'data_ml/meds_req.xlsx'
x1 = pd.ExcelFile(file1)
meds = x1.parse('Sheet1')
print(meds.shape) #(151751, 13)
meds = meds.dropna(subset=['START_TIME'])
print(meds.shape) #(149980, 13)

file2 = 'data_ml/DATE.xlsx'
x2 = pd.ExcelFile(file2)
date = x2.parse('Sheet1')
print(date.shape) #(5955, 3)

bp = pd.merge(meds, date, on='PAT_DEID', how='inner')
print(bp.shape) #(171452, 15)

bp = bp.dropna(subset=['START_TIME'])
bp['START_TIME'] = bp['START_TIME'].str[0:7] + '20' + bp['START_TIME'].str[7:]
bp['START_DATE'] = bp['START_DATE'].str[0:7] + '20' + bp['START_DATE'].str[7:]
print(bp.shape) #(171452, 15)
bp['START_TIME'] = pd.to_datetime(bp['START_TIME'])
bp['START_DATE'] = pd.to_datetime(bp['START_DATE'])
bp['Difference'] = bp['START_DATE'].sub(bp['START_TIME'], axis=0)
print(bp.shape) #(171452, 16)
bp['DAYS_BEFORE_SURGERY'] = bp['Difference'] / np.timedelta64(1, 'D')
bp['DAYS_BEFORE_SURGERY'] = bp['DAYS_BEFORE_SURGERY'].astype(int)

bp1 = bp[((bp.DAYS_BEFORE_SURGERY > 7) & (bp.DAYS_BEFORE_SURGERY < 366))]
print(bp1.shape) #(20522, 17)
bp1.to_pickle("data_ml/prior_opioid_pat.pkl")

writer = pd.ExcelWriter('data_ml/prior_opioid_pat.xlsx')
bp1.to_excel(writer,'Sheet1')
writer.save()
