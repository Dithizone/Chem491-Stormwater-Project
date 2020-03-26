# This is a scratchpad for trying things out.

import pandas as pd
from UsefulThings import theheaders
from UsefulThings import printthedetails
from UsefulThings import gsites

# df2011f = pd.read_csv('data/2011f.csv', names=theheaders, index_col=None)
# df2012f = pd.read_csv('data/2012f.csv', names=theheaders, index_col=None)
# df2013f = pd.read_csv('data/2013f.csv', names=theheaders, index_col=None)
# df2014f = pd.read_csv('data/2014f.csv', names=theheaders, index_col=None)
# df2015f = pd.read_csv('data/2015f.csv', names=theheaders, index_col=None)
# df2016f = pd.read_csv('data/2016f.csv', names=theheaders, index_col=None)
# df2017f = pd.read_csv('data/2017f.csv', names=theheaders, index_col=None)
# df2018f = pd.read_csv('data/2018f.csv', names=theheaders, index_col=None)
# df2019f = pd.read_csv('data/2019f.csv', names=theheaders, index_col=None)
TheFData = pd.read_csv('data/TheFData.csv')

print('The QAQC Sample Types:')
for i in TheFData.loc[:, 'QAQC Sample Type'].unique():
    print(f'{i}')

print('\nThe Site IDs:')
for j in TheFData.loc[:, 'Site ID'].unique():
    print(f'{j}')

print('\n<<<Some of the above seem incorrect.>>>')
