# Chem491-Stormwater-Project
This is the repository for the stormwater data mining project at CSU Channel Islands! We can imagine this project in a few discrete stages &mdash; Data acquisition, data wrangling and arranging, data exploration (e.g., PCA, covariance), and then the pretty graphs and charts.

### Data acquisition (Complete for F and G data)
The text from each PDF was extracted by ctrl-A and pasted into text files (see, e.g., ```data/raw/2019fg```). Text was then separated by whether or not it was F or G data (see ```data/precsv```) or non-data (see ```data/precsv/garbagefg.txt```).

### Data wrangling (F data complete, G data in progress)
The plan is to separate the raw data by whether they came from Appendix F or G and mold them into a .csv format. This is complete for F data (Behold! ```data/FDataComplete.csv```)

A LOT of cleaning had to be done to make names consistent and do band-aid fixes of errors due to my extracting method (e.g. ```y,Blank (HNO3||me equip blank``` had to be converted to ```Carboy Blank (HNO3||methanol),equip blank```). These can be seen in **historical/FixingFData.py**.

The F data is complete and the G data is just beginning. Presently, the data is arranged exactly as it is in the PDFs, but will be more useful with pollutants along one axis and dates along another (and maybe sampling station along a third).

### Data arranging
I imagine the structure will be ```index='dates'``` and ```header=pollutants``` for covariance tests and a transpose will need to be done for PCA. Pollutants and analysis method will need to be combined (e.g., "Copper (LCS)" and "Copper (Matrix Spike)") so the ```Result``` column can be used as the values after doing the ```pandas.DataFrame.pivot_table()``` thing.

One option for arranging: we could create a 3-way tensor ```(sampling date, pollutant name, sampling location)``` if I get proficient enough in that soon.

### Data exploration
Clustering in PCA will reveal if certain pollutants are related and correlate with each other, especially in wildfire-relevant times, as will covariance. NMF may be valuable if some pollutant behaviors are wildfire-dependant and others are not.

Anyway, this is where the fun begins! We'll just have to get creative.

### PG;NP
Maybe determining a non-wildfire rhythm and subtracting it out (i.e. graphing only the pollutants' deviation from typical behavior) will be the most elegant way of making pretty pictures. We'll see what the exploration stage shows, though!
