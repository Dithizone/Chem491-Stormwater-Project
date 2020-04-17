# This takes data/prepivot/TheGDataComplete.csv and converts
# it into a smaller data set with dates as the index
# and constituents as the columns, with individual cells being the
# constituent concentrations in ng/L. Converting to
# mol/L would require the molar masses of over 200 complex
# organic molecules which, if necessary, can be collected
# from PubChem automatically using BeautifulSoup4 but we're
# on the clock.

import pandas as pd
import matplotlib.pyplot as plt
from UsefulThings import monitoringStations

unitstokeep = ['mg/L', 'µg/L', 'ng/L']

# It turns out I should've actually read a little about
# each data set because the F data is just QAQC stuff
# and not actually useful for our project... *crying emoji*
theGData = pd.read_csv('data/prepivot/TheGDataComplete.csv', parse_dates=['Sample Date', 'Analysis Date'])

ourGData_ng = theGData[theGData['Units'] == 'ng/L']

ourGData_mg = theGData[theGData['Units'] == 'mg/L']
ourGData_mg['Result'] = ourGData_mg['Result'] * 1000000  # Converts from mg/L to ng/L
ourGData_mg['Units'] = 'ng/L'  # Updates 'mg/L' label to 'ng/L'

ourGData_ug = theGData[theGData['Units'] == 'µg/L']
ourGData_ug['Result'] = ourGData_ug['Result'] * 1000  # Converts from ug/L to ng/L
ourGData_ug['Units'] = 'ng/L'  # Updates units label to ng/L

ourGData = ourGData_ng.append(ourGData_ug, ignore_index=True)\
    .append(ourGData_mg, ignore_index=True)  # Put all the data back together
print('Pandas disapproves of how I did unit conversions so it\'s giving a "SettingWithCopyWarning" error '
      'which this print command will now push out of the Run window.\n\n\n\n')


# Before pulling out monitoring stations, pivot table shape is (717, 201)
# Each station's new shape is about (50, 200), which is an intriguingly
# small number of dates.

for station in monitoringStations:
    dfForStation = ourGData[ourGData['Site ID'] == station]
    pivotStation = pd.pivot_table(dfForStation, values='Result', index='Sample Date', columns='Constituent')
    print(f'At {station}, the data has shape {dfForStation.shape}. After pivot: {pivotStation.shape}')
    pivotStation.to_csv(path_or_buf=f'data/{station}.csv')

# And now we have the data!
