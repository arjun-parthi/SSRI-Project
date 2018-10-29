import pandas as pd
import numpy as np

depression_affirmed_1yr = pd.read_pickle('out/depression_affirmed_1yr.pkl')

##Changed START_DATE to ENCOUNTER_DATE
file4 = 'DB/AP_DEP_PAT_DIAG.xlsx'
x4 = pd.ExcelFile(file4)
icd9_all = x4.parse('Sheet1')
print(icd9_all.shape) #(63528, 21)

file1 = 'AP_SURGERY_PROCEDURE.xlsx'
x1 = pd.ExcelFile(file1)
data_surgeries = x1.parse('Sheet1')
data_surgeries_required = data_surgeries[['PAT_DEID','START_DATE']]
dep_icd9_surgeries = pd.merge(icd9_all, data_surgeries_required, on='PAT_DEID', how='inner')

print(dep_icd9_surgeries.shape) #(159929, 22)
print(icd9_all.PAT_DEID.nunique()) #7831
print(dep_icd9_surgeries.PAT_DEID.nunique()) #6282
dep_icd9_surgeries1 = dep_icd9_surgeries.copy()
dep_icd9_surgeries1['START_DATE_start'] = pd.to_datetime(dep_icd9_surgeries1['START_DATE'],format='%d-%b-%y')
dep_icd9_surgeries1['START_DATE_end'] = dep_icd9_surgeries1['START_DATE_start'] - pd.to_timedelta(365,unit='d')
dep_icd9_surgeries1['ENCOUNTER_DATE_dt'] = pd.to_datetime(dep_icd9_surgeries1['ENCOUNTER_DATE'],format='%d-%b-%y')
dep_icd9_sur_1year = dep_icd9_surgeries1.loc[(dep_icd9_surgeries1['ENCOUNTER_DATE_dt'] <= dep_icd9_surgeries1['START_DATE_start']) & (dep_icd9_surgeries1['ENCOUNTER_DATE_dt'] >= dep_icd9_surgeries1['START_DATE_end'])]
print(dep_icd9_sur_1year.shape) #(33636, 25)
print(dep_icd9_sur_1year.PAT_DEID.nunique()) #4066

dep_icd9_sur_1year.to_pickle("out/depression_icd9_1yr.pkl")
# data1 = df2.iloc[0:300]
writer = pd.ExcelWriter('out/depression_icd9_1yr.xlsx')
dep_icd9_sur_1year.to_excel(writer,'Sheet1')
writer.save()


print("Matching between depression notes and depression icd9")
notes_icd9 = pd.merge(depression_affirmed_1yr, dep_icd9_sur_1year, on='PAT_DEID', how='inner')

print(notes_icd9.PAT_DEID.nunique()) #1751
print(notes_icd9.shape) #(1890761, 33)

print("All depression either in depression notes or depression icd9")
notes_icd9_all = pd.merge(depression_affirmed_1yr, dep_icd9_sur_1year, on='PAT_DEID', how='outer')
print(notes_icd9_all.PAT_DEID.nunique()) #5978
print(notes_icd9_all.shape) #(1929955, 33)

notes_icd9_all.to_pickle("out/depression_icd9_all_1yr.pkl")

new = notes_icd9_all[['PAT_DEID']].copy()
notes_icd9_all_pat_unique = new.drop_duplicates(subset='PAT_DEID', keep="last")
print(notes_icd9_all_pat_unique.shape) #(5978, 1)
print(notes_icd9_all_pat_unique.PAT_DEID.nunique()) #5978
notes_icd9_all_pat_unique.to_pickle("out/dep_icd9_all_1yr_pat.pkl")
writer = pd.ExcelWriter('out/dep_icd9_all_1yr_pat.xlsx')
notes_icd9_all_pat_unique.to_excel(writer,'Sheet1')
writer.save()
