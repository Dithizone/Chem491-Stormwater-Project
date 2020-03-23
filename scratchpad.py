# This is a scratchpad for trying things out.

from UsefulThings import datanames
from UsefulThings import fevents

thingsinfirstcolumn = []

for name in datanames:
    with open(f'data/precsv/precsv{name}.txt', 'r') as file:
        precsv = file.read().replace(',', '||').split(sep='\n')
        for line in precsv:
            if line.split(sep=" ")[0] not in thingsinfirstcolumn:
                thingsinfirstcolumn.append(line.split(sep=" ")[0])

for i in thingsinfirstcolumn:
    if i not in fevents:
        print(f'\'{i}\',')  # Thanks Python!
