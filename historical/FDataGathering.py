# This one gathered all the F Data into data/{year}f.txt files.
# It has completed its job admirably.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from UsefulThings import datanames
from UsefulThings import fevents

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
            if re.search(r'Dissolved', splitprecsv[foundAnalysisDateWhenJ + 3]) is not None and re.search(r'Solids', splitprecsv[foundAnalysisDateWhenJ + 4]) is not None:
                Constituent = Constituent + ' ' + splitprecsv[foundAnalysisDateWhenJ + 3] + ' ' + splitprecsv[foundAnalysisDateWhenJ + 4]
                k = foundAnalysisDateWhenJ + 5
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
            if re.search(r'MPN/100', splitprecsv[foundFractionWhenK + 3]) is None:
                Units = splitprecsv[foundFractionWhenK + 3]
                # print(f'Units: {Units}')
                Method = splitprecsv[foundFractionWhenK + 4] + ' ' + splitprecsv[foundFractionWhenK + 5]
            if re.search(r'MPN/100', splitprecsv[foundFractionWhenK + 3]) is not None:
                Units = splitprecsv[foundFractionWhenK + 3] + ' ' + splitprecsv[foundFractionWhenK + 4]
                Method = splitprecsv[foundFractionWhenK + 5]
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

            with open(f'data/{name.replace("f", "").replace("g", "")}f.csv', 'a') as file2:
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
