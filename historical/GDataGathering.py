# This will craft the G data .csv files.
# Update (2020.4.2), it did its job wonderfully!

import re
from UsefulThings import fevents
from UsefulThings import datanames

# The column values in the G data

SiteID = ''
Event = ''
EventType = ''
SampleDate = ''
AnalysisDate = ''
Constituent = ''
Fraction = ''
Sign = ''
Result = ''
Units = ''
Method = ''
MDL = ''
ReportingLimit = ''
AnalyzingLaboratory = ''
Qualifier = ''

datanameswithout2011 = ['2019fg',
                        '2018fg',
                        '2017g',
                        '2017f',
                        '2016g',
                        '2016f',
                        '2015fg',
                        '2014f',
                        '2013fg',
                        '2012g',
                        '2012f']
listofuniques = []

for name in datanameswithout2011:
    with open(file=f'data/precsv/precsv{name}.txt', mode='r') as file:
        precsv = file.read().replace(',', '||').split(sep='\n')  # Turns every line into an entry in 'precsv' list
        for i in range(len(precsv)):
            splitprecsv = precsv[i].split(sep=' ')  # Chops up each entry in 'precsv' list by space separation
            if splitprecsv[0] not in fevents and splitprecsv[0] != "":  # Now we're looking at a line of G data
                foundWetorDry = False
                wordnumber = 0
                print(splitprecsv)
                while foundWetorDry is False:  # Finds which word in the entry is "Wet" or "Dry"
                    if re.search('Wet', splitprecsv[wordnumber]) is not None or re.search('Dry', splitprecsv[wordnumber]) is not None:
                        foundWetorDry = True
                        wordnumber -= 1
                    wordnumber += 1
                foundWetDryAtWordNumber = wordnumber
                SiteID = splitprecsv[0]
                Event = splitprecsv[1]
                for j in range(foundWetDryAtWordNumber - 2):  # Creates Event as everything between Wet/Dry and word 0
                    Event = Event + ' ' + splitprecsv[1 + j]
                EventType = splitprecsv[foundWetDryAtWordNumber]
                SampleDate = splitprecsv[foundWetDryAtWordNumber + 1]
                foundAnalysisDate = False
                analysisDateStart = foundWetDryAtWordNumber + 2
                while foundAnalysisDate is False:  # Checking ahead to see if times and AM/PM are present in sample dates
                    if re.search(r'\d{1,2}/\d{1,2}/\d{4}', splitprecsv[analysisDateStart]) is None:
                        SampleDate = SampleDate + ' ' + splitprecsv[analysisDateStart]
                        analysisDateStart = analysisDateStart + 1
                    if re.search(r'\d{1,2}/\d{1,2}/\d{4}', splitprecsv[analysisDateStart]) is not None:
                        foundAnalysisDate = True
                AnalysisDate = splitprecsv[analysisDateStart]
                ConstituentStart = analysisDateStart + 1
                if re.search(r'\d:\d{2}:\d{2}', splitprecsv[ConstituentStart]) is not None:  # Checking ahead for times/AM/PM in analysis dates
                    AnalysisDate = AnalysisDate + ' ' + splitprecsv[ConstituentStart]
                    ConstituentStart += 1
                    if splitprecsv[ConstituentStart] == 'AM' or splitprecsv[ConstituentStart] == 'PM':
                        AnalysisDate = AnalysisDate + ' ' + splitprecsv[ConstituentStart]
                        ConstituentStart += 1
                Constituent = splitprecsv[ConstituentStart]
                SignStart = ConstituentStart + 1
                foundSign = False
                while foundSign is False:  # Finds Sign and creates Fraction as entry before '<,' '>,' '=,' or 'DNQ' or f@#$ing '*'
                    SignStart += 1
                    if re.search('<', splitprecsv[SignStart]) is not None or re.search('>', splitprecsv[SignStart]) is not None or re.search('DNQ', splitprecsv[SignStart]) is not None or re.search('=', splitprecsv[SignStart]) is not None or re.search('\\*', splitprecsv[SignStart]) is not None:
                        foundSign = True
                for k in range((SignStart - 1) - ConstituentStart - 1):
                    Constituent = Constituent + ' ' + splitprecsv[ConstituentStart + k + 1]
                Fraction = splitprecsv[SignStart - 1]
                Sign = splitprecsv[SignStart]
                Result = splitprecsv[SignStart + 1]
                UnitsEnd = SignStart + 2
                Units = splitprecsv[UnitsEnd]
                if re.search('MPN/100', splitprecsv[UnitsEnd]) is not None:  # Doing some band-aid fixes for weird units
                    UnitsEnd += 1
                    Units = Units + ' ' + splitprecsv[UnitsEnd]
                if re.search('pH', splitprecsv[UnitsEnd]) is not None:
                    UnitsEnd += 1
                    Units = Units + ' ' + splitprecsv[UnitsEnd]
                MethodStart = UnitsEnd + 1
                Method = splitprecsv[MethodStart]
                if re.search('Field', splitprecsv[MethodStart]):  # Band-aid fixes for Methods
                    MethodStart += 1
                    Method = Method + ' ' + splitprecsv[MethodStart]
                if re.search('SM', splitprecsv[MethodStart]):
                    MethodStart += 1
                    Method = Method + ' ' + splitprecsv[MethodStart]
                    MethodStart += 1
                    Method = Method + ' ' + splitprecsv[MethodStart]
                if re.search('ASTM', splitprecsv[MethodStart]):
                    MethodStart += 1
                    Method = Method + ' ' + splitprecsv[MethodStart]
                if re.search('LUFT', splitprecsv[MethodStart]):
                    MethodStart += 1
                    Method = Method + ' ' + splitprecsv[MethodStart]
                if re.search('EPA', splitprecsv[MethodStart]):
                    MethodStart += 1
                    Method = Method + ' ' + splitprecsv[MethodStart]
                MDLStart = MethodStart + 1
                MDL = splitprecsv[MDLStart]
                ReportingLimit = splitprecsv[MDLStart + 1]
                AnalyzingLaboratoryStart = MDLStart + 2
                AnalyzingLaboratory = splitprecsv[AnalyzingLaboratoryStart]
                # Band-aids so later I can edit whatever error is causing AnalyzingLaboratory to be a number
                # (It's probably one of the PDFs switching to EPA methods in a new format)
                if re.search('36', splitprecsv[AnalyzingLaboratoryStart]) is not None:
                    AnalyzingLaboratory = AnalyzingLaboratory + ' ' + splitprecsv[AnalyzingLaboratoryStart + 1] + ' ' + splitprecsv[AnalyzingLaboratoryStart + 2]
                if re.search('0.9', splitprecsv[AnalyzingLaboratoryStart]) is not None:
                    AnalyzingLaboratory = AnalyzingLaboratory + ' ' + splitprecsv[AnalyzingLaboratoryStart + 1]
                if re.search('0.8', splitprecsv[AnalyzingLaboratoryStart]) is not None:
                    AnalyzingLaboratory = AnalyzingLaboratory + ' ' + splitprecsv[AnalyzingLaboratoryStart + 1]
                if re.search('WKLEST', splitprecsv[AnalyzingLaboratoryStart]) is not None:
                    AnalyzingLaboratory = 'WKL'

                # if AnalyzingLaboratory not in listofuniques:
                #     listofuniques.append(AnalyzingLaboratory)
                # with open(f'data/{name.replace("f", "").replace("g", "")}g.csv', 'a') as file2:
                #     file2.write(f'{SiteID},'
                #                 f'{Event},'
                #                 f'{EventType},'
                #                 f'{SampleDate},'
                #                 f'{AnalysisDate},'
                #                 f'{Constituent},'
                #                 f'{Fraction},'
                #                 f'{Sign},'
                #                 f'{Result},'
                #                 f'{Units},'
                #                 f'{Method},'
                #                 f'{MDL},'
                #                 f'{ReportingLimit},'
                #                 f'{AnalyzingLaboratory}\n')
                print(f'{SiteID},'
                      f'{Event},'
                      f'{EventType},'
                      f'{SampleDate},'
                      f'{AnalysisDate},'
                      f'{Constituent},'
                      f'{Fraction},'
                      f'{Sign},'
                      f'{Result},'
                      f'{Units},'
                      f'{Method},'
                      f'{MDL},'
                      f'{ReportingLimit},'
                      f'{AnalyzingLaboratory}\n')

# for q in listofuniques:
#     print(q)
