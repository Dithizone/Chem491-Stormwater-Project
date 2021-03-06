# This is a collection of useful functions, lists, and such
# so they don't clutter up other working files!

# See if I can load DataFrames here, create a list of
# DataFrames here, and just import them as a list to unclutter
# other scripts/notebooks. TODO: Try this DataFrame loading idea.

import matplotlib.pyplot as plt
import pandas as pd

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

fevents = ['2018/19-1',
           '2018/19-2',
           '2018/19-3',
           '2018/19-4',
           '2018/19-5',
           '2018/19-PRE',
           '2019-DRY',
           '2017/18-1',
           '2017/18-2',
           '2017/18-3',
           '2017/18-4',
           '2017/18-5',
           '2017/18-PRE',
           '2018-DRY',
           '2016/17-1',
           '2016/17-2',
           '2016/17-3',
           '2016/17-4',
           '2016/17-5',
           '2016/17-6',
           '2016/17-PRE',
           '2016/17-PREBlankwater-ultrapure',
           '2017-DRY',
           '2015/16-1',
           '2015/16-2',
           '2015/16-3',
           '2015/16-4',
           '2015/16-5',
           '2015/16-PRE',
           '2016-DRY',
           '2014/15-1',
           '2014/15-2',
           '2014/15-3',
           '2014/15-4',
           '2014/15-5',
           '2014/15-6',
           '2014/15-PRE',
           '2014/15-PRE2',
           '2015-DRY',
           '2013/14-1',
           '2013/14-2',
           '2013/14-3',
           '2013/14-4',
           '2013/14-PRE',
           '2014-DRY',
           '2012/13-1',
           '2012/13-2',
           '2012/13-3',
           '2012/13-4',
           '2012/13-5',
           '2012/13-PRE',
           '2012/13-PRETubing',
           '2012/13-PRE2',
           '2012/13-PRE2Tubing',
           '2013-DRY',
           '2011/12-1',
           '2011/12-2',
           '2011/12-3',
           '2011/12-4',
           '2011/12-PRE',
           '2011/12-PRE2',
           '2011/12-PRE2Arrowhead',
           '2012-DRY',
           '2010/11-1',
           '2010/11-2',
           '2010/11-3',
           '2010/11-4',
           '2010/11-5',
           '2011-DRY']

feventproblemchildren = ['2016/17-PREBlankwater-ultrapure',
                         '2012/13-PRETubing',
                         '2012/13-PRE2Tubing',
                         '2011/12-PRE2Arrowhead', ]

gsites = ['DRY-HUE3',
          'DRY-MPK2',
          'DRY-OJA6',
          'DRY-OXN2',
          'DRY-SPA3',
          'DRY-UNI4',
          'DRY-VEN5',
          'ME-CC',
          'ME-SCR',
          'ME-VR2',
          'MO-CAM',
          'MO-FIL',
          'MO-HUE',
          'MO-MEI',
          'MO-MPK',
          'MO-OJA',
          'MO-OXN',
          'MO-SIM',
          'MO-SPA',
          'MO-THO',
          'MO-VEN',
          'DRY-SPA4',
          'DRY-CAM4',
          'DRY-UNI2',
          'CCWR07-02',
          'DRY-SPA2',
          'RC',
          'MPK',
          'SCR',
          'VR',
          'Edison']
monitoringStations = ['MO-CAM',
                      'MO-FIL',
                      'MO-HUE',
                      'MO-MEI',
                      'MO-MPK',
                      'MO-OJA',
                      'MO-OXN',
                      'MO-SIM',
                      'MO-SPA',
                      'MO-THO',
                      'MO-VEN',
                      'ME-CC',
                      'ME-SCR',
                      'ME-VR2']
stationIDsAndSelectedRainfallStation = {'Website to find locations': 'https://www.vcwatershed.net/fws/gmap.html',
                                        'MO-CAM': 'H259 Camarillo-PVWD (a bit south)',
                                        'MO-FIL': 'H199A (South side of Fillmore by Santa Clara river)',
                                        'MO-HUE': '017C Port Hueneme - Oxnard Sewer Plant (nearby)',
                                        'MO-MEI': 'H218 (adjacent)',
                                        'MO-MPK': 'H508 (Southwest in Moorpark)',
                                        'MO-OJA': 'H030D (adjacent)',
                                        'MO-OXN': 'H239 El Rio spreading ground (MO-OXN isn\'t on map but this seems close)',
                                        'MO-SIM': 'H506 (Just east of the Reagan Library)',
                                        'MO-SPA': 'H245A (North side of Santa Paula), except for 2010 which is H245B',
                                        'MO-THO': 'H188 (In Newbury Park... but that\'s where THO seems to be in the image)',
                                        'MO-VEN': 'H175A Saticoy-County Yard (upstream a ways from MO-VEN, but along Santa Clara river)',
                                        'ME-CC': 'H505 (Right by CSUCI, incidentally)',
                                        'ME-SCR': 'Use H175A just like MO-VEN (positioned in between MO-VEN and ME-SCR along Santa Clara river)',
                                        'ME-VR2': 'H122, Ventura-Kingston Reservoir (Right next to ME-VR2)'}
