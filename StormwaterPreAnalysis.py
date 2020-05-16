# This is just a faster way to make and test out graphs
# before putting them in the Jupyter Notebook.
# (StormwaterAnalysis.ipynb)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from UsefulThings import ME_VR2,\
    MO_SPA,\
    MO_FIL,\
    MO_THO,\
    ME_CC,\
    saveThisGraph,\
    theToxicPAHs,\
    subsetOfTheMetals,\
    constituentsWeWant
from matplotlib.dates import YearLocator

scaledME_VR2 = MinMaxScaler().fit_transform(ME_VR2.values)
scaledMO_SPA = MinMaxScaler().fit_transform(MO_SPA.values)
scaledMO_FIL = MinMaxScaler().fit_transform(MO_FIL.values)
scaledME_CC = MinMaxScaler().fit_transform(ME_CC.values)
scaledMO_THO = MinMaxScaler().fit_transform(MO_THO.values)

ME_VR2data = pd.DataFrame(data=scaledME_VR2)
MO_SPAdata = pd.DataFrame(data=scaledMO_SPA)
MO_FILdata = pd.DataFrame(data=scaledMO_FIL)
ME_CCdata = pd.DataFrame(data=scaledME_CC)
MO_THOdata = pd.DataFrame(data=scaledMO_THO)

ME_VR2data.columns = constituentsWeWant
ME_VR2data.index = ME_VR2.index
MO_SPAdata.columns = constituentsWeWant
MO_SPAdata.index = MO_SPA.index
MO_FILdata.columns = constituentsWeWant
MO_FILdata.index = MO_FIL.index
ME_CCdata.columns = constituentsWeWant
ME_CCdata.index = ME_CC.index
MO_THOdata.columns = constituentsWeWant
MO_THOdata.index = MO_THO.index

# ----------------------
# ----- The Metals -----
# ----------------------
plt.figure(1, figsize=(25, 5))
plt.suptitle('Behavior of Metals Due to Thomas Fire', fontsize=22)

plt.subplot(1, 3, 1)
plt.title('Mass Emissions, Ventura River')
for i in subsetOfTheMetals:
    plt.plot(ME_VR2data[i], label=i)
plt.ylabel('Standardized Frequency')
plt.xlabel('Date')
plt.axvline(x='2017-05-23', linewidth=5)
plt.xticks(rotation=90)
plt.legend()

plt.subplot(1, 3, 2)
plt.title('Major Outfall, Fillmore')
for i in subsetOfTheMetals:
    plt.plot(MO_FILdata[i], label=i)
plt.xlabel('Date')
plt.axvline(x='2017-08-02', linewidth=5)
plt.xticks(rotation=90)

