import pandas as pd
import numpy as np
from collections import Counter

data = pd.read_csv('out/negex_all.txt', sep="\t", header=None)
print(data.shape)

data.columns = ['PAT_DEID','NOTE_DEID','NOTE_DATE','ENCOUNTER_DATE','NOTE_CODE','TEXT_SNIPPET','lower_text','STATUS']
df = data.groupby(['PAT_DEID','NOTE_DEID','NOTE_DATE','ENCOUNTER_DATE','NOTE_CODE'])['STATUS'].apply(','.join).reset_index()
df_text = data.groupby(['PAT_DEID','NOTE_DEID','NOTE_DATE','ENCOUNTER_DATE','NOTE_CODE'])['TEXT_SNIPPET'].apply(' ##### '.join).reset_index()
df_text_required = df_text[['NOTE_DEID','TEXT_SNIPPET']]
df_fin = pd.merge(df, df_text_required, on='NOTE_DEID', how='inner')
df1 = df_fin.copy()

def check(l):
    # l1 = l['STATUS'].tolist()
    # l2 = str(l1).split(',')
    l2 = l['STATUS'].split(',')
    c = Counter(l2)
    affirmed = c['affirmed']
    negated = c['negated']
    if (affirmed > negated or affirmed == negated):
        return "Affirmed"
    else:
        return "Negated"

def majority_rule(var1,var2):
    df[var2] = df.apply(check, axis = 1)
    return df

df1 = majority_rule('STATUS','STATUS_FINAL')
print(df1.shape)
df2 = pd.merge(df1, df_text_required, on='NOTE_DEID', how='inner')

df2.to_pickle("out/annotated_note_all.pkl")
