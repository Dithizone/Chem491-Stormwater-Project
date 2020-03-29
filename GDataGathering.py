# This will craft the G data .csv files.

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

datanamestest = ['2019fg']

for name in datanamestest:
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
                # TODO Figure out how I want to grab the dates
                print(f'{SiteID}, {Event}, {EventType}\n')


