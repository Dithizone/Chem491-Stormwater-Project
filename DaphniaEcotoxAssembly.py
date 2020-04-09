# This will check that we've gotten all the Daphnia data from Ecotox,
# erase duplicates, remove undesired columns, select specific data,
# and save the smaller subset as its own file.

# It may be best to redownload after considering what columns we *do*
# want rather than just grabbing all of them...

import pandas as pd

aquaticReport1 = pd.read_csv('data/ecotox/AquaticReport1.txt', sep='|', index_col=False, low_memory=False)
aquaticReport2 = pd.read_csv('data/ecotox/AquaticReport2.txt', sep='|', index_col=False, low_memory=False)
aquaticReport3 = pd.read_csv('data/ecotox/AquaticReport3.txt', sep='|', index_col=False, low_memory=False)
aquaticReport4 = pd.read_csv('data/ecotox/AquaticReport4.txt', sep='|', index_col=False, low_memory=False)

daphniaEcotoxData = aquaticReport1.append(aquaticReport2, ignore_index=True)\
                                  .append(aquaticReport3, ignore_index=True)\
                                  .append(aquaticReport4, ignore_index=True)\
                                  .drop_duplicates()

print(daphniaEcotoxData)
