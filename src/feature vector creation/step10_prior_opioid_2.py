import pandas as pd
import numpy as np
file1 = '../data/meds_req.xlsx'
x1 = pd.ExcelFile(file1)
meds = x1.parse('Sheet1')
print(meds.shape)
meds = meds.dropna(subset=['START_TIME'])
print(meds.shape)

file2 = '../data/SURGERY_DATE.xlsx'
x2 = pd.ExcelFile(file2)
date = x2.parse('Sheet1')
print(date.shape)
date = date.drop(['CLASSIFICATION'], axis=1)

bp = pd.merge(meds, date, on='PAT_DEID', how='inner')
print(bp.shape)

bp = bp.dropna(subset=['START_TIME'])
bp = bp[bp.START_TIME.notnull()]
bp['START_TIME'] = bp['START_TIME'].str[0:7] + '20' + bp['START_TIME'].str[7:]
bp['START_DATE'] = bp['START_DATE'].str[0:7] + '20' + bp['START_DATE'].str[7:]
print(bp.shape)
bp['START_TIME'] = pd.to_datetime(bp['START_TIME'])
bp['START_DATE'] = pd.to_datetime(bp['START_DATE'])
bp['Difference'] = bp['START_DATE'].sub(bp['START_TIME'], axis=0)
print(bp.shape)
bp['DAYS_BEFORE_SURGERY'] = bp['Difference'] / np.timedelta64(1, 'D')
bp['DAYS_BEFORE_SURGERY'] = bp['DAYS_BEFORE_SURGERY'].astype(int)

bp1 = bp[((bp.DAYS_BEFORE_SURGERY > 7) & (bp.DAYS_BEFORE_SURGERY < 366))]
print(bp1.shape)
bp1['OPIOID_TOLERANT']='YES'

writer = pd.ExcelWriter('../data/prior_opioid_pat.xlsx')
bp1.to_excel(writer,'Sheet1')
writer.save()