monitoringStationCoords = {'Station': ['Latitude', 'Longitude'],
                           'MO-CAM': [34.219492, -119.066173],
                           'MO-FIL': [34.405355, -118.929577],
                           'MO-HUE': [34.140853, -119.187986],
                           'MO-MEI': [34.443184, -119.278031],
                           'MO-MPK': [34.279133, -118.905403],
                           'MO-OJA': [34.444788, -119.241287],
                           'MO-OXN': [34.236975, -119.184792],
                           'MO-SIM': [34.271909, -118.781102],
                           'MO-SPA': [34.358091, -119.049187],
                           'MO-THO': [34.213262, -118.921535],
                           'MO-VEN': [34.245438, -119.19175],
                           'ME-CC': [34.179189, -119.039648],
                           'ME-SCR': [34.301172, -119.110343],
                           'ME-VR2': [34.344223, -119.299081]}

theheaders = ['Event ID',
              'Site ID',
              'QAQC Sample Type',
              'Analysis Date',
              'Classification',
              'Constituent',
              'Fraction',
              'Sign',
              'Result',
              'Units',
              'Method',
              'MDL',
              'RL']

thegheaders = ["Site ID",
               "Event",
               "Event Type",
               "Sample Date",
               "Analysis Date",
               "Constituent",
               "Fraction",
               "Sign",
               "Result",
               "Units",
               "Method",
               "MDL",
               "Reporting Limit",
               "Analyzing Laboratory"]

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

constituentsWeWant = ['Acenaphthene',
                      'Acenaphthylene',
                      'Aluminum',
                      'Anthracene',
                      'Arsenic',
                      'Benz(a)anthracene',
                      'Benzo(a)pyrene',
                      'Benzo(b)fluoranthene',
                      'Benzo(g||h||i)perylene',
                      'Benzo(k)fluoranthene',
                      'Cadmium',
                      'Calcium',
                      'Chrysene',
                      'Copper',
                      'Dibenz(a||h)anthracene',
                      'Fluoranthene',
                      'Fluorene',
                      'Indeno(1||2||3-cd)pyrene',
                      'Iron',
                      'Lead',
                      'Magnesium',
                      'Mercury',
                      'Naphthalene',
                      'Nickel',
                      'Phenanthrene',
                      'Potassium',
                      'Pyrene',
                      'Sodium',
                      'Zinc']
thePAHs = ['Acenaphthene',
           'Acenaphthylene',
           'Anthracene',
           'Benz(a)anthracene',
           'Benzo(a)pyrene',
           'Benzo(b)fluoranthene',
           'Benzo(g||h||i)perylene',
           'Benzo(k)fluoranthene',
           'Chrysene',
           'Dibenz(a||h)anthracene',
           'Fluoranthene',
           'Fluorene',
           'Indeno(1||2||3-cd)pyrene',
           'Naphthalene',
           'Phenanthrene',
           'Pyrene']
theToxicPAHs = ['Benz(a)anthracene',
                'Benzo(a)pyrene',
                'Benzo(b)fluoranthene',
                'Benzo(k)fluoranthene',
                'Dibenz(a||h)anthracene',
                'Indeno(1||2||3-cd)pyrene']
theMetals = ['Aluminum',
             'Arsenic',
             'Cadmium',
             'Calcium',
             'Copper',
             'Iron',
             'Lead',
             'Magnesium',
             'Mercury',
             'Nickel',
             'Potassium',
             'Sodium',
             'Zinc']
subsetOfTheMetals = ['Cadmium',
                     'Copper',
                     'Lead',
                     'Mercury',
                     'Nickel',
                     'Zinc']
tubbsConstituentsWeWant = ['Aluminum, Dissolved',
                           'Arsenic, Dissolved',
                           'Benzo(b)fluoranthene, Total',
                           'Benzo(g,h,i)perylene, Total',
                           'Cadmium, Dissolved',
                           'Calcium, Total',
                           'Copper, Total',
                           'Fluoranthene, Total',
                           'Iron, Dissolved',
                           'Lead, Dissolved',
                           'Magnesium, Total',
                           'Mercury, Dissolved',
                           'Mercury, Methyl, Total',
                           'Nickel, Dissolved',
                           'Pyrene, Total',
                           'Zinc, Dissolved']

