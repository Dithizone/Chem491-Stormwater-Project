# The first step is to gather all the data in a workable format.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

datanames = ['2019fg',
             '2018fg',
             '2017g',
             '2017f',
             '2016g',
             '2016f',
             '2015fg',
             '2014f',
             '2013fg',
             '2012g',
             '2012f',
             '2011fg']

datanamestest = ['2011fg']

fevents = ['2018/19-1',
           '2018/19-2',
           '2018/19-3',
           '2018/19-4',
           '2018/19-5',
           '2018/19-PRE',
           '2019-DRY',
           '2017/18-1',
           '2017/18-2',
           '2017/18-3',
           '2017/18-4',
           '2017/18-5',
           '2017/18-PRE',
           '2018-DRY',
           '2016/17-1',
           '2016/17-2',
           '2016/17-3',
           '2016/17-4',
           '2016/17-5',
           '2016/17-6',
           '2016/17-PRE',
           '2017-DRY',
           '2015/16-1',
           '2015/16-2',
           '2015/16-3',
           '2015/16-4',
           '2015/16-5',
           '2015/16-PRE',
           'PS-2015',
           '2016-DRY',
           '2014/15-1',
           '2014/15-2',
           '2014/15-3',
           '2014/15-4',
           '2014/15-5',
           '2014/15-6',
           '2014/15-PRE',
           '2015-DRY',
           '2013/14-1',
           '2013/14-2',
           '2013/14-3',
           '2013/14-4',
           '2013/14-PRE',
           '2014-DRY',
           '2012/13-1',
           '2012/13-2',
           '2012/13-3',
           '2012/13-4',
           '2012/13-5',
           '2012/13-PRE',
           '2013-DRY',
           '2011/12-1',
           '2011/12-2',
           '2011/12-3',
           '2011/12-4',
           '2011/12-PRE',
           '2012-DRY',
           '2010/11-1',
           '2010/11-2',
           '2010/11-3',
           '2010/11-4',
           '2010/11-5',
           '2011-DRY']

EventID = ''
SiteID = ''
QAQCSampleType = ''
AnalysisDate = ''
Classification = ''
Constituent = ''
Fraction = ''
Sign = ''
Result = ''
Units = ''
Method = ''
MDL = ''
RL = ''

