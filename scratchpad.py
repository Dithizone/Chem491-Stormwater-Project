# This is a scratchpad for trying things out.
# Most recently (2020.4.2), this is double-checking that
# we got all the G data.

import pandas as pd
from UsefulThings import theheaders
from UsefulThings import printthedetails
from UsefulThings import fevents
from UsefulThings import gsites
from UsefulThings import datanames
import re

# df2011f = pd.read_csv('data/2011f.csv', names=theheaders, index_col=None)
# df2012f = pd.read_csv('data/2012f.csv', names=theheaders, index_col=None)
# df2013f = pd.read_csv('data/2013f.csv', names=theheaders, index_col=None)
# df2014f = pd.read_csv('data/2014f.csv', names=theheaders, index_col=None)
# df2015f = pd.read_csv('data/2015f.csv', names=theheaders, index_col=None)
# df2016f = pd.read_csv('data/2016f.csv', names=theheaders, index_col=None)
# df2017f = pd.read_csv('data/2017f.csv', names=theheaders, index_col=None)
# df2018f = pd.read_csv('data/2018f.csv', names=theheaders, index_col=None)
# df2019f = pd.read_csv('data/2019f.csv', names=theheaders, index_col=None)

uniques = []
totalgdata = 0
totalgdataincsv = 0
totalgdatain2011 = 0
GDatafiles = ['2012g', '2013g', '2015g', '2016g', '2017g', '2018g', '2019g']

for name in datanames:
    with open(file=f'data/precsv/precsv{name}.txt', mode='r') as file:
        precsv = file.read().replace(',', '||').split(sep='\n')
        for i in range(len(precsv)):
            splitprecsv = precsv[i].split(sep=' ')
            if splitprecsv[0] not in fevents:
                if splitprecsv[0] != '':
                    totalgdata += 1

for individualfile in GDatafiles:
    with open(file=f'data/{individualfile}.csv', mode='r') as file2:
        csv = file2.read().replace(',', '||').split(sep='\n')
        totalgdataincsv += len(csv)

with open(file=f'data/precsv/precsv2011fg.txt', mode='r') as file3:
    precsv3 = file3.read().replace(',', '||').split(sep='\n')
    for i in range(len(precsv3)):
        splitprecsv3 = precsv3[i].split(sep=' ')
        if splitprecsv3[0] not in fevents:
            if splitprecsv3[0] != '':
                totalgdatain2011 += 1

print(f'\nTotal of {totalgdata} entries in G data from precsv. Without 2011, {totalgdata - totalgdatain2011}.')
print(f'\nAnd the total in the csv files is {totalgdataincsv}.')
