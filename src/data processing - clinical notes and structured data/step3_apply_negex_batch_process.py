from negex import *
import csv
import nltk.data
import pandas as pd
import numpy as np

file1 = 'dep_terms.xlsx'
x1 = pd.ExcelFile(file1)
df1 = x1.parse('depression')
terms = df1['Terms'].tolist()
terms1 = [str(x).lower() for x in terms]

def neg(inp):
    rfile = open(r'negex_triggers.txt')
    irules = sortRules(rfile.readlines())
    reports = csv.reader(open(r'files/small_ts_improve_{0}.txt'.format(inp),'r'), delimiter = '\t')
    next(reports)
    reportNum = 0
    correctNum = 0
    ofile = open(r'output/ts_negex_{0}.txt'.format(inp), 'w')
    output = []
    outputfile = csv.writer(ofile, delimiter = '\t')
    for i,report in enumerate(reports):
        tagger = negTagger(sentence = report[5], phrases = terms1, rules = irules, negP=False)
        report.append(tagger.getNegationFlag())
        output.append(report)
        print("Line{}".format(i))
    for row in output:
        if row:
            outputfile.writerow(row)
    ofile.close()

def main():
    for i in range(2000, 358000, 2000):
        print("File number_{0}".format(i))
        neg(i)

# neg(357072)
if __name__ == '__main__': main()
