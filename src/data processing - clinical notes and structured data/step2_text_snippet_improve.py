from negex import *
import csv
import nltk.data
import pandas as pd
import numpy as np
import re

file1 = 'dep_terms.xlsx'
x1 = pd.ExcelFile(file1)
df1 = x1.parse('depression')
terms = df1['Terms'].tolist()
terms1 = [str(x).lower() for x in terms]

data = pd.read_pickle("text_snippets_after_exclusions.pkl")

def splitting(li):
    lis1 = re.split("  +",li)
    return lis1

data1 = data.copy()
data_copy = data.copy()
data = data1.drop('lower_text', axis=1)
df3 = data.apply(lambda row : splitting(str(row['TEXT_SNIPPET'])), axis=1)
df5 = data.join(df3.to_frame())
print(df5.shape)
print(df3.shape)
print(data.shape)

df6 = df5.drop('TEXT_SNIPPET', axis=1)
df6.columns = ['PAT_DEID','NOTE_DEID','NOTE_DATE','ENCOUNTER_DATE','NOTE_CODE','TEXT_SNIPPET']
print(df6.shape)

def explode(df, lst_cols, fill_value=''):
    # make sure `lst_cols` is a list
    if lst_cols and not isinstance(lst_cols, list):
        lst_cols = [lst_cols]
    # all columns except `lst_cols`
    idx_cols = df.columns.difference(lst_cols)

    # calculate lengths of lists
    lens = df[lst_cols[0]].str.len()

    if (lens > 0).all():
        # ALL lists in cells aren't empty
        return pd.DataFrame({
            col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
            for col in idx_cols
        }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
          .loc[:, df.columns]
    else:
        # at least one list in cells is empty
        return pd.DataFrame({
            col:np.repeat(df[col].values, df[lst_cols[0]].str.len())
            for col in idx_cols
        }).assign(**{col:np.concatenate(df[col].values) for col in lst_cols}) \
          .append(df.loc[lens==0, idx_cols]).fillna(fill_value) \
          .loc[:, df.columns]


df7 = explode(df6, ['TEXT_SNIPPET'], fill_value='')
print(df7.shape)


df7['lower_text'] = df7['TEXT_SNIPPET'].str.lower()
df8 = df7[df7['lower_text'].str.contains('|'.join(terms1), regex = True)]
print(df8.shape)
print(df8.iloc[1:5,6])
df8.to_pickle("text_snippets_improve_all.pkl")
df8.to_csv(r'text_snippets_improve_all.txt', header=None, index=None, sep='\t', mode='a')
