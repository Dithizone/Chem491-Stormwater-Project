# This is a scratchpad for trying things out

datanames = ['2019fg',
             '2018fg',
             '2017g',
             '2017f',
             '2016g',
             '2016f',
             '2015fg',
             '2014f',
             '2013fg',
             '2012g',
             '2012f',
             '2011fg']

precsv2019fg = open('data/raw/2019fg.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2018fg = open('data/raw/2018fg.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2017g = open('data/raw/2017g.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2017f = open('data/raw/2017f.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2016g = open('data/raw/2016g.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2016f = open('data/raw/2016f.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2015fg = open('data/raw/2015fg.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2014f = open('data/raw/2014f.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2013fg = open('data/raw/2013fg.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2012g = open('data/raw/2012g.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2012f = open('data/raw/2012f.txt', 'r', encoding='utf-8', errors='ignore').read()
precsv2011fg = open('data/raw/2011fg.txt', 'r', encoding='utf-8', errors='ignore').read()

for i in datanames:
    with open(f'data/correctlyencoded/{i}.txt', 'w', encoding='utf-8', errors='ignore') as file:
        file.write(open(f'data/raw/{i}.txt', 'r', encoding='utf-8', errors='ignore').read())
