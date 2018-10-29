import pandas as pd
import numpy as np

antidep_sur_1year = pd.read_pickle('out/antidep_notes_1yr.pkl')
ssri_sur_1year = pd.read_pickle('out/antidep_ssri_med_1yr.pkl')

print("Matching between antidep notes and antidep medication table")
notes_medtable = pd.merge(antidep_sur_1year, ssri_sur_1year, on='PAT_DEID', how='inner')

print(notes_medtable.PAT_DEID.nunique()) #1192
print(notes_medtable.shape) #(1093623, 45)

print("All antidep either in antidep notes or antidep medication table")
notes_medtable_all = pd.merge(antidep_sur_1year, ssri_sur_1year, on='PAT_DEID', how='outer')
print(notes_medtable_all.PAT_DEID.nunique()) #3531
print(notes_medtable_all.shape) #(1109390, 45)

notes_medtable_all.to_pickle("out/antidep_all_1yr.pkl")

new = notes_medtable_all[['PAT_DEID']].copy()
notes_med_all_pat_unique = new.drop_duplicates(subset='PAT_DEID', keep="last")
print(notes_med_all_pat_unique.shape) #(3531, 1)
print(notes_med_all_pat_unique.PAT_DEID.nunique()) #3531
notes_med_all_pat_unique.to_pickle("out/antidep_all_1yr_pat.pkl")
writer = pd.ExcelWriter('out/antidep_all_1yr_pat.xlsx')
notes_med_all_pat_unique.to_excel(writer,'Sheet1')
writer.save()
