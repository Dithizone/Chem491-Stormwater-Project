# This will figure out what's in the data/tubbsfire/Sonoma County Data 16-19.txt
# file and how useful it will be.

# Fire data for Tubbs and others can be found at https://rmgsc.cr.usgs.gov/outgoing/GeoMAC/
# Fires in data/shapefiles were chosen by cross-referencing fires with
# those from Ventura county according to e.g. https://en.wikipedia.org/wiki/2017_California_wildfires

import pandas as pd
import matplotlib.pyplot as plt
from UsefulThings import NewData, constituentsWeWant, tubbsConstituentsWeWant

tubbsdata = pd.read_csv('data/tubbsFire/Sonoma County Data 16-19.txt', sep='|', dtype={'Result': float})
# Wow so, one of the entries for Total Dissolved Solids had a Result value
# of .289.6 which Pandas treated as a string in the middle of a whole
# column of floats which made memory usage HUGE. So large, in fact, that
# PyCharm would lock up as it began processing the g/L sections and end
# with a memory error. I tried erasing previous dataframes mid-script to
# free memory (if that even works?) but once I found that typo and fixed
# it, everything runs amazingly fast.

for i in tubbsdata.columns.values:
    print(f'{i}\t\tUniques: {len(tubbsdata[i].unique())}\t\tCount: {tubbsdata[i].count()}')

print(f'\n------- Units -------')
print(tubbsdata['Unit'].unique())
print(f'tubbsdata shape is {tubbsdata.shape}')

# Pulling out just ng/L, ug/L, mg/L, and g/L
tubbsdata_ng = tubbsdata[tubbsdata['Unit'] == 'ng/L']

tubbsdata_ug = tubbsdata[tubbsdata['Unit'] == 'ug/L']
tubbsdata_ug['Result'] = tubbsdata_ug['Result'] * 1000  # Converts from ug/L to ng/L
tubbsdata_ug['Unit'] = 'ng/L'  # Updates units label to ng/L

tubbsdata_mg = tubbsdata[tubbsdata['Unit'] == 'mg/L']
tubbsdata_mg['Result'] = tubbsdata_mg['Result'] * 1000000  # Converts from mg/L to ng/L
tubbsdata_mg['Unit'] = 'ng/L'

tubbsdata_g = tubbsdata[tubbsdata['Unit'] == 'g/L']
tubbsdata_g['Result'] = tubbsdata_g['Result'] * 1000000000  # Converts from g/L to ng/L
tubbsdata_g['Unit'] = 'ng/L'

TheTubbsData = tubbsdata_ng.append(tubbsdata_ug, ignore_index=True)\
    .append(tubbsdata_mg, ignore_index=True)\
    .append(tubbsdata_g, ignore_index=True)  # Put all the data back together

print('Pandas disapproves of how I did unit conversions so it\'s giving a "SettingWithCopyWarning" error '
      'which this print command will now push out of the Run window.\n\n\n\n')

print(f'TheTubbsData shape is {TheTubbsData.shape}')

print(f'\n------- StationNames ({len(TheTubbsData["StationName"].unique())}) -------')
# Station "Piner Creek at Marlow Rd" is the one in Google Earth
for j in TheTubbsData['StationName'].unique():
    print(j)

print(f'\n------- StationCode ({len(TheTubbsData["StationCode"].unique())}) -------')
# Station 114PI5786 is the one in Google Earth
for k in TheTubbsData["StationCode"].unique():
    print(k)

stationsfortubbsfire = ['114PI5786', '114PR1182', '114UL0366', '114MW6173', '114PL8130']

for station in stationsfortubbsfire:
    dfForStation = TheTubbsData[TheTubbsData['StationCode'] == '114PI5786']
    pivotStation = pd.pivot_table(dfForStation, values='Result', index='SampleDate', columns='Analyte')
    wantedConstituentsFromStation = pivotStation[tubbsConstituentsWeWant]
    print(f'At {station}, the data has shape {dfForStation.shape}. After pivot: {pivotStation.shape}. After selection: {wantedConstituentsFromStation.shape}')
    pivotStation.to_csv(path_or_buf=f'data/tubbsfire/{station}.csv')

# Now we have the data... though it's (4, 16) so I'm not sure how useful it'll be.

# ---------------------------------
# ------- Now, the rainfall -------
# ---------------------------------
# from https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00023213/detail

santarosarainfall = pd.read_csv('data/tubbsFire/santarosarainfall.csv')
print(santarosarainfall)
