# This is a scratchpad for trying things out.
# Most recently (2020.03.28), this is generating data to motivate FixingFData.py

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

TheFData = pd.read_csv('data/TheFDataComplete.csv.csv')

print('The QAQC Sample Types:')
for i in TheFData.loc[:, 'QAQC Sample Type'].unique():
    print(f'"{i}",')

print('\nThe Site IDs:')
for j in TheFData.loc[:, 'Site ID'].unique():
    print(f'"{j}",')

print('\n<<<All of the above seem reasonable.>>>')

QAQCwhichseemwrong = ["Blank (distille equip blank",
                      "Blank (distille srgt equip blank",
                      "Blank (distille srgt equip blank|| rec",
                      "(old) equip blank",
                      "2L (plastic) equip blank",
                      "(old) srgt equip blank",
                      "(old) srgt equip blank|| rec",
                      "2L (plastic) srgt equip blank",
                      "2L (plastic) srgt equip blank|| rec",
                      "(HNO3||methanol) equip blank",
                      "(HNO3||methanol) srgt equip blank",
                      "(HNO3||methanol)srgt equip blank|| rec",
                      "Blank (HNO3||me equip blank",
                      "Blank (HNO3||me matrix spike",
                      "Blank (HNO3||me matrix spike|| rec",
                      "Blank (HNO3||me matrix spike dup",
                      "Blank (HNO3||me matrix spike dup|| rec",
                      "Blank (HNO3||me matrix spike|| RPD",
                      "Blank (HNO3||me srgt matrix spike",
                      "Blank (HNO3||me srgt matrix spike|| rec",
                      "Blank (HNO3||me srgt matrix spike dup",
                      "Blank (HNO3||me srgt matrix spike dup|| rec",
                      "Blank (HNO3||me srgt equip blank",
                      "Blank (HNO3||me srgt equip blank|| rec",
                      " srgt environ",
                      " srgt environ|| rec"]  # These have been fixed now.

SiteIDwhichseemwrong = ["RC",
                        "ubing",
                        "Rinse",
                        "y"]  # These have been fixed now.

# Let's look at the entries which contains these
#
#
# for i in range(len(QAQCwhichseemwrong)):
#     thewwrongentries = TheFData.loc[:, 'QAQC Sample Type'] == QAQCwhichseemwrong[i]
#     print(f'\nRows with {QAQCwhichseemwrong[i]}')
#     print(TheFData[thewwrongentries].iloc[:, [0, 1, 2]])
#     print(TheFData[thewwrongentries].iloc[:, [0, 1, 2]].shape)
