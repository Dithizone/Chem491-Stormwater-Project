# This will explore the ECOTOX data Frankie gathered, found
# in data/ecotox/aquatic report; Daphnia Magna.csv

import pandas as pd
import matplotlib.pyplot as plt
from UsefulThings import NewData

ecotoxdata = NewData(filepath='data/ecotox/aquatic report; Daphnia Magna.csv')
print(ecotoxdata.showuniques('Endpoint'))  # Shows 'None' as an endpoint?

# (My cool NewData class has limitations)
ecotox = pd.read_csv(filepath_or_buffer='data/ecotox/aquatic report; Daphnia Magna.csv')
weirdendpoint = ecotox[ecotox['Endpoint'] != 'LC50']
weirdendpoint2 = weirdendpoint[weirdendpoint['Endpoint'] != 'EC50']
weirdendpoint3 = weirdendpoint2[weirdendpoint2['Endpoint'] != 'LC50*']
weirdendpoint4 = weirdendpoint3[weirdendpoint3['Endpoint'] != 'EC50*']

print(weirdendpoint3['Endpoint'])  # Doesn't show 'None' as an endpoint
