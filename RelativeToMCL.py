# This will take the data from the five stations and recalculate
# them as as fraction of their MCL. So like, if they equal 1 then
# they're at the MCL. Above or below 1 means above or below MCL.

import numpy as np
from UsefulThings import ME_VR2, \
    MO_SPA, \
    MO_FIL, \
    MO_THO, \
    ME_CC, \
    saveThisGraph
from copy import deepcopy
import matplotlib.pyplot as plt
import pandas as pd

# All MCLs in ng/L (from https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations#Organic )
# These are {'constituent': [MCL, Daphnia mortality EC50]}
lotsOfVariation = None  # This is so I can write lotsOfVariation as a note while keeping functionality

SRCity = pd.read_csv('data/tubbsFire/114SR0761_SWAMP.csv', index_col='SampleDate')
SRDownstream = pd.read_csv('data/tubbsFire/114MW0020.csv', index_col='SampleDate')

PAHMCLsAndDaphnia = {'Benz(a)anthracene': [(200 / 0.1), (np.average([0.000551139336, 0.00155877792]) * 1000000)],
                     'Benzo(a)pyrene': [(200 / 1), (np.average([0.001624910532, 0.000981506517]) * 1000000)],
                     'Benzo(b)fluoranthene': [(200 / 0.1), None],
                     'Benzo(k)fluoranthene': [(200 / 0.1), None],
                     'Dibenz(a||h)anthracene': [(200 / 1), (np.average([0.000551139336, 0.00155877792]) * 1000000)],
                     'Indeno(1||2||3-cd)pyrene': [(200 / 0.1), None]}

metalMCLsAndDaphnia = {'Cadmium': [5000, (0.0095 * 1000000)],
                       'Copper': [1300000, (0.039 * 1000000)],
                       'Lead': [15000, (0.168 * 1000000)],
                       'Mercury': [2000, (np.average([0.0027, 0.002]) * 1000000)],
                       'Nickel': [None, lotsOfVariation],
                       'Zinc': [None, lotsOfVariation]}

metalMCLs = ['Cadmium', 'Copper', 'Lead', 'Mercury']
PAHMCLs = ['Benz(a)anthracene',
           'Benzo(a)pyrene',
           'Benzo(b)fluoranthene',
           'Benzo(k)fluoranthene',
           'Dibenz(a||h)anthracene',
           'Indeno(1||2||3-cd)pyrene']

metalDaphnia = ['Cadmium', 'Copper', 'Lead', 'Mercury']
PAHDaphnia = ['Benz(a)anthracene',
              'Benzo(a)pyrene',
              'Dibenz(a||h)anthracene']


def convertToMCL(station, MCL0orDaphnia1, SantaRosa=False):
    for key in metalMCLsAndDaphnia.keys():
        if metalMCLsAndDaphnia[key][MCL0orDaphnia1] is not None:
            station[key] = station[key] / metalMCLsAndDaphnia[key][MCL0orDaphnia1]
    if SantaRosa is False:
        for otherkey in PAHMCLsAndDaphnia.keys():
            if PAHMCLsAndDaphnia[otherkey][MCL0orDaphnia1] is not None:
                station[otherkey] = station[otherkey] / PAHMCLsAndDaphnia[otherkey][MCL0orDaphnia1]


def makedeepcopy(station, SantaRosa=False):
    if SantaRosa is False:
        return deepcopy(
            station[['Cadmium', 'Copper', 'Lead', 'Mercury', 'Benz(a)anthracene', 'Benzo(a)pyrene', 'Benzo(b)fluoranthene',
                     'Benzo(k)fluoranthene', 'Dibenz(a||h)anthracene', 'Indeno(1||2||3-cd)pyrene']])
    if SantaRosa is True:
        return deepcopy(
            station[['Cadmium', 'Copper', 'Lead', 'Mercury']])

# Deepcopies of all stations, reframed as ratios of MCL and Daphnia EC50
ME_VR2MCL = makedeepcopy(ME_VR2)
ME_VR2Daphnia = makedeepcopy(ME_VR2)
convertToMCL(ME_VR2MCL, 0)
convertToMCL(ME_VR2Daphnia, 1)

