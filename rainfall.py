# This will need to scrub the data of unnecessary (but helpful!)
# data at the top and bottom of the rainfall stuff, and turn it
# into something Pandas-able. Rainfall data can be found here:
# https://www.vcwatershed.net/hydrodata/php/getstations.php?dataset=rain_day&order=name

# The location of the rainfall data is data/rainfall/for <station name>

from UsefulThings import stationIDsAndSelectedRainfallStation

# Prints the rainfall data info I scribbled down
for i in stationIDsAndSelectedRainfallStation.keys():
    print(f'{i}:\t{stationIDsAndSelectedRainfallStation[i]}')
