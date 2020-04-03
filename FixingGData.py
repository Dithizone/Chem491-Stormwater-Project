# This will assemble all the individual G data csv files
# into a huge TheGData.csv. Little fixes will be done to create
# TheGData2.csv, and then the final, completed G data will be
# called TheGDataComplete.csv, just like with the F Data.

import pandas as pd
from UsefulThings import printthedetails
from UsefulThings import thegheaders

df2012g = pd.read_csv('data/2012g.csv', names=thegheaders, index_col=None)
df2013g = pd.read_csv('data/2013g.csv', names=thegheaders, index_col=None)
df2015g = pd.read_csv('data/2015g.csv', names=thegheaders, index_col=None)
df2016g = pd.read_csv('data/2016g.csv', names=thegheaders, index_col=None)
df2017g = pd.read_csv('data/2017g.csv', names=thegheaders, index_col=None)
df2018g = pd.read_csv('data/2018g.csv', names=thegheaders, index_col=None)
df2019g = pd.read_csv('data/2019g.csv', names=thegheaders, index_col=None)

