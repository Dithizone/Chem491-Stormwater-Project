# This is a collection of useful functions, lists, and such
# so they don't clutter up other working files!

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
