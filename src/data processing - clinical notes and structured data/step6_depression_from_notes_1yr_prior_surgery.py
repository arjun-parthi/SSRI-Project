import pandas as pd
import numpy as np


data_notes = pd.read_pickle('out/annotated_note_all.pkl')
file1 = 'AP_SURGERY_PROCEDURE.xlsx'
x1 = pd.ExcelFile(file1)
data_surgeries = x1.parse('Sheet1')
print(data_notes.shape) #(145556, 8)
print(data_surgeries.shape) #(105976, 16)

dep_affirmed = data_notes.loc[data_notes['STATUS_FINAL'].isin(['Affirmed'])]
print(dep_affirmed.shape) #(138233, 8)
dep_negated = data_notes.loc[data_notes['STATUS_FINAL'].isin(['Negated'])]
print(dep_negated.shape) #(7323, 8)

data_surgeries_required = data_surgeries[['PAT_DEID','START_DATE']]
dep_affirmed_surgeries = pd.merge(dep_affirmed, data_surgeries_required, on='PAT_DEID', how='inner')
print(dep_affirmed_surgeries.shape) #(338977, 9)
print(dep_affirmed.PAT_DEID.nunique()) #5530
print(dep_affirmed_surgeries.PAT_DEID.nunique()) #4501
dep_affirmed_surgeries1 = dep_affirmed_surgeries.copy()
dep_affirmed_surgeries1['START_DATE_start'] = pd.to_datetime(dep_affirmed_surgeries1['START_DATE'],format='%d-%b-%y')
dep_affirmed_surgeries1['START_DATE_end'] = dep_affirmed_surgeries1['START_DATE_start'] - pd.to_timedelta(365,unit='d')
dep_affirmed_surgeries1['NOTE_DATE_dt'] = pd.to_datetime(dep_affirmed_surgeries1['NOTE_DATE'],format='%d-%b-%y')
dep_affirmed_surgeries1['ENCOUNTER_DATE_dt'] = pd.to_datetime(dep_affirmed_surgeries1['ENCOUNTER_DATE'],format='%d-%b-%y')
dep_aff_sur_1year = dep_affirmed_surgeries.loc[(dep_affirmed_surgeries1['ENCOUNTER_DATE_dt'] <= dep_affirmed_surgeries1['START_DATE_start']) & (dep_affirmed_surgeries1['ENCOUNTER_DATE_dt'] >= dep_affirmed_surgeries1['START_DATE_end'])]

print(dep_aff_sur_1year.shape) #(86248, 9)
print(dep_aff_sur_1year.PAT_DEID.nunique()) #3663

dep_aff_sur_1year.to_pickle("out/depression_affirmed_1yr.pkl")
writer = pd.ExcelWriter('out/depression_affirmed_1yr.xlsx')
dep_aff_sur_1year.to_excel(writer,'Sheet1')
writer.save()
