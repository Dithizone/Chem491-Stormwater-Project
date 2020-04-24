# Chem491-Stormwater-Project
(Current as of 2020.4.23)

This is the repository for the stormwater data mining project at 
CSU Channel Islands! We can imagine this project in a few discrete 
stages &mdash; Data acquisition, data wrangling and arranging, 
data exploration (e.g., PCA, covariance), and then the pretty 
graphs and charts.

### Data acquisition (Complete for F and G data)
The text from each PDF was extracted by ctrl-A and pasted into text files 
(see, e.g., ```data/raw/2019fg```). Text was then separated by whether or 
not it was F or G data (see ```data/precsv```) or non-data 
(see ```data/precsv/garbagefg.txt```). This was done with **historical/ExtractingData.py**.

### Data wrangling (F and G data complete)
Behold! ```data/TheFDataComplete.csv``` and ```data/TheGDataComplete.csv```.

Lines of data were separated by ```\n``` and ```' '``` and pieced back together 
in a .csv format using **historical/FDataGathering.py** and **historical/GDataGathering.py**, 
after which a LOT of cleaning had to be done to make names consistent and do band-aid 
fixes of errors due to my extracting method (e.g. ```y,Blank (HNO3||me equip blank``` 
had to be converted to ```Carboy Blank (HNO3||methanol),equip blank```). 
These fixes can be seen in **historical/FixingFData.py** and **historical/FixingGData.py**.

### Data arranging (Complete, with disclaimer)
Presently (2020.4.23), the data has since been converted so rows are dates and columns
are contituents, and separated by monitoring station. The resulting data sets have a 
shape of about (50, 200). This was done by **historical/pivotTable.py** and the (rough)
results can be seen in **StormwaterAnalysis.ipynb**

Disclaimer: The data has holes (which is problematic for many analyses) which might
be fixable by condensing dates from, say, ```2011-10-05 06:30:00``` and ```2011-10-05 13:50:00```
into a single date, ```2011-10-05```, or squishing into a range of several days.

I have worked with tensors and two decomposition methods (canonical polyadic and Tucker),
but since we're not looking at relationships between constituents or stations and instead
looking at these data relative to wildfires (not part of the tensor), this seems irrelevant.

### Additional data and future plans
Rainfall data (```data\rainfall\for <station name>```) has been collected, and the station and
wildfire locations are being assembled in Google Earth to aid in selecting specific stations
to explore.

Daphnia endpoint toxicity data is also being collected, to compare endpoint concentrations with 
pre- and post-fire levels in Ventura County, and/or to create plausible dose response curves 
(potentially using logit or probit models, as time permits).

Data concerning the Carr fire in northern California is also being sought, to explore 
similarities/differences between the two environments.

### Future plans
Once the stations and wildfire locations are assembled, specific subsets of our data can be
chosen for exploration to see changes after the fire.

Additionally, two other avenues of exploration (dose response prediction and NorCal/SoCal
comparison) will progress once data is procured.
