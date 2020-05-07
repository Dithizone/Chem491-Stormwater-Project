# This is a scratchpad for trying things out.
# Most recently (2020.05.07), this is double-checking that
# all the constituents we want are in the pivoted data.

import pandas as pd
from UsefulThings import constituentsWeWant
from tubbsfire import TheTubbsData
import re

MOVEN = pd.read_csv('data/fullpivotstations/MO-VEN.csv')

for j in MOVEN.columns.values:
    if j not in constituentsWeWant:
        print(f"'{j}',")

# for i in constituentsWeWant:
#     if i not in MOVEN.columns.values:
#         print(i)
