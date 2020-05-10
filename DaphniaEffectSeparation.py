# This separates the data by effect (e.g., "Mortality" or "Immobilization")
# Then it will simplify the data into just three columns: Endpoint, Chemical
# Name, and Effect Measurement.

import pandas as pd

daphniadata = pd.read_csv('data/ecotox/DaphniaECOTOX.csv', index_col=0)
print(f'DaphniaData is {daphniadata.shape}')
print(f'------- The columns -------')
print(daphniadata.columns.values)
print(f'\n------- The endpoints -------')
print(daphniadata['Endpoint'].unique())
print(f'\n------- The effects -------')
for effect in daphniadata['Effect'].unique():
    effectdata = daphniadata[daphniadata["Effect"] == effect]
    print(
        f'{effectdata.shape[0]} entries for {effect}. The measurements are: {effectdata["Effect Measurement"].unique()}. The endpoints involved are: {effectdata["Endpoint"].unique()}.\n')


def daphniasubset(effect):
    data = daphniadata[daphniadata['Effect'] == effect]
    return data


mortalitydata = daphniasubset('Mortality')
immobilizationdata = daphniasubset('Intoxication')
reproductiondata = daphniasubset('Reproduction')
growthdata = daphniasubset('Growth')

listofdaphniadata = [mortalitydata, immobilizationdata, reproductiondata, growthdata]
listofdaphniadatanames = ['mortalitydata', 'immobilizationdata', 'reproductiondata', 'growthdata']

namenumber = 0
for data in listofdaphniadata:
    print(f'------- {data["Effect"].unique()} ({data.shape[0]}) -------')
    for measurement in data['Effect Measurement'].unique():
        measurementdata = data[data['Effect Measurement'] == measurement]
        print(
            f'{measurement} has {measurementdata.shape[0]} entries. Compounds tested are: {measurementdata["Chemical Name"].unique()}\n')
    # data.to_csv(path_or_buf=f'data/ecotox/{listofdaphniadatanames[namenumber]}.csv')
    namenumber += 1

print(f'------- Simple Mortality Data -------')


def simplify(dataframe):
    simple = dataframe[['Effect Measurement',
                        'Endpoint',
                        'Chemical Name',
                        'Conc 1 Mean (Standardized)',
                        'Conc 1 Units (Standardized)']] \
        .sort_values(by='Chemical Name') \
        .reset_index() \
        .drop(columns='index')
    return simple


simplemortality = simplify(mortalitydata)
simplerimmobilization = simplify(immobilizationdata)
simplereproduction = simplify(reproductiondata)
simplegrowth = simplify(growthdata)

simplelist = [simplemortality, simplerimmobilization, simplereproduction, simplegrowth]
simplename = ['simplemortality', 'simplerimmobilization', 'simplereproduction', 'simplegrowth']

# for simple in range(len(simplelist)):
#     simplelist[simple].to_csv(path_or_buf=f'data/ecotox/{simplename[simple].replace("simple", "focused")}.csv')