for name in datanames:
    with open(f'data/precsv/precsv{name}.txt', 'r') as file:
        precsv = file.read().replace(',', '||').split(sep='\n')
        inFData = True
        FLength = -1

        while inFData is True:
            FLength += 1
            if precsv[FLength].split(sep=' ')[0] not in fevents:
                inFData = False

        for i in range(FLength):
            splitprecsv = precsv[i].split(sep=' ')
            print(splitprecsv)
            EventID = splitprecsv[0]
            # print(f'EventID: {EventID}')
            SiteID = splitprecsv[1]
            # print(f'SiteID: {SiteID}')
            QAQCSampleType = splitprecsv[2]
            j = 3
            foundAnalysisDate = False
            foundAnalysisDateWhenJ = j
            while foundAnalysisDate is not True:
                if re.search(r'\d{1,2}/\d{1,2}/\d{4}', splitprecsv[j]) is not None:
                    AnalysisDate = splitprecsv[j]
                    # print(f'AnalysisDate: {AnalysisDate}')
                    foundAnalysisDateWhenJ = j
                    foundAnalysisDate = True
                if re.search(r'\d{1,2}/\d{1,2}/\d{4}', splitprecsv[j]) is None:
                    QAQCSampleType = QAQCSampleType + ' ' + splitprecsv[j]
                    j += 1
            # print(f'QAQCSampleType: {QAQCSampleType}')
            Classification = splitprecsv[foundAnalysisDateWhenJ + 1]
            # print(f'Classification: {Classification}')
            foundFraction = False
            Constituent = splitprecsv[foundAnalysisDateWhenJ + 2]
            k = foundAnalysisDateWhenJ + 3
            foundFractionWhenK = k
            while foundFraction is not True:
                if re.search(r'n/a', splitprecsv[k]) is not None or re.search(r'Total',
                                                                              splitprecsv[k]) is not None or re.search(
                        r'Dissolved', splitprecsv[k]) is not None:
                    Fraction = splitprecsv[k]
                    # print(f'Fraction: {Fraction}')
                    foundFractionWhenK = k
                    foundFraction = True
                if re.search(r'n/a', splitprecsv[k]) is None and re.search(r'Total',
                                                                           splitprecsv[k]) is None and re.search(
                        r'Dissolved', splitprecsv[k]) is None:
                    Constituent = Constituent + ' ' + splitprecsv[k]
                    k += 1
            # print(f'Constituent: {Constituent}')
            Sign = splitprecsv[foundFractionWhenK + 1]
            # print(f'Sign: {Sign}')
            Result = splitprecsv[foundFractionWhenK + 2]
            # print(f'Result: {Result}')
            Units = splitprecsv[foundFractionWhenK + 3]
            # print(f'Units: {Units}')
            Method = splitprecsv[foundFractionWhenK + 4] + ' ' + splitprecsv[foundFractionWhenK + 5]
            m = foundFractionWhenK + 5
            foundLastMethodWhenM = m
            if re.search(r'[a-zA-Z]', splitprecsv[m + 1]) is not None:
                Method = Method + ' ' + splitprecsv[m + 1]
                foundLastMethodWhenM += 1
            # print(f'Method: {Method}')
            MDL = splitprecsv[foundLastMethodWhenM + 1]
            # print(f'MDL: {MDL}')
            RL = splitprecsv[foundLastMethodWhenM + 2]
            # print(f'RL: {RL}')

            with open(f'data/{name}f.txt', 'a') as file2:
                file2.write(f'{EventID},'
                            f'{SiteID},'
                            f'{QAQCSampleType},'
                            f'{AnalysisDate},'
                            f'{Classification},'
                            f'{Constituent},'
                            f'{Fraction},'
                            f'{Sign},'
                            f'{Result},'
                            f'{Units},'
                            f'{Method},'
                            f'{MDL},'
                            f'{RL}\n')
            print(f'{EventID},'
                  f'{SiteID},'
                  f'{QAQCSampleType},'
                  f'{AnalysisDate},'
                  f'{Classification},'
                  f'{Constituent},'
                  f'{Fraction},'
                  f'{Sign},'
                  f'{Result},'
                  f'{Units},'
                  f'{Method},'
                  f'{MDL},'
                  f'{RL}\n')

# old = 'Below is the code that separated data from non-data.'
#
# garbagefg = open('data/precsv/garbagefg.txt', 'w')
# thingswhichneedutf8 = ['2019fg',
#                        '2018fg',
#                        '2017g',
#                        '2017f',
#                        '2016g',
#                        '2016f',
#                        '2015fg',
#                        '2014f',
#                        '2013fg',
#                        '2012g',
#                        '2012f',
#                        '2011fg']
#
# for k in thingswhichneedutf8:
#     with open(f'precsv{k}.txt', 'w', encoding='utf-8', errors='ignore') as datafile:
#         sepraw = open(f'data/correctlyencoded/{k}.txt', 'r', encoding='utf-8-sig', errors='ignore').read().replace('\uf076', '||||').replace('\uf0e0', '||||').replace('\u2070', '||||').replace('\u0d4c', '||||').replace('\u0d45', '||||').replace('\u0b3b', '||||').replace('ଶ଴ସି௣ு', '||||').replace('ுି', '||||').replace('ଶ଴ସ', '||||').replace('\u0be3', '||||').replace('\u05db', '||||').replace('\u123a', '||||').replace('\u2265', '||||').split(sep='\n')
#         # if k not in thingswhichneedutf8:
#         #     sepraw = open(f'data/raw/{k}.txt', 'r').read().split(sep='\n')
#         # if k in thingswhichneedutf8:
#         #     sepraw = open(f'data/raw/{k}.txt', 'r', encoding='utf-8').read().split(sep='\n')
#         for i in sepraw:
#             eventpresent = 0
#             for j in fevents:
#                 if re.search(f'{j}', i) is None:
#                     eventpresent += 1
#             if eventpresent == len(fevents):
#                 print(f'{i}\t\t{k}')
#                 garbagefg.write(f'{i}\n')
#             if eventpresent < len(fevents):
#                 datafile.write(f'{i}\n')
#
# garbagefg.close()
