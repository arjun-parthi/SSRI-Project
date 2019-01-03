import pandas as pd
import numpy as np
file4 = '../data/VITALS_BP1.xlsx'
x4 = pd.ExcelFile(file4)
bp = x4.parse('Sheet1')
print(bp.shape)
print(bp.iloc[0:1])
print(bp.dtypes)
bp = bp.dropna(subset=['START_DATE'])
bp['RECORDED_TIME'] = bp['RECORDED_TIME'].str[0:7] + '20' + bp['RECORDED_TIME'].str[7:]
bp['START_DATE'] = bp['START_DATE'].str[0:7] + '20' + bp['START_DATE'].str[7:]
bp['RECORDED_TIME'] = pd.to_datetime(bp['RECORDED_TIME'])
bp['START_DATE'] = pd.to_datetime(bp['START_DATE'])

bp['Difference'] = bp['START_DATE'].sub(bp['RECORDED_TIME'], axis=0)
bp['DAYS_BEFORE_SURGERY'] = bp['Difference'] / np.timedelta64(1, 'D')
bp['DAYS_BEFORE_SURGERY'] = bp['DAYS_BEFORE_SURGERY'].astype(int)
bp['x'] = bp.groupby('PAT_DEID')['DAYS_BEFORE_SURGERY'].transform('min')
print(bp.shape)
print(bp.iloc[0:2])
print(bp.dtypes)
bp1 = bp.loc[(bp['x']  == bp['DAYS_BEFORE_SURGERY'])]
print(bp1.shape)
print(bp1.iloc[0:2])
bp1['y'] = bp1.groupby('PAT_DEID')['ABS_1'].transform('max')
bp1 = bp1.loc[(bp1['y']  == bp1['CHANGE_SYSTOLIC'].abs())]
print(bp1.shape)
print(bp1.iloc[0:2])

bp2 = bp1.drop_duplicates(['PAT_DEID'], keep='last')
print(bp2.shape)
print(bp2.iloc[0:2])
