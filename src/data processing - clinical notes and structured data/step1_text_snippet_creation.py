import nltk.data
import pandas as pd
import numpy as np
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Input File 1 - List of depression terms
file1 = 'dep_terms.xlsx'
x1 = pd.ExcelFile(file1)
df1 = x1.parse('depression')

# Input file 2 - All notes
file2 = 'dep_note.xlsx'
x2 = pd.ExcelFile(file2)
df2 = x2.parse(sheet_name = 'SURGERYPAIN.AP_DEP_STRIDE_NOTE')

df4 = df2.copy()
df3 = df2.apply(lambda row : pd.Series(tokenizer.tokenize(str(row['NOTE']))), axis=1)

df5 = df2.join(df3)
df6 = pd.melt(df5, id_vars=["PAT_DEID", "NOTE_DEID", "NOTE_DATE", "ENCOUNTER_DATE", "NOTE_CODE", "NOTE"],
                  value_name="TEXT_SNIPPET")

df6['TEXT_SNIPPET'].replace('', np.nan, inplace=True)
df6.dropna(subset=['TEXT_SNIPPET'], inplace=True)

df6.drop(['NOTE','variable'], axis=1, inplace=True)
terms = df1['Terms'].tolist()
terms1 = [str(x).lower() for x in terms]
df7 = df6.copy()

df6['lower_text'] = df6['TEXT_SNIPPET'].str.lower()
df8 = df6[df6['lower_text'].str.contains('|'.join(terms1), regex = True)]
df8.to_pickle("text_snippets_after_exclusions.pkl")
df8.to_csv(r'text_snippets_after_exclusions.txt', header=None, index=None, sep='\t', mode='a')
