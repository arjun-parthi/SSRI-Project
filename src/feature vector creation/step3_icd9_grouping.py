import pandas as pd
import numpy as np

file1 = '../data/ICD9_final1.xlsx'
x1 = pd.ExcelFile(file1)
icd9 = x1.parse('Sheet1')
print(icd9.shape)
print(icd9.iloc[0:1])
print(icd9.dtypes)


def ICD9_001(row):
    if row['ICD9_LIST'] < 140:
        val = 1
    else:
        val = 0
    return val

def ICD9_140(row):
    if (row['ICD9_LIST'] >= 140.0 and row['ICD9_LIST'] < 240.0):
        val = 1
    else:
        val = 0
    return val

def ICD9_240(row):
    if row['ICD9_LIST'] >= 240 and row['ICD9_LIST'] < 280:
        val = 1
    else:
        val = 0
    return val

def ICD9_280(row):
    if row['ICD9_LIST'] >= 280 and row['ICD9_LIST'] < 290:
        val = 1
    else:
        val = 0
    return val

def ICD9_290(row):
    if row['ICD9_LIST'] >= 290 and row['ICD9_LIST'] < 320:
        val = 1
    else:
        val = 0
    return val

def ICD9_320(row):
    if row['ICD9_LIST'] >= 320 and row['ICD9_LIST'] < 390:
        val = 1
    else:
        val = 0
    return val

def ICD9_390(row):
    if row['ICD9_LIST'] >= 390 and row['ICD9_LIST'] < 460:
        val = 1
    else:
        val = 0
    return val

def ICD9_460(row):
    if row['ICD9_LIST'] >= 460 and row['ICD9_LIST'] < 520:
        val = 1
    else:
        val = 0
    return val

def ICD9_520(row):
    if row['ICD9_LIST'] >= 520 and row['ICD9_LIST'] < 580:
        val = 1
    else:
        val = 0
    return val

def ICD9_580(row):
    if row['ICD9_LIST'] >= 580 and row['ICD9_LIST'] < 630:
        val = 1
    else:
        val = 0
    return val

def ICD9_630(row):
    if row['ICD9_LIST'] >= 630 and row['ICD9_LIST'] < 680:
        val = 1
    else:
        val = 0
    return val

def ICD9_680(row):
    if row['ICD9_LIST'] >= 680 and row['ICD9_LIST'] < 710:
        val = 1
    else:
        val = 0
    return val

def ICD9_710(row):
    if row['ICD9_LIST'] >= 710 and row['ICD9_LIST'] < 740:
        val = 1
    else:
        val = 0
    return val

def ICD9_740(row):
    if row['ICD9_LIST'] >= 740 and row['ICD9_LIST'] < 760:
        val = 1
    else:
        val = 0
    return val

def ICD9_760(row):
    if row['ICD9_LIST'] >= 760 and row['ICD9_LIST'] < 780:
        val = 1
    else:
        val = 0
    return val

def ICD9_780(row):
    if row['ICD9_LIST'] >= 780 and row['ICD9_LIST'] < 800:
        val = 1
    else:
        val = 0
    return val

def ICD9_800(row):
    if row['ICD9_LIST'] >= 800 and row['ICD9_LIST'] < 1000:
        val = 1
    else:
        val = 0
    return val

def ICD9_EV(row):
    if row['ICD9_LIST'] > 99990:
        val = 1
    else:
        val = 0
    return val

icd9['ICD9_LIST'] = icd9['ICD9_LIST'].str.replace('E','99991')
icd9['ICD9_LIST'] = icd9['ICD9_LIST'].str.replace('V','99992')
icd9['ICD9_LIST'] = icd9['ICD9_LIST'].str.replace('IMO','5')
icd9['ICD9_LIST'] = icd9['ICD9_LIST'].astype(float).fillna(0.0)
icd9['ICD9_EV'] = icd9.apply(ICD9_EV, axis=1)
icd9['ICD9_001'] = icd9.apply(ICD9_001, axis=1)
icd9['ICD9_140'] = icd9.apply(ICD9_140, axis=1)
icd9['ICD9_240'] = icd9.apply(ICD9_240, axis=1)
icd9['ICD9_280'] = icd9.apply(ICD9_280, axis=1)
icd9['ICD9_290'] = icd9.apply(ICD9_290, axis=1)
icd9['ICD9_320'] = icd9.apply(ICD9_320, axis=1)
icd9['ICD9_390'] = icd9.apply(ICD9_390, axis=1)
icd9['ICD9_460'] = icd9.apply(ICD9_460, axis=1)
icd9['ICD9_520'] = icd9.apply(ICD9_520, axis=1)
icd9['ICD9_580'] = icd9.apply(ICD9_580, axis=1)
icd9['ICD9_630'] = icd9.apply(ICD9_630, axis=1)
icd9['ICD9_680'] = icd9.apply(ICD9_680, axis=1)
icd9['ICD9_710'] = icd9.apply(ICD9_710, axis=1)
icd9['ICD9_740'] = icd9.apply(ICD9_740, axis=1)
icd9['ICD9_760'] = icd9.apply(ICD9_760, axis=1)
icd9['ICD9_780'] = icd9.apply(ICD9_780, axis=1)
icd9['ICD9_800'] = icd9.apply(ICD9_800, axis=1)

print(icd9.shape)
print(icd9.iloc[0:1])
print(icd9.dtypes)

writer = pd.ExcelWriter('../data/ICD9_features.xlsx')
icd9.to_excel(writer,'Sheet1')
writer.save()
