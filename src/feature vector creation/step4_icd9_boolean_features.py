import pandas as pd
import numpy as np

file1 = 'data_ml/ICD9_features.xlsx'
x1 = pd.ExcelFile(file1)
icd9 = x1.parse('Sheet1')
print(icd9.shape) #(541543, 19)
print(icd9.iloc[0:1])
print(icd9.dtypes)

icd9 = icd9.drop(['ICD9_LIST'], axis=1)
icd9_new = icd9.groupby(icd9.PAT_DEID).sum()
print(icd9_new.shape) #(1560, 18)
print(icd9_new.iloc[0:1])
print(icd9_new.dtypes)


def to_bool(A):
    if A > 0:
        val = 1
    else:
        val = 0
    return val


icd9_new['ICD9_001'] = icd9_new['ICD9_001'].apply(to_bool)
icd9_new['ICD9_140'] = icd9_new['ICD9_140'].apply(to_bool)
icd9_new['ICD9_240'] = icd9_new['ICD9_240'].apply(to_bool)
icd9_new['ICD9_280'] = icd9_new['ICD9_280'].apply(to_bool)
icd9_new['ICD9_290'] = icd9_new['ICD9_290'].apply(to_bool)
icd9_new['ICD9_320'] = icd9_new['ICD9_320'].apply(to_bool)
icd9_new['ICD9_390'] = icd9_new['ICD9_390'].apply(to_bool)
icd9_new['ICD9_460'] = icd9_new['ICD9_460'].apply(to_bool)
icd9_new['ICD9_520'] = icd9_new['ICD9_520'].apply(to_bool)
icd9_new['ICD9_580'] = icd9_new['ICD9_580'].apply(to_bool)
icd9_new['ICD9_630'] = icd9_new['ICD9_630'].apply(to_bool)
icd9_new['ICD9_680'] = icd9_new['ICD9_680'].apply(to_bool)
icd9_new['ICD9_710'] = icd9_new['ICD9_710'].apply(to_bool)
icd9_new['ICD9_740'] = icd9_new['ICD9_740'].apply(to_bool)
icd9_new['ICD9_760'] = icd9_new['ICD9_760'].apply(to_bool)
icd9_new['ICD9_780'] = icd9_new['ICD9_780'].apply(to_bool)
icd9_new['ICD9_800'] = icd9_new['ICD9_800'].apply(to_bool)
icd9_new['ICD9_EV'] = icd9_new['ICD9_EV'].apply(to_bool)
print(icd9_new.shape) #(1560, 18)
print(icd9_new.iloc[0:1])
print(icd9_new.dtypes)

writer = pd.ExcelWriter('data_ml/ICD9_final_features.xlsx')
icd9_new.to_excel(writer,'Sheet1')
writer.save()