MO_SPAMCL = makedeepcopy(MO_SPA)
MO_SPADaphnia = makedeepcopy(MO_SPA)
convertToMCL(MO_SPAMCL, 0)
convertToMCL(MO_SPADaphnia, 1)

MO_FILMCL = makedeepcopy(MO_FIL)
MO_FILDaphnia = makedeepcopy(MO_FIL)
convertToMCL(MO_FILMCL, 0)
convertToMCL(MO_FILDaphnia, 1)

MO_THOMCL = makedeepcopy(MO_THO)
MO_THODaphnia = makedeepcopy(MO_THO)
convertToMCL(MO_THOMCL, 0)
convertToMCL(MO_THODaphnia, 1)

ME_CCMCL = makedeepcopy(ME_CC)
ME_CCDaphnia = makedeepcopy(ME_CC)
convertToMCL(ME_CCMCL, 0)
convertToMCL(ME_CCDaphnia, 1)

SRCityMCL = makedeepcopy(SRCity, SantaRosa=True)
SRCityDaphnia = makedeepcopy(SRCity, SantaRosa=True)
convertToMCL(SRCityMCL, 0, SantaRosa=True)
convertToMCL(SRCityDaphnia, 1, SantaRosa=True)

SRDownstreamMCL = makedeepcopy(SRDownstream, SantaRosa=True)
SRDownstreamDaphnia = makedeepcopy(SRDownstream, SantaRosa=True)
convertToMCL(SRDownstreamMCL, 0, SantaRosa=True)
convertToMCL(SRDownstreamDaphnia, 1, SantaRosa=True)

# -----------------------------------------
# -----------------------------------------
# Now, pretty graphs of each for MCL ------
# -----------------------------------------
# -----------------------------------------

