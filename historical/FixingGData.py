# This will assemble all the individual G data csv files
# into a huge TheGData.csv. Little fixes will be done to create
# TheGData2.csv, and then the final, completed G data will be
# called TheGDataComplete.csv, just like with the F Data.
# Update (2020.4.3): Success!

import pandas as pd
from UsefulThings import printthegdetails
from UsefulThings import thegheaders

# -------------------------------------------------------------------------------
# This stuff below was to assemble all the G data together and write TheGData.csv
# -------------------------------------------------------------------------------

# df2012g = pd.read_csv('data/2012g.csv', names=thegheaders, index_col=None)
# df2013g = pd.read_csv('data/2013g.csv', names=thegheaders, index_col=None)
# df2015g = pd.read_csv('data/2015g.csv', names=thegheaders, index_col=None)
# df2016g = pd.read_csv('data/2016g.csv', names=thegheaders, index_col=None)
# df2017g = pd.read_csv('data/2017g.csv', names=thegheaders, index_col=None)
# df2018g = pd.read_csv('data/2018g.csv', names=thegheaders, index_col=None)
# df2019g = pd.read_csv('data/2019g.csv', names=thegheaders, index_col=None)
#
# listofDataFrames = [df2012g, df2013g, df2015g, df2016g, df2017g, df2018g, df2019g]
# dataFrameIndexCount = 0
# TheGData = df2012g.append(df2013g, ignore_index=True)\
#                   .append(df2015g, ignore_index=True)\
#                   .append(df2016g, ignore_index=True)\
#                   .append(df2017g, ignore_index=True)\
#                   .append(df2018g, ignore_index=True)\
#                   .append(df2019g, ignore_index=True)
#
# for dataframe in listofDataFrames:
#     dataFrameIndexCount += len(dataframe.index)
#     print(f"There are {len(dataframe.index)}")
#
# print(f'There are {len(TheGData.index)} entries in TheGData and {dataFrameIndexCount} in each individually.')
# TheGData.to_csv(path_or_buf='historical/TheGData.csv', index=False)

# ------------------------------------------------------
# Now we'll check uniques and fix stuff that looks weird
# ------------------------------------------------------

TheGData = open('TheGData.csv').read()\
    .replace('SCR,Down Down', 'SCR Down,PS-2015')\
    .replace('SCR,Up Up', 'SCR Up,PS-2015')\
    .replace('VR,Down Down', 'VR Down,PS-2015')\
    .replace('VR,Up Up', 'VR Up,PS-2015')\
    .replace('ng/g,dw,yrthrdGCMS-SIM,0.93,0.93 WKL', 'ng/g dw,GCMS-SIM,0.93,0.93,WKL')\
    .replace('ng/g,dw,yrthrdGCMS-SIM,0.94,0.94 WKL', 'ng/g dw,GCMS-SIM,0.94,0.94,WKL')\
    .replace('ng/g,dw,yrthrdGCMS-SIM,0.92,0.92 WKL', 'ng/g dw,GCMS-SIM,0.92,0.92,WKL')\
    .replace('ng/g,dw,yrthrdGCMS-SIM,0.82,0.82 WKL', 'ng/g dw,GCMS-SIM,0.82,0.82,WKL')\
    .replace('ng/g,dw,yrthrdGCMS-SIM,0.83,0.83 WKL', 'ng/g dw,GCMS-SIM,0.83,0.83,WKL')\
    .replace('mg/Kg,dw,EPA,9060.0,36 200 WKL', 'mg/kg dw,EPA 9060.0,36,200,WKL')\
    .replace('MPK,Upstream Upstream,Wet,10/5/2011', 'MPK Upstream,2011/12-1,Wet,10/5/2011')\
    .replace('MPK,Upstream Upstream,Wet,1/21/2012', 'MPK Upstream,2011/12-2,Wet,1/21/2012')\
    .replace('MPK,Upstream Upstream,Wet,11/1/2014', 'MPK Upstream,2014/15-1,Wet,11/1/2014') \
    .replace('MPK,Upstream Upstream,Wet,12/12/2014', 'MPK Upstream,2014/15-3,Wet,12/12/2014')\
    .replace('RC,pipe pipe at MPK,Wet,10/5/2011', 'Edison RC Pipe at MPK,2011/12-1,Wet,10/5/2011')\
    .replace('RC,pipe pipe at MPK,Wet,1/21/2012', 'Edison RC Pipe at MPK,2011/12-2,Wet,1/21/2011')\
    .replace('RC,Pipe Pipe at MPK,Wet,10/5/2011', 'Edison RC Pipe at MPK,2011/12-1,Wet,10/5/2011')\
    .replace('RC,Pipe Pipe at MPK,Wet,1/21/2012', 'Edison RC Pipe at MPK,2011/12-2,Wet,1/21/2011')\
    .replace('RC,pipe pipe at MPK,Wet,11/1/2014', 'Edison RC Pipe at MPK,2014/15-1,Wet,11/1/2014') \
    .replace('RC,pipe pipe at MPK,Wet,12/12/2014', 'Edison RC Pipe at MPK,2014/15-3,Wet,12/12/2014')\
    .replace('RC,Pipe Pipe at MPK,Wet,12/12/2014', 'Edison RC Pipe at MPK,2014/15-3,Wet,12/12/2014')

with open('TheGData2.csv', 'w') as file:
    file.write(TheGData)

TheGDataFrame = pd.read_csv('TheGData2.csv', index_col=None)
printthegdetails(TheGDataFrame)

# ------ Success!
# TheGDataFrame.to_csv(path_or_buf='data/TheGDataComplete.csv', index=False)
