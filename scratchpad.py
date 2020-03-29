# This is a scratchpad for trying things out.
# Most recently (2020.03.29), this is determining whether
# 'Wet' and 'Dry' are word I can anchor the G data to.

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
wet = 0
dry = 0

for name in datanames:
    with open(file=f'data/precsv/precsv{name}.txt', mode='r') as file:
        precsv = file.read().replace(',', '||').split(sep='\n')
        for i in range(len(precsv)):
            splitprecsv = precsv[i].split(sep=' ')
            if splitprecsv[0] not in fevents:
                if splitprecsv[0] != '':
                    totalgdata += 1
                    if splitprecsv[2] not in uniques:
                        uniques.append(splitprecsv[2])
                        print(f'{splitprecsv[2]}\t\t(in {name})')
                    for k in splitprecsv:
                        if re.search('Dry', k) is not None:
                            wet += 1
                        if re.search('Wet', k) is not None:
                            dry += 1

print('\n')
print('The entire list (omitting fevents):')
for j in uniques:
    if j not in fevents:
        print(j)

print(f'\nTotal of {totalgdata} entries in G data. Also, {wet} Wet and {dry} Dry, total {wet + dry}.')