plt.figure(1, figsize=(14, 5))
plt.suptitle('MCL, Ventura River', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalMCLs:
    plt.plot(ME_VR2MCL[i], label=i)
plt.ylabel('Fraction of MCL')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-05-23', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHMCLs:
    plt.plot(ME_VR2MCL[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-05-23', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/MCLVRmetalPAH.png')
plt.show()

plt.figure(2, figsize=(14, 5))
plt.suptitle('MCL, Santa Paula', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalMCLs:
    plt.plot(MO_SPAMCL[i], label=i)
plt.ylabel('Fraction of MCL')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2016-12-16', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHMCLs:
    plt.plot(MO_SPAMCL[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2016-12-16', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/MCLSPAmetalPAH.png')
plt.show()

plt.figure(3, figsize=(14, 5))
plt.suptitle('MCL, Fillmore', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalMCLs:
    plt.plot(MO_FILMCL[i], label=i)
plt.xlabel('Date')
plt.ylabel('Fraction of MCL')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-08-02', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHMCLs:
    plt.plot(MO_FILMCL[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-08-02', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/MCLFILmetalPAH.png')
plt.show()

plt.figure(4, figsize=(14, 5))
plt.suptitle('MCL, Calleguas Creek', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalMCLs:
    plt.plot(ME_CCMCL[i], label=i)
plt.ylabel('Fraction of MCL')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHMCLs:
    plt.plot(ME_CCMCL[i], label=i)
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/MCLCCmetalPAH.png')
plt.show()

plt.figure(5, figsize=(14, 5))
plt.suptitle('MCL, Thousand Oaks', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalMCLs:
    plt.plot(MO_THOMCL[i], label=i)
plt.xlabel('Date')
plt.ylabel('Fraction of MCL')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHMCLs:
    plt.plot(MO_THOMCL[i], label=i)
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/MCLTHOmetalPAH.png')
plt.show()

# -----------------------------------------
# -----------------------------------------
# Now, pretty graphs of each for Daphnia --
# -----------------------------------------
# -----------------------------------------

plt.figure(6, figsize=(14, 5))
plt.suptitle('Daphnia EC50, Ventura River', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalDaphnia:
    plt.plot(ME_VR2Daphnia[i], label=i)
plt.ylabel('Fraction of Daphnia EC50')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-05-23', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHDaphnia:
    plt.plot(ME_VR2Daphnia[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-05-23', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/DaphniaVRmetalPAH.png')
plt.show()

plt.figure(7, figsize=(14, 5))
plt.suptitle('Daphnia EC50, Santa Paula', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalDaphnia:
    plt.plot(MO_SPADaphnia[i], label=i)
plt.ylabel('Fraction of Daphnia EC50')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2016-12-16', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHDaphnia:
    plt.plot(MO_SPADaphnia[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2016-12-16', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/DaphniaSPAmetalPAH.png')
plt.show()

plt.figure(8, figsize=(14, 5))
plt.suptitle('Daphnia EC50, Fillmore', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalDaphnia:
    plt.plot(MO_FILDaphnia[i], label=i)
plt.xlabel('Date')
plt.ylabel('Fraction of Daphnia EC50')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-08-02', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHDaphnia:
    plt.plot(MO_FILDaphnia[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-08-02', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/DaphniaFILmetalPAH.png')
plt.show()

plt.figure(9, figsize=(14, 5))
plt.suptitle('Daphnia EC50, Calleguas Creek', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalDaphnia:
    plt.plot(ME_CCDaphnia[i], label=i)
plt.ylabel('Fraction of Daphnia EC50')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHDaphnia:
    plt.plot(ME_CCDaphnia[i], label=i)
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/DaphniaCCmetalPAH.png')
plt.show()

plt.figure(10, figsize=(14, 5))
plt.suptitle('Daphnia EC50, Thousand Oaks', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in metalDaphnia:
    plt.plot(MO_THODaphnia[i], label=i)
plt.xlabel('Date')
plt.ylabel('Fraction of Daphnia EC50')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.legend(loc='upper center', bbox_to_anchor=(-0.3, 0.8))
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in PAHDaphnia:
    plt.plot(MO_THODaphnia[i], label=i)
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2018-05-30', linewidth=3)
plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(1.3, 0.8))
# saveThisGraph(filepathtosavepng='images/forpaper/DaphniaTHOmetalPAH.png')
plt.show()

# --------------------------------------------
# ------- Pretty graphs for Santa Rosa -------
# --------------------------------------------

# SRCity MCL
plt.figure(11, figsize=(7, 5))
plt.title('MCL, in Santa Rosa', fontsize=18)
for i in metalMCLs:
    plt.plot(SRCityMCL[i], label=i)
plt.ylabel('Fraction of MCL')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2011-11-29', linewidth=3)
plt.legend(loc='best')
plt.xticks(rotation=90)
saveThisGraph(filepathtosavepng='images/forpaper/MCLSRCityMetal.png')
plt.show()

# SR Downstream MCL
plt.figure(12, figsize=(7, 5))
plt.title('MCL, downstream of Santa Rosa', fontsize=18)
for i in metalMCLs:
    plt.plot(SRDownstreamMCL[i], label=i)
plt.ylabel('Fraction of MCL')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-02-07', linewidth=3)
plt.legend(loc='best')
plt.xticks(rotation=90)
saveThisGraph(filepathtosavepng='images/forpaper/MCLSRDownstreamMetal.png')
plt.show()

# SRCity Daphnia
plt.figure(13, figsize=(7, 5))
plt.title('Daphnia EC50, in Santa Rosa', fontsize=18)
for i in metalMCLs:
    plt.plot(SRCityDaphnia[i], label=i)
plt.ylabel('Fraction of MCL')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2011-11-29', linewidth=3)
plt.legend(loc='best')
plt.xticks(rotation=90)
saveThisGraph(filepathtosavepng='images/forpaper/DaphniaSRCityMetal.png')
plt.show()

# SR Downstream Daphnia
plt.figure(14, figsize=(7, 5))
plt.title('Daphnia EC50, downstream of Santa Rosa', fontsize=18)
for i in metalMCLs:
    plt.plot(SRDownstreamDaphnia[i], label=i)
plt.ylabel('Fraction of MCL')
plt.xlabel('Date')
plt.axhline(y=1, linewidth=3)
plt.axvline(x='2017-02-07', linewidth=3)
plt.legend(loc='best')
plt.xticks(rotation=90)
saveThisGraph(filepathtosavepng='images/forpaper/DaphniaSRDownstreamMetal.png')
plt.show()
