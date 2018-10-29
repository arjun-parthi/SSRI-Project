import pandas as pd
import numpy as np

depression = pd.read_pickle('out/dep_icd9_all_1yr_pat.pkl')
ssri = pd.read_pickle('out/antidep_all_1yr_pat.pkl')
print(depression.PAT_DEID.nunique()) #5978
print(depression.shape) #(5978, 1)
print(ssri.PAT_DEID.nunique()) #3531
print(ssri.shape) #(3531, 1)
print("Matching between depression and SSRI")
dep_antidep = pd.merge(depression, ssri, on='PAT_DEID', how='inner')

print(dep_antidep.PAT_DEID.nunique()) #2650
print(dep_antidep.shape) #(2650, 1)

dep_antidep.to_pickle("out/dep_antidep_all_1yr_pat.pkl")
writer = pd.ExcelWriter('out/dep_antidep_all_1yr_pat.xlsx')
dep_antidep.to_excel(writer,'Sheet1')
writer.save()
