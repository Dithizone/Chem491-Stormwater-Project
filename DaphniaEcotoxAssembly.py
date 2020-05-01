# This will explore the ECOTOX data Frankie gathered, found
# in data/ecotox/aquatic report; Daphnia Magna.csv

import pandas as pd
import matplotlib.pyplot as plt
from UsefulThings import NewData

columnsIwant = ['Test Number',
                'CAS Number',
                'Chemical Name',
                'Test Method',
                'Species Scientific Name',
                'Organism Lifestage',
                'Organism Age Mean',
                'Organism Age Min',
                'Organism Age Max',
                'Age Units',
                'Exposure Type',
                'Media Type',
                'Test Location',
                'Number of Doses',
                'Conc 1 Type (Standardized)',
                'Conc 1 Mean (Standardized)',
                'Conc 1 Min (Standardized)',
                'Conc 1 Max (Standardized)',
                'Conc 1 Units (Standardized)',
                'Effect',
                'Effect Measurement',
                'Endpoint',
                'Observed Duration Mean (Days)',
                'Observed Duration Min (Days)',
                'Observed Duration Max (Days)',
                'Observed Duration Units (Days)',
                'Test Type',
                'Temperature Mean',
                'Temperature Min',
                'Temperature Max',
                'Temperature Units',
                'Hardness Mean',
                'Hardness Min',
                'Hardness Max',
                'Hardness Units',
                'pH Mean',
                'pH Min',
                'pH Max',
                'Author',
                'Title',
                'Publication Year']

ecotoxdata = pd.read_csv('data/ecotox/2020.4.30DaphniaAquaticReport.txt', sep='|')
for i in ecotoxdata.columns.values:  # Shows unique entries and total entries (i.e. are there holes?)
    print(f'{i}\t\tUniques: {len(ecotoxdata[i].unique())}\t\tCount: {ecotoxdata[i].count()}')

print('\n------- The dataframe (hopefully) ------- ')
ecotoxdataframe = ecotoxdata[columnsIwant]

# Selecting for just data on Neonates
ecotoxdataframe = ecotoxdataframe[ecotoxdataframe['Organism Lifestage'] == 'Neonate']\
    .sort_values(by='Chemical Name', ascending=False).reset_index()
print(ecotoxdataframe.shape)  # (1007, 41)
ecotoxdataframe.to_csv(path_or_buf='data/ecotox/DaphniaECOTOX.csv')