plt.subplot(1, 3, 3)
plt.title('Major Outfall, Santa Paula')
for i in subsetOfTheMetals:
    plt.plot(MO_SPAdata[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2016-12-16', linewidth=5)
# saveThisGraph(filepathtosavepng='images/thomasmetals.png')

plt.show()


# --------------------
# ----- The PAHs -----
# --------------------
plt.figure(2, figsize=(25, 5))
plt.suptitle('Behavior of PAHs Due to Thomas Fire', fontsize=22)

plt.subplot(1, 3, 1)
plt.title('Mass Emissions, Ventura River')
for i in theToxicPAHs:
    plt.plot(ME_VR2data[i], label=i)
plt.ylabel('Standardized Frequency')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2017-05-23', linewidth=5)
plt.legend()

plt.subplot(1, 3, 2)
plt.title('Major Outfall, Fillmore')
for i in theToxicPAHs:
    plt.plot(MO_FILdata[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2017-08-02', linewidth=5)

plt.subplot(1, 3, 3)
plt.title('Major Outfall, Santa Paula')
for i in theToxicPAHs:
    plt.plot(MO_SPAdata[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2016-12-16', linewidth=5)
# saveThisGraph(filepathtosavepng='images/thomasPAHs.png')

plt.show()

# -------------------------------
# -------------------------------
# -------- The Hill Fire --------
# -------------------------------
# -------------------------------

# ------------------
# ----- Metals -----
# ------------------

plt.figure(3, figsize=(15, 5))
plt.suptitle('Behavior of Metals Due to Hill Fire', fontsize=22)

plt.subplot(1, 2, 1)
plt.title('Mass Emissions, Calleguas Creek')
for i in subsetOfTheMetals:
    plt.plot(ME_CCdata[i], label=i)
plt.ylabel('Standardized Frequency')
plt.xlabel('Date')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Major Outfall, Thousand Oaks')
for i in subsetOfTheMetals:
    plt.plot(MO_THOdata[i], label=i)
plt.xlabel('Date')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)

# saveThisGraph(filepathtosavepng='images/hillmetals.png')

plt.show()

# ------------------
# ----- Metals -----
# ------------------

plt.figure(4, figsize=(15, 5))
plt.suptitle('Behavior of PAHs Due to Hill Fire', fontsize=22)

plt.subplot(1, 2, 1)
plt.title('Mass Emissions, Calleguas Creek')
for i in theToxicPAHs:
    plt.plot(ME_CCdata[i], label=i)
plt.ylabel('Standardized Frequency')
plt.xlabel('Date')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Major Outfall, Thousand Oaks')
for i in theToxicPAHs:
    plt.plot(MO_THOdata[i], label=i)
plt.xlabel('Date')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)

# saveThisGraph(filepathtosavepng='images/hillPAHs.png')

plt.show()

# ------------------------- Now, separated by station rather than by metal/PAH -------------------------

plt.figure(5, figsize=(14, 5))
plt.suptitle('Mass Emissions, Ventura River', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in subsetOfTheMetals:
    plt.plot(ME_VR2data[i], label=i)
plt.ylabel('Standardized Frequency')
plt.xlabel('Date')
plt.axvline(x='2017-05-23', linewidth=5)
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in theToxicPAHs:
    plt.plot(ME_VR2data[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2017-05-23', linewidth=5)
plt.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8))
# saveThisGraph(filepathtosavepng='images/VRmetalPAH.png')
plt.show()

plt.figure(6, figsize=(14, 5))
plt.suptitle('Major Outfall, Santa Paula', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in subsetOfTheMetals:
    plt.plot(MO_SPAdata[i], label=i)
plt.ylabel('Standardized Frequency')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2016-12-16', linewidth=5)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in theToxicPAHs:
    plt.plot(MO_SPAdata[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2016-12-16', linewidth=5)
plt.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8))
# saveThisGraph(filepathtosavepng='images/SPAmetalPAH.png')
plt.show()

plt.figure(7, figsize=(14, 5))
plt.suptitle('Major Outfall, Fillmore', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in subsetOfTheMetals:
    plt.plot(MO_FILdata[i], label=i)
plt.xlabel('Date')
plt.ylabel('Standardized Frequency')
plt.axvline(x='2017-08-02', linewidth=5)
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in theToxicPAHs:
    plt.plot(MO_FILdata[i], label=i)
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.axvline(x='2017-08-02', linewidth=5)
plt.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8))
# saveThisGraph(filepathtosavepng='images/FILmetalPAH.png')
plt.show()

plt.figure(8, figsize=(14, 5))
plt.suptitle('Mass Emissions, Calleguas Creek', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in subsetOfTheMetals:
    plt.plot(ME_CCdata[i], label=i)
plt.ylabel('Standardized Frequency')
plt.xlabel('Date')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in theToxicPAHs:
    plt.plot(ME_CCdata[i], label=i)
plt.xlabel('Date')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8))
# saveThisGraph(filepathtosavepng='images/CCmetalPAH.png')
plt.show()

plt.figure(9, figsize=(14, 5))
plt.suptitle('Major Outfall, Thousand Oaks', fontsize=22)
plt.subplot(1, 2, 1)
plt.title('Metals')
for i in subsetOfTheMetals:
    plt.plot(MO_THOdata[i], label=i)
plt.xlabel('Date')
plt.ylabel('Standardized Frequency')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
plt.title('PAHs')
for i in theToxicPAHs:
    plt.plot(MO_THOdata[i], label=i)
plt.xlabel('Date')
plt.axvline(x='2018-05-30', linewidth=5)
plt.xticks(rotation=90)
plt.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8))
# saveThisGraph(filepathtosavepng='images/THOmetalPAH.png')
plt.show()