# Dataframes
MO_CAM = pd.read_csv('data/MO-CAMmetals-PAHs.csv', index_col='Sample Date')
MO_FIL = pd.read_csv('data/MO-FILmetals-PAHs.csv', index_col='Sample Date')
MO_HUE = pd.read_csv('data/MO-HUEmetals-PAHs.csv', index_col='Sample Date')
MO_MEI = pd.read_csv('data/MO-MEImetals-PAHs.csv', index_col='Sample Date')
MO_MPK = pd.read_csv('data/MO-MPKmetals-PAHs.csv', index_col='Sample Date')
MO_OJA = pd.read_csv('data/MO-OJAmetals-PAHs.csv', index_col='Sample Date')
MO_OXN = pd.read_csv('data/MO-OXNmetals-PAHs.csv', index_col='Sample Date')
MO_SIM = pd.read_csv('data/MO-SIMmetals-PAHs.csv', index_col='Sample Date')
MO_SPA = pd.read_csv('data/MO-SPAmetals-PAHs.csv', index_col='Sample Date')
MO_THO = pd.read_csv('data/MO-THOmetals-PAHs.csv', index_col='Sample Date')
MO_VEN = pd.read_csv('data/MO-VENmetals-PAHs.csv', index_col='Sample Date')
ME_CC = pd.read_csv('data/ME-CCmetals-PAHs.csv', index_col='Sample Date')
ME_SCR = pd.read_csv('data/ME-SCRmetals-PAHs.csv', index_col='Sample Date')
ME_VR2 = pd.read_csv('data/ME-VR2metals-PAHs.csv', index_col='Sample Date')

allTheDataFrames = [MO_CAM,
                    MO_FIL,
                    MO_HUE,
                    MO_MEI,
                    MO_MPK,
                    MO_OJA,
                    MO_OXN,
                    MO_SIM,
                    MO_SPA,
                    MO_THO,
                    MO_VEN,
                    ME_CC,
                    ME_SCR,
                    ME_VR2]


def printthedetails(dataframe):
    """This prints all the unique values for columns 0 through 10 for the chosen dataframe."""
    for m in [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]:
        print(f'{theheaders[m]} ({m}):')
        for n in dataframe.iloc[:, m].unique():
            if m == 2 or m == 5:
                print(f'- {n.replace("||", ",")}')
            if m != 2 and m != 5:
                print(f'\t{n}')
        print('\n')


def printthegdetails(dataframe):
    """This prints all the unique values for columns specific to the G data from the chosen dataframe."""
    for p in [0, 1, 2, 5, 6, 7, 9, 10, 11, 13]:
        print(f'\n{thegheaders[p]} ({p}):')
        for q in dataframe.iloc[:, p].unique():
            print(f'\t{q}')


def linePlotTheThing(dataframetoplot,
                     columntoplot,
                     title=None,
                     titlefontsize=15,
                     xaxislabel=None,
                     yaxislabel=None,
                     color='xkcd:cerulean blue',
                     islogscale=False,
                     figuredimensions=(8, 6),
                     filepathtosavepng=None,
                     legend=False,
                     showplot=True):
    dataframetoplot.plot(kind='line',
                         y=columntoplot,
                         color=color,
                         figsize=figuredimensions,
                         logy=islogscale,
                         legend=legend)
    plt.xlabel(xlabel=xaxislabel)
    plt.ylabel(ylabel=yaxislabel)
    plt.title(label=title, fontsize=titlefontsize)
    if filepathtosavepng is not None:
        plt.savefig(fname=filepathtosavepng,
                    bbox_inches='tight',
                    orientation="landscape",
                    pad_inches=0.2,
                    dpi=600)
    if showplot is True:
        return plt.show()


def saveThisGraph(filepathtosavepng):
    plt.savefig(fname=filepathtosavepng, bbox_inches='tight', orientation="landscape", pad_inches=0.2, dpi=600)
    return print('Graph saved!')


def linePlotAllTheThings(dataframetoplot,
                         columnstoplot,
                         title=None,
                         titlefontsize=15,
                         xaxislabel=None,
                         yaxislabel=None,
                         figuredimensions=(8, 6),
                         filepathtosavepng=None,
                         showplot=True):
    plt.figure(figsize=figuredimensions)
    for k in columnstoplot:
        plt.plot(dataframetoplot.loc[:, k], label=f'{k}')
    plt.title(label=title, fontsize=titlefontsize)
    plt.legend()
    plt.xlabel(xaxislabel)
    plt.ylabel(yaxislabel)
    if filepathtosavepng is not None:
        saveThisGraph(filepathtosavepng)
    if showplot is True:
        return plt.show()


class NewData:
    def __init__(self, filepath, sep=','):
        self.datalocation = filepath
        data = pd.read_csv(filepath_or_buffer=filepath, sep=sep)
        self.columns = data.columns.values
        self.data = data

    def showuniques(self, column):
        for i in self.data[column].unique():
            print(i)
        print(f'Total: {len(self.data[column].unique())}')

    def selectJustRowsWith(self, entry, incolumn):
        smallerdata = self.data[self.data[incolumn] == entry]
        return smallerdata
