# This separates the data-relevant lines from data-irrelevant
# (or "garbage") lines. It has accomplished its task admirably.

import re
from UsefulThings import fevents
from UsefulThings import datanames

garbagefg = open('../data/precsv/garbagefg.txt', 'w')
for k in datanames:
    with open(f'data/precsv/precsv{k}.txt', 'w', encoding='utf-8', errors='ignore') as datafile:
        sepraw = open(f'data/raw/{k}.txt', 'r', encoding='utf-8-sig', errors='ignore').read().replace('\uf076', '||||').replace('\uf0e0', '||||').replace('\u2070', '||||').replace('\u0d4c', '||||').replace('\u0d45', '||||').replace('\u0b3b', '||||').replace('ଶ଴ସି௣ு', '||||').replace('ுି', '||||').replace('ଶ଴ସ', '||||').replace('\u0be3', '||||').replace('\u05db', '||||').replace('\u123a', '||||').replace('\u2265', '||||').split(sep='\n')
        for i in sepraw:
            eventpresent = 0
            for j in fevents:
                if re.search(f'{j}', i) is None:
                    eventpresent += 1
            if eventpresent == len(fevents):
                print(f'{i}\t\t{k}')
                garbagefg.write(f'{i}\n')
            if eventpresent < len(fevents):
                datafile.write(f'{i}\n')

garbagefg.close()
