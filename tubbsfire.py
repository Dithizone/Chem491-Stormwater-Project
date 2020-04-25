# This will figure out what's in the data/tubbsfire/ceden_data
# file and how useful it will be.

import pandas as pd
import matplotlib.pyplot as plt
from UsefulThings import NewData

tubbsdata = NewData('data/tubbsFire/ceden_data_20200417023345.txt', sep='|')

# analytes = tubbsdata.showuniques('Analyte')
columns = tubbsdata.columns
# units = tubbsdata.showuniques('Unit')

print(columns)
dates = tubbsdata.showuniques('SampleDate')  # 2018-02-14 to 2018-11-23, oh no
