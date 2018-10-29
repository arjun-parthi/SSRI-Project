import pandas as pd
import numpy as np

################################
##### From Clinical Notes #####
################################
data_antidep_notes = pd.read_pickle('text_snippets_antidepressants_shorten.pkl')

file1 = 'AP_SURGERY_PROCEDURE.xlsx'
x1 = pd.ExcelFile(file1)
data_surgeries = x1.parse('Sheet1')
data_surgeries_required = data_surgeries[['PAT_DEID','START_DATE']]
antidep_surgeries = pd.merge(data_antidep_notes, data_surgeries_required, on='PAT_DEID', how='inner')

print(antidep_surgeries.shape) #(293974, 8)
print(data_antidep_notes.PAT_DEID.nunique()) #3647
print(antidep_surgeries.PAT_DEID.nunique()) #2988

antidep_surgeries1 = antidep_surgeries.copy()
antidep_surgeries1['START_DATE_start'] = pd.to_datetime(antidep_surgeries1['START_DATE'],format='%d-%b-%y')
antidep_surgeries1['START_DATE_end'] = antidep_surgeries1['START_DATE_start'] - pd.to_timedelta(365,unit='d')
antidep_surgeries1['ENCOUNTER_DATE_dt'] = pd.to_datetime(antidep_surgeries1['ENCOUNTER_DATE'],format='%d-%b-%y')
antidep_sur_1year = antidep_surgeries1.loc[(antidep_surgeries1['ENCOUNTER_DATE_dt'] <= antidep_surgeries1['START_DATE_start']) & (antidep_surgeries1['ENCOUNTER_DATE_dt'] >= antidep_surgeries1['START_DATE_end'])]
print(antidep_sur_1year.shape) #(66305, 11)
print(antidep_sur_1year.PAT_DEID.nunique()) #1892

antidep_sur_1year.to_pickle("out/antidep_notes_1yr.pkl")
# data1 = df2.iloc[0:300]
writer = pd.ExcelWriter('out/antidep_notes_1yr.xlsx')
antidep_sur_1year.to_excel(writer,'Sheet1')
writer.save()
################################
#### From STRIDE MEDICATION ####
################################
## Changed START_TIME to START_TIME_med
file4 = 'DB/AP_STRIDE_SSRI_FINAL.xlsx'
x4 = pd.ExcelFile(file4)
ssri_all = x4.parse('Sheet1')
print(ssri_all.shape) #(27269, 31)
ssri_surgeries = pd.merge(ssri_all, data_surgeries_required, on='PAT_DEID', how='inner')

print(ssri_surgeries.shape) #(61558, 32)
print(ssri_all.PAT_DEID.nunique()) #5794
print(ssri_surgeries.PAT_DEID.nunique()) #4597

ssri_surgeries1 = ssri_surgeries.copy()
ssri_surgeries1['START_DATE_start'] = pd.to_datetime(ssri_surgeries1['START_DATE'],format='%d-%b-%y')
ssri_surgeries1['START_DATE_end'] = ssri_surgeries1['START_DATE_start'] - pd.to_timedelta(365,unit='d')
ssri_surgeries1['ORDER_TIME_dt'] = pd.to_datetime(ssri_surgeries1['ORDER_TIME'],format='%d-%b-%y')
ssri_sur_1year = ssri_surgeries1.loc[(ssri_surgeries1['ORDER_TIME_dt'] <= ssri_surgeries1['START_DATE_start']) & (ssri_surgeries1['ORDER_TIME_dt'] >= ssri_surgeries1['START_DATE_end'])]
print(ssri_sur_1year.shape) #(13438, 35)
print(ssri_sur_1year.PAT_DEID.nunique()) #2831


ssri_sur_1year.to_pickle("out/antidep_ssri_med_1yr.pkl")
# data1 = df2.iloc[0:300]
writer = pd.ExcelWriter('out/antidep_ssri_med_1yr.xlsx')
ssri_sur_1year.to_excel(writer,'Sheet1')
writer.save()
